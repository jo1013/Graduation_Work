import os
import sys
from subprocess import call

def ossys():
    #os.system('lxterminal ')
    os.system('killall -9 mjpg_streamer')
    os.system('mjpg_streamer -i "input_uvc.so -vf flase" -o "output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www/"')
    return 


def streaming():
    call('killall -9 mjpg_streamer', shell=True)
    call('mjpg_streamer -i "input_uvc.so -vf flase" -o "output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www/"', shell=True)
    return 
