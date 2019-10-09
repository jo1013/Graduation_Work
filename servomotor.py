import time
from subprocess import call
import sys

DELAY = 1

#pan: 좌,우
#tilt: 상, 하
# 서보모터 위치 제한
pan_min = 50
pan_max = 250
tilt_min = 150
tilt_max = 250

# 서보모터 위치 초기값
pan_pos = 150;
tilt_pos = 150;

speed = 1


# 서보모터를 움직이는 함수 - 서보블라스터 명령
# 터미널 명령을 실행(아래 함수들을 실행하면 이 부분을 거쳐 최종 실행)
def pwm(pin, angle):
    print("servo[" + str(pin) + "] [" + str(angle) + "]")
    cmd = "echo " + str(pin) + "=" + str(angle) + "> /dev/servoblaster"
    call(cmd, shell=True)


#pan(left, right)
def rightpan():
    global pan_pos
    pan_pos -= 25
    if (pan_pos <= pan_min):
        pan_pos = pan_min
    pwm(1, pan_pos)

def leftpan():
    global pan_pos
    pan_pos += 25
    if (pan_pos >= pan_max):
        pan_pos = pan_max
    pwm(1, pan_pos)


#tilt(up, down)
def downtilt():
    global tilt_pos
    tilt_pos -= 10
    if (tilt_pos <= tilt_min):
        tilt_pos = tilt_min
    pwm(2, tilt_pos)

def uptilt():
    global tilt_pos
    tilt_pos += 10
    if (tilt_pos >= tilt_max):
        tilt_pos = tilt_max
    pwm(2, tilt_pos)


#servoblaster start
def servostart():
    call("sudo /etc/init.d/servoblaster start", shell=True)
    pwm(1, pan_pos)
    pwm(2, tilt_pos)
    # webiopi.debug("ON")


#servoblaster stop
# 사용하지 않을 때는 모터동작모듈을 중지시킨다.
# 24시칸 켜 놓겠다면 필요없는 기능
def servostop():
    pwm(1, 150)
    pwm(2, 150)
    time.sleep(1)
    call("sudo /etc/init.d/servoblaster stop", shell=True)
    # webiopi.debug("Off")

