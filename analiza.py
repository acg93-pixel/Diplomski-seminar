import numpy as np
import cv2
from config import conf
import os

img = cv2.imread(conf.detected_image_folder + "062.jpg", 0)
boolmat = img > 0 

detected = np.sum(boolmat)
imsz = img.size

print ((detected/imsz)*100)

