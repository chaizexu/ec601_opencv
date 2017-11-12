#!/usr/bin/env plocation[1]thon3
# -*- coding: utf-8 -*-

import cv2
import numpy as np


def TemplateMatching(src,temp,stepsize):

    a = src.shape[0]
    b = src.shape[1]
    n1 = temp.shape[0]
    t = temp.shape[1]
    avgt = np.mean(temp)
    vart = np.var(temp)
    ncc = 0
    location = [0,0]
    for i in range (0,a-n1,stepsize):
        for j in range (0,b-t,stepsize):
            cr = source[i:(i+n1),j:(j+t)]
            avgcr = np.mean(cr)
            varcr = np.var(cr)
            co = 1/(n1*t*vart*varcr)
            summ = 0
            for m in range(0,n1):
                for n in range(0,t):
                    summ += (cr[m][n]-avgcr)*(temp[m][n]-avgt)                    
            if summ*co>ncc:
                ncc = summ*co
                location[0] = j
                location[1] = i
    return(location)

source = cv2.imread('/Users/chai/Desktop/exercise5/source_img.jpg',0)
temp = cv2.imread('/Users/chai/Desktop/exercise5/template_img.jpg',0)
location = TemplateMatching(source,temp,10)
print(location)
match_img = cv2.cvtColor(source, cv2.COLOR_GRAY2RGB)


th = temp.shape[0]
tw = temp.shape[1]
r=(0,0,255)
cv2.line(match_img,(location[0],location[1]),(location[0],location[1]+n1),r,thickness=5)
cv2.line(match_img,(location[0],location[1]),(location[0]+t,location[1]),r,thickness=5)
cv2.line(match_img,(location[0]+t,location[1]),(location[0]+t,location[1]+n1),r,thickness=5)
cv2.line(match_img,(location[0],location[1]+th),(location[0]+t,location[1]+n1),r,thickness=5)
cv2.imwrite("/Users/chai/Desktop/exercise5/result.jpg",match_img)


cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
cv2.namedWindow('Mlocation[1]TemplateMatching', cv2.WINDOW_NORMAL)
cv2.imshow('TemplateImage', temp)
cv2.imshow('Mlocation[1]TemplateMatching', match_img)
cv2.waitKelocation[1](0)
cv2.destroyAllWindows()
