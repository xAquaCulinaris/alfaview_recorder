import cv2
import numpy as np


def find_button(screenshot, button_to_find, output_name):
    print('Searching for button..')
    h,w = button_to_find.shape[:-1]

    res = cv2.matchTemplate(screenshot, button_to_find, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res>= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    print('Found button..')
    return (pt[0]+w/2, pt[1]+h/2)
