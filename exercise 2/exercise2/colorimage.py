import numpy as np
import cv2
src="/Users/chai/Desktop/exercise2/Test_images/" 
names=["Lenna.png","coins.png","baboon.jpg","cameraman.png","rice_grains.jpg","barbara.png"]

for i in names:
    srcc=src+i
    img=cv2.imread(srcc,cv2.IMREAD_COLOR)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    ycrcb=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
    R,G,B=cv2.split(img)
    H,S,V=cv2.split(hsv)
    Y,cr,cb=cv2.split(ycrcb)
    
    print(i+" "+"RGB"+":",img[20,25])
    print(i+" "+"HSV"+":",hsv[20,25])
    print(i+" "+"ycrcb"+":",ycrcb[20,25])
    
    cv2.imwrite("R"+"_"+i,R)
    cv2.imwrite("G"+"_"+i,G)
    cv2.imwrite("B"+"_"+i,B)
    cv2.imwrite("H"+"_"+i,H)
    cv2.imwrite("S"+"_"+i,S)
    cv2.imwrite("V"+"_"+i,V)
    cv2.imwrite("Y"+"_"+i,Y)
    cv2.imwrite("cr"+"_"+i,cr)
    cv2.imwrite("cb"+"_"+i,cb)
