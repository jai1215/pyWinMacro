import numpy as np
import cv2
import time
import os

from utils.grabscreen import grab_screen
from utils.getkeys import key_check

count = 0

while True:
    keys = key_check()
    print("waiting press B to start")
    if keys == "B":
        print("Starting")
        break
    
while True:
    count +=1
    image = grab_screen(region=(50, 100, 799+500, 499+500))
    cv2.imshow(f"Test Image ", image)
    cv2.waitKey(1)
    keys = key_check()
    # targets.append(keys)h
    if keys == "H":
        break