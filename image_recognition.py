import cv2
import numpy as np


def find_button(screenshot, button_to_find, output_name):
    h,w = open_button.shape[:-1]

    res = cv2.matchTemplate(screenshot, button_to_find, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res>= threshold)
    for pt in zip(*loc[::-1]):
        print(output_name + ":")
        print("x: " + str(pt[0]+w/2))
        print("y: " + str(pt[1]+h/2))
        print()

        cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    #remove later only need coordinates
    cv2.imwrite(output_name, screenshot)


screenshot1 = cv2.imread('buttons_to_find/screenshot1.png')
screenshot2 = cv2.imread('buttons_to_find/screenshot2.png')
screenshot3 = cv2.imread('buttons_to_find/screenshot3.png')


open_button = cv2.imread('buttons_to_find/open_button.png')
skip_update_button = cv2.imread('buttons_to_find/skip_update_button.png')
join_rooom_button = cv2.imread('buttons_to_find/join_room_button.png')

find_button(screenshot1, open_button, 'result1.png')
find_button(screenshot2, skip_update_button, 'result2.png')
find_button(screenshot3, join_rooom_button, 'result3.png')
