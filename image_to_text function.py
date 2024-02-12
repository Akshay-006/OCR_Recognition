import pytesseract
import cv2
from pytesseract import Output



myconfig=r"--psm 6 --oem 3"

def image_to_text(img):
    img=cv2.imread(img)
    str= ''

    height, width, _ = img.shape

    result = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)
    amount_boxes = len(result['text'])
    for i in range(amount_boxes):
        if float(result['conf'][i]) > 80:
            str += result['text'][i]+ ' '

    print(str)

image_to_text("image2.jpeg")