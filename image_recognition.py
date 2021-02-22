import cv2
import numpy as np
import pyautogui

def find_button(screenshot, button_to_find):
    print('Searching for button..')
    h,w = button_to_find.shape[:-1]

    res = cv2.matchTemplate(screenshot, button_to_find, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print('Found button..')

    return (max_loc[0]+w/2, max_loc[1]+h/2)
