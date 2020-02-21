# Convert images grabbed from twitter to video
# Using cv2 from opencv to create video
import os
import cv2
import numpy as np

path = 'tweets/'
filelist = os.listdir(path)

fps = 1/3 
size = (600, 200) 

output_file = 'tweets.avi'

video = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'MPEG'), fps, size)

for item in filelist:
    if item.endswith('.png'): 
        item = path + item
        img = cv2.imread(item)
        video.write(img)

cv2.destroyAllWindows()
video.release()

