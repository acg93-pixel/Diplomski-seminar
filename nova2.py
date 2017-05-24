import cv2
import numpy as np
import time
import datetime
from config import conf
import os

im = cv2.imread(conf.sample_folder + 'slika1.png')
img = cv2.resize(im,None,fx=0.5,fy=0.5, interpolation = cv2.INTER_AREA)
imgR = img[:,:,0]
imgG = img[:,:,1]
imgB = img[:,:,2]
imR = cv2.equalizeHist(imgR)
imG = cv2.equalizeHist(imgG)
imB = cv2.equalizeHist(imgB)
im = np.dstack((imR, imG, imB))
#unsharp masking
gaussian_3 = cv2.GaussianBlur(im, (9, 9), 10.0)
ui = cv2.addWeighted(im, 1.5, gaussian_3, -0.5, 0, im)

imR = ui[:,:,2]



laplacian = cv2.Laplacian(imR,cv2.CV_64F)


cv2.imshow("Keypoints", laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()

