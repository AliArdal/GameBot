import time
from datetime import datetime, timedelta
import keyboard


def skill1():
    keyboard.press('1')
    time.sleep(0.005)
    keyboard.release('1')
    time.sleep(0.01)

def skill2():
    keyboard.press('2')
    time.sleep(0.01)
    keyboard.release('2')
    time.sleep(0.2)

def skill4():
    keyboard.press('4')
    time.sleep(0.01)
    keyboard.release('4')
    time.sleep(0.2)

def mob_sec():
    keyboard.press('Z')
    time.sleep(0.1)
    keyboard.release('Z')
    time.sleep(0.1)

time.sleep(3)
skill_2_suresi = 120
skill_2_kullanim_zamani = datetime.now()

counter = 0
while True:
    mob_sec()
    time.sleep(0.1)
    skill1()
    time.sleep(0.01)

    counter += 1
    if counter % 35 == 0:
        skill4()

    if datetime.now() >= skill_2_kullanim_zamani:
        skill2()
    if datetime.now() >= skill_2_kullanim_zamani:
        skill2()
        skill_2_kullanim_zamani = datetime.now() + timedelta(seconds=skill_2_suresi)