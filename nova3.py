import cv2
import numpy as np
from config import conf
import time
import datetime

def load_to_hsv(filename, interpolation_method):
    im = cv2.imread(conf.sample_folder + filename)
    img = cv2.resize(im,None,fx=0.5,fy=0.5, interpolation = interpolation_method)
    out = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return out

def extract_points(img, hue_tresh, saturaion_tresh):
    return np.logical_and(img[...,0] > hue_tresh, img[...,1] < saturaion_tresh )

if __name__ == '__main__':

    for i in range (60,73):
        name = '0{}.jpg'.format(i)
        print(name)
        out = load_to_hsv(name, cv2.INTER_AREA)

        extracted = extract_points(out, 100, 32)

        timestamp = time.strftime(conf.time_format, time.gmtime())

        if conf.save_data:
            cv2.imwrite(conf.detected_image_folder + name , 255 * (extracted.astype('uint8')))

##        cv2.imshow ("Tresholded", 255* extracted.astype('uint8'))       
##        cv2.waitKey(0)
##        cv2.destroyAllWindows()
