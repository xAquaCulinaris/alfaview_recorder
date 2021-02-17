import cv2
import numpy as np
import os
import pyautogui
import time




duration = 10
output = "raw.avi"
converted = "video.avi"

left = 1920
top = 1080
width = 1920
height = 1080


def capture_video(end_time):
    print("Starting capturing..")
    # Define the codec and create VideoWriter object
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output, codec, 10.0, (width, height))

    frames = 0
    while time.perf_counter() < end_time:
        img = pyautogui.screenshot(region=(left,top,width,height))
        image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(image)
        frames += 1

    out.release()
    cv2.destroyAllWindows()
    print("Finished capturing\n")
    return frames


def convert_video(multiplier):
    print("Starting conversion..")
    cap = cv2.VideoCapture(output)
    codec = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(converted, codec, multiplier, (width,height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("video ended")
            break
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Finished conversion..")




start_time = time.perf_counter()
end_time = start_time + duration
frames = capture_video(end_time)


sec = end_time-start_time
multiplier = frames/sec

print("sec " + str(sec))
print("multiplier " + str(multiplier))

convert_video(multiplier)
