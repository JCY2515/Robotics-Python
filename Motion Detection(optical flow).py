## Modified for red only
import numpy as np
import cv2
import time


threshold = 100
step = 16 #the number of pixels within each block the velocity is being looked for

def draw_flow(img, flow):
    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y,x].T
    lines = np.vstack([x, y, x-fx, y-fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    img_bgr = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.polylines(img_bgr, lines, 0, (0, 255, 0))
    for (x1, y1), (_x2, _y2) in lines:
        cv2.circle(img_bgr, (x1, y1), 1, (0, 255, 0), -1)
    return img_bgr

###################################
#*****Parameters a dense optical flow using the Gunnar Farneback's algorithm.
#computed flow image that has the same size as prev and type CV_32FC2
flow=None

#parameter, specifying the image scale (<1) to build pyramids for each image;
#pyrScale=0.5 means a classical pyramid, where each next layer is twice smaller than the previous one.
pyrScale=0.5

#number of pyramid layers including the initial image; levels=1 means that no extra layers are created and only the original images are used.
levels=3

#averaging window size; larger values increase the algorithm robustness to
#image noise and give more chances for fast motion detection, but yield more blurred motion field.
winsize=15

#number of iterations the algorithm does at each pyramid level.
iterations=3

#size of the pixel neighborhood used to find polynomial expansion in each pixel; larger values mean that the image will be approximated with
#smoother surfaces, yielding more robust algorithm and more blurred motion field, typically poly_n =5 or 7.
polyN=5

#standard deviation of the Gaussian that is used to smooth derivatives used as a basis for the polynomial expansion; for polyN=5, you can
#set polySigma=1.1, for polyN=7, a good value would be polySigma=1.5.
polySigma=1.2

#operation flags that can be a combination of OPTFLOW_USE_INITIAL_FLOW and/orOPTFLOW_FARNEBACK_GAUSSIAN
flags = 0
cap = cv2.VideoCapture(0)
suc, prev = cap.read()

## Seperate into color layers to get Red Only
red = np.matrix(prev[:,:,2])
blue = np.matrix(prev[:,:,0])
green = np.matrix(prev[:,:,1])
red_Only = np.int16(red)-np.int16(green)-np.int16(blue)

# Threshold to B/W image
red_Only[red_Only<threshold] = 0
red_Only[red_Only>=threshold] = 255

#Convervting to correct image type values
red_Only=np.uint8(red_Only)

#Save this as the previous red only image
prevRed = red_Only

####motion tracking on all colors/gray scale
##prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

while True:
    suc, img = cap.read()
    
    ## Seperate into color layers to get Red Only
    red = np.matrix(img[:,:,2])
    blue = np.matrix(img[:,:,0])
    green = np.matrix(img[:,:,1])
    red_Only = np.int16(red)-np.int16(green)-np.int16(blue)
    
    # Threshold to B/W image
    red_Only[red_Only<threshold] = 0
    red_Only[red_Only>=threshold] = 255
    
    #Convervting to correct image type values
    red_Only=np.uint8(red_Only)
    
    #take curren image and convert to Gray scale for better visual later
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # start time to calculate FPS
    start = time.time()
    
    ######Computes a dense optical flow using the Gunnar Farneback's algorithm.
    flow = cv2.calcOpticalFlowFarneback(prevRed, red_Only, flow, pyrScale, levels, winsize, iterations,
    polyN, polySigma, flags)
    prevRed = red_Only
    
##    ##motion tracking on all colors/gray scale
##    flow = cv2.calcOpticalFlowFarneback(prevgray, gray, flow, pyrScale, levels, winsize, iterations, polyN, polySigma, flags)
##    prevgray = gray

    # End time
    end = time.time()
    
    # calculate the FPS for current frame detection
    fps = 1 / (end-start)
    print(f"{fps:.2f} FPS")
    cv2.imshow('flow', draw_flow(gray, flow))
    
    key = cv2.waitKey(5)
    if key == 27: #esc key to break out of the while loop
        break
    
cap.release()
cv2.destroyAllWindows()
cv2.imshow('flow', draw_flow(gray, flow))
