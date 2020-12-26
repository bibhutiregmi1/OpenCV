import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab

# img = cv2.imread('1.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))

### Detecting Characters
# hImg, wImg, _ = img.shape
# cong = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_boxes(img,config=cong)
# for b in boxes.splitlines():
#     b = b.split(' ')
#     x, y, w, h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
#     cv2.putText(img,b[0], (x,hImg-y+25), cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
#

# DETECTING WORDS
# hImg, wImg, _ = img.shape
# boxes = pytesseract.image_to_data(img)
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b = b.split()
#         if len(b)==12:
#             x, y, w, h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)
#             cv2.putText(img,b[11], (x,y+2), cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

# DETECTING NUMBERS
# hImg, wImg, _ = img.shape
# config_txt = r'--oem 3 --psm 6  tessedit_char_whitelist=0123456789'
# boxes = pytesseract.image_to_data(img,config=config_txt)
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b = b.split()
#         if len(b)==12:
#             x, y, w, h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)
#             cv2.putText(img,b[11], (x,y+2), cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)


##############################################
##### Webcam and Screen Capture Example ######
##############################################
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
def captureScreen(bbox=(300,300,1500,1000)):
    capScr = np.array(ImageGrab.grab(bbox))
    capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    return capScr

while True:
    timer = cv2.getTickCount()
    _,img = cap.read()
    #img = captureScreen()
    #DETECTING CHARACTERES
    hImg, wImg,_ = img.shape
    boxes = pytesseract.image_to_boxes(img)
    for b in boxes.splitlines():
        #print(b)
        b = b.split(' ')
        #print(b)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
        cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    #cv2.putText(img, str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20,230,20), 2);
    cv2.imshow("Result",img)
    cv2.waitKey(1)


# cv2.imshow('Result', img)
# cv2.waitKey(0)
