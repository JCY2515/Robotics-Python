#Lab 10 - Object Identification
#Wong Chung Yin

import numpy as np
import cv2

cap=cv2.VideoCapture(1)

while(1):
    _,frame=cap.read()

    red=np.matrix(frame[:,:,2])
    green=np.matrix(frame[:,:,1])
    blue=np.matrix(frame[:,:,0])

    red_only=np.int16(red)-np.int16(green)-np.int16(blue)

    red_only[red_only<0]=0
    red_only[red_only>255]=255

    red_only=np.uint8(red_only)

    mask=np.ones((5,5),np.uint8)
    opening=cv2.morphologyEx(red_only,cv2.MORPH_OPEN,mask)
    cv2.imshow('Masked image',opening)

    _,labels=cv2.connectedComponents(opening,4)
    b=np.matrix(labels)

    Obj1=b==0
    Obj1=np.uint8(Obj1)
    Obj1[Obj1>0]=255
    cv2.imshow('First Object',Obj1)

    Obj2=b==1
    Obj2=np.uint8(Obj2)
    Obj2[Obj2>0]=255
    cv2.imshow('Second Object',Obj2)

    Obj3=b==2
    Obj3=np.uint8(Obj3)
    Obj3[Obj3>0]=255
    cv2.imshow('Third Object',Obj3)

    Obj4=b==3
    Obj4=np.uint8(Obj4)
    Obj4[Obj4>0]=255
    cv2.imshow('Fourth Object',Obj4)
    

    cv2.imshow('Frame',frame)
    cv2.imshow('Red Only',red_only)

    k=cv2.waitKey(5)
    if k==27:
        break

cv2.destroyAllWindows()
print(np.amax(labels))
