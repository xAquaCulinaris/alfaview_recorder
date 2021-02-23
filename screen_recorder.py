from mss.linux import MSS as mss
from PIL import Image
import cv2
import numpy as np
import time

output = "raw.avi"

def screen_recorder(duration, end_time, top,left, width, height):
    print("Starting recording")
    monitor = {"top": top, "left": left, "width": width, "height": height}
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output, codec, duration, (width, height))
    with mss() as sct:
        frames = 0
        while time.perf_counter() < end_time:
            sct_img = sct.grab(monitor)
            img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
            image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

            out.write(image)
            frames += 1

    out.release()
    cv2.destroyAllWindows()
    print("Finished recording")
    return frames
