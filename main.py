#!/usr/bin/python3
import threading
import time
import os
from screen_recorder import screen_recorder
from video_converter import convert_video
from audio_recorder import record_audio
from combine_files import combine_audio
from open_alfaview import open_browser
from close_alfaview import close_alfaview
from alfaview_location import get_alfaview_location
from config_parser import get_config_double

duration = get_config_double('DEFAULT', 'recording_duration')

def video_thread(window_dimensions):
    start_time = time.perf_counter()
    end_time = start_time + duration
    frames = screen_recorder(duration, end_time, window_dimensions[0], window_dimensions[1], window_dimensions[2]-2, window_dimensions[3]-2)


    sec = end_time-start_time
    multiplier = frames/sec


    convert_video(multiplier, window_dimensions[2]-2, window_dimensions[3]-2)


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
    #TODO: wait for alfaview to really open
    window_dimensions = get_alfaview_location()

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
