import numpy as np
import cv2

cap=cv2.VideoCapture(1)

while(1):
    
    _,frame=cap.read()

    red=np.matrix(frame[:,:,2])
    green=np.matrix(frame[:,:,1])
    blue=np.matrix(frame[:,:,0])

    red_only = np.int16(red) - np.int16(green) - np.int16(blue)

    red_only[red_only<0]=0
    red_only[red_only>255]=255

    column_sums=np.matrix(np.sum(red_only,0))
    column_numbers=np.matrix(np.arange(1,641))
    column_mult=np.multiply(column_sums,column_numbers)
    total=np.sum(column_mult)
    total_total=np.sum(np.sum(red_only))
    column_location=total/total_total

    print(column_location)

    red_only=np.uint8(red_only)

    cv2.imshow('RGB',frame)
    cv2.imshow('Red',red)
    cv2.imshow('Green',green)
    cv2.imshow('Blue',blue)
    cv2.imshow('red only',red_only)
    
    k=cv2.waitKey(5)
    if k==27:
        break

cv2.destroyAllWindows()

print(frame)    
print(np.shape(red_only))
