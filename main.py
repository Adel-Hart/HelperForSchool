# -*- coding: utf-8 -*- 

from selenium import webdriver
from openpyxl import Workbook
import os
import chromedriver_autoinstaller
gyung = os.getcwd()
gyung1 = gyung.replace("dist", "")
import keyboard
import random
import codecs
import csv
import time
import sys
sys.path.append(gyung1+"\\file")
import zagazindan
import mommyson
import chulsuk
import leadergy

while True:
    os.system('cls')
    print("학생들과 선생님들을 위한 종합선물세트!\n\n1.출석체크\n2.출석체크확인\n3.자가진단 자동\n4.급식이뭐야?\n5.끄기\n\n모든거 다 내가 만들었으니 의심 ㄴㄴ")
    ann = input(" :")
    if ann == "1":
        chulsuk.cs()
    if ann == "2":
        leadergy.lg()
    if ann == "3":
        zagazindan.zaga()
    if ann == "4":
        mommyson.bab()
    if ann == "5":
        break
