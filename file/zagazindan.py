# -*- coding: utf-8 -*- 
from selenium import webdriver
import chromedriver_autoinstaller
import keyboard
import random 
import os
import time
import codecs

def zaga():
    gyung = os.getcwd()
    gyung1 = gyung.replace("\\", "/").replace("/file", "")
    print(gyung1)

    if os.path.isfile(gyung1+'/data/profile.dat'):
            with open(gyung1+'/data/profile.dat', encoding = 'utf-8') as data_file:
                ds = data_file.readline().strip()
                dn = data_file.readline().strip()
                dbt = data_file.readline().strip()
                dp = data_file.readline().strip()

                print(ds,dn,dbt,dp)

    else:
        print("학교이름 :")
        school = input(" :")
        print("이름")
        name = input(" :")
        print("생일")
        bth = input(" :")
        print("비밀번호")
        pw = input(" :")

        print("설정을 저장하시겠습니까 (설정안하고 바로 가능 이거보셈 readme.txt)[y/n]")
        ss = input(" :")

        if ss == "y":
            if os.path.isfile(gyung1+'/data/profile.dat'):
                print("파일을 저장?[y/n]")
                ss_2 = input(str(" :"))

                if ss_2 == "y":
                    a = open(gyung1+'/data/profile.dat', 'w', encoding = 'utf-8')
                    a.close()
                    with open(gyung1+'/data/profile.dat', 'a', encoding = 'utf-8') as fen:
                        ago = school + '\n' + name + '\n' + bth + '\n' + pw + '\n'
                        ago.replace()
                        print(ago)
                        fen.write(ago)
                    print("save")

                else:
                    print()

            else:
                a = open(gyung1+'/data/profile.dat', 'w', encoding = 'utf-8')
                a.close()
                with open(gyung1+'/data/profile.dat', 'a', encoding = 'utf-8') as fen:
                    ago = school + '\n' + name + '\n' + bth + '\n' + pw + '\n'
                    ago.replace(" ","")
                    print(ago)
                    fen.write(ago)
                print("save")
        ds = school
        dn = name
        dbt = bth
        dp = pw
        #접속시작
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(gyung1+"/module/chromedriver.exe", chrome_options=options)
    url = 'https://hcs.eduro.go.kr/'
    driver.get(url)
    driver.implicitly_wait(3)

    rtime = random.uniform(0.1, 3.2)
    driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div/button').click()
    time.sleep(rtime)
    driver.find_element_by_css_selector('#WriteInfoForm > table > tbody > tr:nth-child(1) > td > button').send_keys('\n')
    time.sleep(rtime)
    driver.find_element_by_css_selector(
        "#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > table > tbody > tr:nth-child(1) > td > select > option:nth-child(6)"
    ).click()
    time.sleep(rtime)
    driver.find_element_by_css_selector(
        '#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > table > tbody > tr:nth-child(2) > td > select > option:nth-child(4)').click()
    driver.find_element_by_css_selector('#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > table > tbody > tr:nth-child(3) > td:nth-child(2) > input').send_keys(ds)
    driver.find_element_by_css_selector(
        '#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > table > tbody > tr:nth-child(3) > td:nth-child(3) > button').click()
    driver.find_element_by_css_selector('#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > ul > li > p > a').click()
    time.sleep(rtime)
    driver.find_element_by_css_selector('#softBoardListLayer > div.layerContentsWrap > div.layerBtnWrap > input').click()
    time.sleep(rtime)
    driver.find_element_by_css_selector('#WriteInfoForm > table > tbody > tr:nth-child(2) > td > input').send_keys(dn)
    time.sleep(rtime)
    driver.find_element_by_css_selector('#WriteInfoForm > table > tbody > tr:nth-child(3) > td > input').send_keys(dbt)
    time.sleep(rtime)
    driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div/div/input').click()
    time.sleep(rtime)
    driver.find_element_by_css_selector('#WriteInfoForm > table > tbody > tr > td > input').send_keys(dp)
    time.sleep(rtime)
    driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div/div/input').click()
    time.sleep(rtime)
    driver.find_element_by_css_selector('#container > div > section.memberWrap > div:nth-child(2) > ul > li > a > span.name').click()
    time.sleep(rtime)
    driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div/div[2]/div[2]/dl[1]/dd/ul/li[1]/label').click()
    time.sleep(rtime)
    driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div/div[2]/div[2]/dl[2]/dd/ul/li[1]/label').click()
    time.sleep(rtime)
    driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div/div[2]/div[2]/dl[3]/dd/ul/li[1]/label').click()
    time.sleep(rtime)
    driver.find_element_by_css_selector('#btnConfirm').click()
    time.sleep(3)
    print("done... -esc누르면 나감")
    while True:
        if keyboard.is_pressed('esc'):
            print("나갑니다")
            break