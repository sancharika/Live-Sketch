from typing import no_type_check
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True: #accepting image and allowing to select ROI (region of interest)
    res,im=cap.read()
    roi=cv2.selectROI("original",im,False#for grid line
    ,False #for selecting from center || center method
    ) #allows to select a image
    cv2.destroyAllWindows()
    break
while True:
    ret,frame=cap.read()
    image=frame[int(roi[1]):int(roi[1]+roi[3]),
    (roi[0]):int(roi[0]+roi[2])] #slice

    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image=cv2.GaussianBlur(image,(7,7),0)
    image=cv2.Canny(image,14,62)
    ret,image =cv2.threshold(image,50,255,cv2.THRESH_BINARY_INV)

    image=cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
    frame[int(roi[1]):int(roi[1]+roi[3]),
    int(roi[0]):int(roi[0]+roi[2])]=image

    cv2.imshow("sketch",frame)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


