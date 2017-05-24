import cv2
import numpy as np
import time
import datetime
from config import conf
import os

img = cv2.imread(conf.sample_folder + 'slika2.png')
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# lower mask (0-10)
lower_red = np.array([30,150,50])
upper_red = np.array([255,255,180])
mask = cv2.inRange(img_hsv, lower_red, upper_red)




output_img = cv2.bitwise_and(img_hsv,img_hsv, mask= mask)

cv2.imshow("obradjena", output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
