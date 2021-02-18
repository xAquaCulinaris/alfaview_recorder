#!/usr/bin/python3
import threading
import time
import os
from screenRecorder import capture_video
from screenRecorder import convert_video
from audio_recorder import record_audio
from combine_files import combine_audio
from open_alfaview import open_browser
from open_alfaview import close_alfaview

duration = 10

def video_thread():
    start_time = time.perf_counter()
    end_time = start_time + duration
    frames = capture_video(end_time)


    sec = end_time-start_time
    multiplier = frames/sec


    convert_video(multiplier)


def audio_thread():
    record_audio(duration)

def delete_files():
    to_delete = ['raw.avi', 'video.avi', 'output.wav', 'screenshot1.png', 'screenshot2.png', 'screenshot3.png']

    for file in to_delete:
        if os.path.exists(file):
            os.remove(file )
            print(file + ' has been removed')
        else:
            print(file + ' does not exists')


def main():
    open_browser()

    t1 = threading.Thread(target=video_thread)
    t2 = threading.Thread(target=audio_thread)
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    combine_audio('video.avi', 'output.wav', 'video.mp4')
    delete_files()

    close_alfaview()



if __name__ == '__main__':
    main()
