import pytesseract
import cv2
from pytesseract import Output

str=""


myconfig = r"--psm 6 --oem 3"

img=cv2.imread("test2.jpeg")
height, width, _ = img.shape

result=pytesseract.image_to_data(img,config=myconfig,output_type=Output.DICT)

amount_boxes=len(result['text'])

for i in range(amount_boxes):
    if float(result['conf'][i]) > 50:
        (x,y,height,width)=  (result['left'][i],result['top'][i],result['height'][i],result['width'][i])
        cv2.rectangle(img,(x,y),(x+width,y+height),(0,255,0),2)
        print(result['text'][i])
        str+=result['text'][i]+' '

print(str)

'''f=open("text.txt",'w')
f.write(str)
f.close()'''