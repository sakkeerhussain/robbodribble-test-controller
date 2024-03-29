import time

import requests

RIGHT_CONST = 3.0
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
    for i in range(1, value/30):
        move_forward(30)
        turn_right(RIGHT_CONST)

TRUN_NIENTY = 65
value = 120
if __name__ == "__main__":

    while True:
        door_close()
        time.sleep(1)
        front_motion(300)
        time.sleep(1)
        move_backward(260)
        time.sleep(1)
        door_open()
        time.sleep(3)
