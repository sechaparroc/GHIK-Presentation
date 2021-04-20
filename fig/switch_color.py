#simple script to change - binary color images
import cv2 as cv
import numpy as np
src = 'unal'
suffix = '_gr'
#load image
image = cv.imread(src + '.png', cv.IMREAD_UNCHANGED)
#keep alpha untouched
bgr = image[:,:,:3] # Channels 0..2
#convert to HSV
hsv=cv.cvtColor(bgr,cv.COLOR_BGR2HSV)
#Define bounds
brown_lo=np.array([0,0,0])
brown_hi=np.array([255,255,10])
# Mask image to only select browns
mask=cv.inRange(hsv,brown_lo,brown_hi)
# Change image where we found brown
bgr[mask>0]=(107,198,175)

#stack alpha
alpha = image[:,:,3] # Channel 3
result = np.dstack([bgr, alpha]) # Add the alpha channel
cv.imwrite(src + suffix + ".png", result)



