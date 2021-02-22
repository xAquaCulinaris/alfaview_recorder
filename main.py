#!/usr/bin/python3
import threading
import time
import os
from screenRecorder import capture_video
from screenRecorder import convert_video
from audio_recorder import record_audio
from combine_files import combine_audio
from open_alfaview import open_browser
from close_alfaview import close_alfaview
from alfaview_location import get_alfaview_location

duration = 10

def video_thread(window_dimensions):
    start_time = time.perf_counter()
    end_time = start_time + duration
    frames = capture_video(end_time, window_dimensions[0], window_dimensions[1], window_dimensions[2], window_dimensions[3])


    sec = end_time-start_time
    multiplier = frames/sec


    convert_video(multiplier, window_dimensions[2], window_dimensions[3])


def audio_thread():
    record_audio(duration)

def delete_files():
    to_delete = ['raw.avi', 'video.avi', 'screenshot1.png', 'screenshot2.png', 'screenshot3.png', 'output.wav']

    for file in to_delete:
        if os.path.exists(file):
            os.remove(file )
            print(file + ' has been removed')
        else:
            print(file + ' does not exists')


def main():
    open_browser()
    window_dimensions = get_alfaview_location()
    top = window_dimensions[0]
    left = window_dimensions[1]
    width = window_dimensions[2]
    height = window_dimensions[3]
    print("top" + str(top))
    print("left" + str(left))
    print("width" + str(width))
    print("heigth" + str(height))


    t1 = threading.Thread(target=video_thread, args=[window_dimensions])
    t2 = threading.Thread(target=audio_thread)
    t1.start()
    t2.start()

    t1.join()
    t2.join()



    combine_audio('video.avi', 'output.wav')
    delete_files()

    close_alfaview()



if __name__ == '__main__':
    main()
