# -*- coding: utf-8 -*- 
import os
import keyboard
def lg():
    path = os.getcwd().replace("\\", "/").replace("/file", "")

    print("---학생부 리더기---")
    with open(path+"/profile/profile.txt", 'r', encoding="utf-8-sig") as popo:
        su = int(popo.readline())
        with open(path+"/data/dummy.dat", 'r', encoding="utf-8-sig")as poo:
            su = str(su)
            print("========list========\n 총"+su+"명\n")
            su = int(su)
            for i in range(su):
                print(poo.readline())
            print("%esc를 누르면 나갑니다%")

    while True:
        if keyboard.is_pressed('esc'):
            print("bye")
            break