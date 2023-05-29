# -*- coding: utf-8 -*- 
import time
import sys
import os
from selenium import webdriver
import chromedriver_autoinstaller
import keyboard
def bab():
    dir = os.getcwd().replace("\\", "/").replace("/file", "")
    tm = time.localtime().tm_wday
    print(tm)
    if tm == 0: #월
        ys = 1
        now = 2
        tmor = 3
    elif tm == 1: #화
        ys = 2
        now = 3
        tmor = 4
    elif tm == 2: #수
        ys = 3
        now = 4
        tmor = 5
    elif tm == 3: #목
        ys = 4
        now = 5
        tmor = 6
    elif tm == 4: #금
        ys = 5
        now = 6
        tmor = 7
    elif tm == 5: #토
        ys = 6
        now = 7
        tmor = 1
    elif tm == 6: #일
        ys = 7
        now = 1
        tmor = 2
    ys = str(ys)
    now = str(now)
    tmor = str(tmor)
    
    school = input("school :")
    print("너무 안된다고 생각할땐 아무키(스패이스바 추천)을 눌러보세요!")
    options = webdriver.ChromeOptions() # 크롬 옵션
    options.add_argument('headless') # headless
    options.add_argument("window-size=1920x1080") # 화면크기
    options.add_argument("disable-gpu")#gpu사용 해제 여기서는 안쓸거임
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
 
    driver = webdriver.Chrome(dir+"/module/chromedriver.exe", chrome_options=options)
    driver.get('https://www.foodsafetykorea.go.kr/portal/sensuousmenu/schoolMeals.do')
    driver.find_element_by_xpath('/html/body/div[2]/form/div[1]/main/section/div[2]/div[1]/fieldset/ul/li[2]/div/div/span').click()
    driver.find_element_by_xpath('/html/body/div[2]/form/div[1]/main/section/div[2]/div[1]/fieldset/ul/li[2]/div/div/div/span[5]').click()
    driver.find_element_by_xpath('/html/body/div[2]/form/div[1]/main/section/div[2]/div[1]/fieldset/ul/li[3]/input').send_keys(school)
    driver.find_element_by_xpath('/html/body/div[2]/form/div[1]/main/section/div[2]/div[1]/fieldset/ul/li[4]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/form/div[1]/main/section/div[2]/table/tbody/tr/td[4]/a[1]').click()
    time.sleep(2)
    try:
        y = driver.find_element_by_xpath('//*[@id="tab1"]/table/tbody/tr['+ys+']/td[2]').text
    except:
        y = "안먹어요"
    try:
        n = driver.find_element_by_xpath('//*[@id="tab1"]/table/tbody/tr['+now+']/td[2]').text
    except:
        n = "안먹어요"
    try:
        t = driver.find_element_by_xpath('//*[@id="tab1"]/table/tbody/tr['+tmor+']/td[2]').text
    except:
        t = "안먹어요"
    driver.close()
    os.system('cls')
    print("어제급식 :"+y+"\n\n오늘급식:"+n+"\n\n내일급식:"+t)
    print("\nesc를 누르면 나감")
    while True:
        if keyboard.is_pressed('esc'):
            print("나갑니다")
            break