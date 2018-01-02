import time

import requests

RIGHT_CONST = 1
BASE_URL = 'http://10.7.120.81/controller/'
# BASE_URL = 'http://192.168.1.55/controller/'


def turn_right(value):
    print ("\n\nTurning right")
    resp = requests.get(BASE_URL + 'turn/right/?value='+str(value)+'&sequence_no=1')
    print resp.content


def turn_left(value):
    print ("\n\nTurning right")
    resp = requests.get(BASE_URL + 'turn/left/?value='+str(value)+'&sequence_no=1')
    print resp.content


def move_forward(value):
    print ("\n\nMoving forward")
    resp = requests.get(BASE_URL + 'drive/forward/?value='+str(value)+'&sequence_no=1')
    print resp.content


def move_backward(value):
    print ("\n\nMoving backward")
    resp = requests.get(BASE_URL + 'drive/backward/?value='+str(value)+'&sequence_no=1')
    print resp.content


def door_open():
    print ("\n\nDoor opening")
    resp = requests.get(BASE_URL + 'door/open/?sequence_no=1')
    print resp.content


def door_close():
    print ("\n\nDoor closing")
    resp = requests.get(BASE_URL + 'door/close/?sequence_no=1')
    print resp.content


def front_motion(value):
    for i in range(1, value/10):
        move_forward(10)
        turn_right(RIGHT_CONST)

TRUN_NIENTY = 65
value = 120
if __name__ == "__main__":

    while True:
        value +=25
        if (value > 240):
            value = 50
        door_close()
        time.sleep(0.5)
        front_motion(value)
        time.sleep(0.3)
        turn_left(TRUN_NIENTY)
        time.sleep(0.3)
        front_motion(180)
        time.sleep(0.3)
        turn_left(TRUN_NIENTY)
        time.sleep(0.3)
        front_motion(value)
        turn_left(TRUN_NIENTY)
        time.sleep(0.5)
        front_motion(80)
        time.sleep(0.3)
        turn_left(TRUN_NIENTY)
        time.sleep(0.3)
        move_backward(25)
        time.sleep(0.3)
        door_open()
        time.sleep(3)
