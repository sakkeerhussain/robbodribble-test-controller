import requests
import time

BASE_URL = 'http://10.7.120.81/controller/'
BASE_URL = 'http://10.7.90.30/controller/'


def move_forward():
    print ("\n\nMoving forward")
    resp = requests.get(BASE_URL + 'drive/front/?value=100&sequence_no=1')
    print resp.content


def move_backward():
    print ("\n\nMoving backward")
    resp = requests.get(BASE_URL + 'drive/back/?value=100&sequence_no=1')
    print resp.content


def door_open():
    print ("\n\nDoor opening")
    resp = requests.get(BASE_URL + 'door/open/?sequence_no=1')
    print resp.content


def door_close():
    print ("\n\nDoor closing")
    resp = requests.get(BASE_URL + 'door/close/?sequence_no=1')
    print resp.content


if __name__ == "__main__":
    while True:
        move_backward()
        time.sleep(1)
        door_open()
        time.sleep(8)
        door_close()
        time.sleep(1)
        move_forward()
        time.sleep(3)
