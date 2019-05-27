import numpy as np
from PIL import ImageGrab
import cv2

while (True):
    image = ImageGrab.grab(bbox=(60, 40, 800, 630))
    image = np.array(image)
    cv2.imshow('window', cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

