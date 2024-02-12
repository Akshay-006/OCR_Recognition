import os

import  pdfminer.high_level
import pytesseract
import cv2
from pytesseract import Output
import io
import fitz
import PIL.Image
import mysql.connector as db

myconfig=r"--psm 6 --oem 3" #config for tesseract ocr to open a img in this config
image_text="" # empty text which will be added with the text in an image
pdf_text=""



def image_to_text(img):
    img=cv2.imread(img) #reads image
    global image_text #global value of image

    data=pytesseract.image_to_data(img,config=myconfig,output_type=Output.DICT)
    """converts image to data 
    which is of a dictionary consisting key values as image , ext , text which has the following byte values"""
    amount_of_boxes=len(data['text']) # length of text present in an image
    for i in range(amount_of_boxes):
        if float(data['conf'][i])>80: # conf is value of confidence that the text readed is correct
            image_text+=data['text'][i]+' ' # adding the texts in the image in the string variable
    return image_text


def get_pdf(pdf):

    #for pdf text

    global pdf_text
    pdf_text=pdfminer.high_level.extract_text(pdf)

    #for image text

    pdf=fitz.open(pdf)
    counter=1

    for i in range(len(pdf)):
        page=pdf[i]
        images=page.get_images()
        for image in images:
            base_img=pdf.extract_image(image[0])
            image_data=base_img['image']
            img=PIL.Image.open(io.BytesIO(image_data))
            extension=base_img['ext']
            img.save(f"image{counter}.{extension}")
            image_to_text(f"image{counter}.{extension}")
            counter+=1


a=input("Enter the pdf name with extension (example1.pdf): ")
get_pdf(a)


#storing the values in database

def store_in_database(image_text,pdf_text):
    connection=db.connect(
        host="localhost",
        user="root",
        password="password",
        database="pdf_to_text"
    )

    cursor=connection.cursor()

    select_query = '''SELECT IF(COUNT(*) > 0, (SELECT MAX(Sno) FROM text), NULL) AS max_sno 
        FROM text'''

    cursor.execute(select_query)

    result = cursor.fetchone()

    S_no = result[0]
    if S_no is not None:
        S_no += 1
    else:
        S_no = 1

    row = (S_no,image_text,pdf_text)

    insert_query="INSERT INTO TEXT VALUES(%s , %s , %s)"



    cursor.execute(insert_query,row)
    connection.commit()

    cursor.close()
    connection.close()

    if connection.is_connected()==False:
        for image in os.listdir():
            if image.endswith(".jpeg") or image.endswith(".png"):
                os.remove(image)

store_in_database(image_text,pdf_text)





























