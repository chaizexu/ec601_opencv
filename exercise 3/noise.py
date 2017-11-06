# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np

def Add_gaussian_Noise(pic, mean, sigma):
    
    noice_pic=pic.copy()
    cv2.randn(noice_pic,mean,sigma)
    cv2.add(pic, noice_pic, noice_pic)
    
    return noice_pic

def Add_salt_pepper_Noise(pic, pa, pb):
    amount1 = int(pic.shape[0]*pic.shape[1]*pa)
    amount2 = int(pic.shape[0]*pic.shape[1]*pb)
    
    noisepic=pic
    
    for i in range(amount1):
        noisepic[np.random.randint(0,pic.shape[0]-1), np.random.randint(0,pic.shape[1]-1)]=0
        
    for i in range(amount2):
        noisepic[np.random.randint(0,pic.shape[0]-1), np.random.randint(0,pic.shape[1]-1)]=255
        
    return noisepic

def main():
    mean = 0
    sigma = 100
    pa = 0.01
    pb = 0.01
    
    pic = cv2.imread("./Lenna.png")
    gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("./LennaGray.png",gray)
    
    gauss_noiseImage = Add_gaussian_Noise(gray,mean,sigma)
    cv2.imwrite("./gaussiannoise.png",gauss_noiseImage)
    boxfilter_img = cv2.boxFilter(gauss_noiseImage, -1, (3, 3))
    cv2.imwrite("./gaussianBoxfilter.png",boxfilter_img)
    gaussfilter_img=cv2.GaussianBlur(gauss_noiseImage, (3,3), 1.5, 3)
    cv2.imwrite("./gaussianGaussfilter.png",gaussfilter_img)
    medianfilter_img=cv2.medianBlur(gauss_noiseImage,5)
    cv2.imwrite("./gaussianMedianfilter.png",medianfilter_img)
    
    pepper_saltImage=Add_salt_pepper_Noise(gray,pa,pb)
    cv2.imwrite("./peppersaltnoise.png",pepper_saltImage)
    boxfilter_img = cv2.boxFilter(pepper_saltImage, -1, (3, 3))
    cv2.imwrite("./peppersaltBoxfilter.png",boxfilter_img)
    gaussfilter_img=cv2.GaussianBlur(pepper_saltImage, (3,3), 1.5, 3)
    cv2.imwrite("./peppersaltGaussfilter.png",gaussfilter_img)
    medianfilter_img=cv2.medianBlur(pepper_saltImage,5)
    cv2.imwrite("./peppersaltMedianfilter.png",medianfilter_img)
    
if __name__ == "__main__":
    main()