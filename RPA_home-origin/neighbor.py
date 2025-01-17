from selenium import webdriver                                      # 동적 사이트 수집
from selenium.webdriver.chrome.service import Service               # 자동적 접근
from selenium.webdriver.chrome.options import Options               # 크롭 드라이버 옵션 지정
from selenium.webdriver.common.keys import Keys                     # actions key 사용
from selenium.webdriver.common.by import By                         # find_element 함수 사용을 위해
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime,timedelta

import time
import pyperclip
import pyautogui

chrome_options=Options()
chrome_service=Service()
chrome_options.add_experimental_option("detach", True)                              # 브라우저 꺼짐 방지 옵션(driver위에 위치해야 한다.)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])       # 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])    # 자동화 메시지 끄기
prefs = {
    "credentials_enable_service": False,                                                        # 비밀번호 자동저장 알럿 닫기
    "profile.password_manager_enabled": False,                                                  # 비밀번호 자동저장 알럿 닫기
}
chrome_options.add_experimental_option("prefs", prefs)                                    # 위에 prefs 설정

driver = webdriver.Chrome(service=chrome_service,options=chrome_options)                        # 크롬 드라이버 실행(설치불필요 ver.4 이상)

# 이웃 추가 클래스
class neighbor():
    # 로그인 함수
    def login(self):
        driver.implicitly_wait(30)                                              # 웹페이지 로딩 될때까지 5초 wait
        driver.maximize_window()                                                # 화면 최대화
        url = "https://www.naver.com/"                                          # 네이버 접속
        driver.get(url)

        login_button_xpath = '//*[@id="account"]//*[contains(@class,MyView-module__link_login___HpHMW)]'
        login_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,login_button_xpath))
        )
        actions = ActionChains(driver)
        actions.move_to_element(login_button).click().perform()
        print("네이버 홈페이지에서 로그인 버튼 클릭 PASS")
        login_info = {
                    "id" :'//*[@id="id"]',
                    "password" : '//*[@id="pw"]',
                    "login"  : '//*[@id="log.login"]'
                }
        user_id = "lksday62"
        user_pw = "@navks9562"
        for login_key, login_value in login_info.items():
            if login_key == "login":
                path = driver.find_element(By.XPATH, login_value)
                actions.move_to_element(path).click().perform()
                time.sleep(1)
                print("로그인 버튼 클릭 PASS")
            else :
                path = driver.find_element(By.XPATH, login_value)
                actions.move_to_element(path).click().perform()
                if login_key == "id":
                    pyperclip.copy(user_id)
                    path.send_keys(Keys.CONTROL,'v')
                    time.sleep(1)
                else :
                    pyperclip.copy(user_pw)
                    path.send_keys(Keys.CONTROL,'v')
                    time.sleep(1)
                print(f'{login_key} 입력 PASS')
        # not_ask_again = driver.find_element(By.ID,"wait")           # 이 브라우저에서 2단계인증 넘어가기 체크
        # actions.move_to_element(not_ask_again).click().perform()
        try :
            otp_btn = driver.find_element(By.ID,'useotpBtn')
            actions.move_to_element(otp_btn).click().perform()
            print("OTP 사용버튼 클릭 PASS")
        except:
            print("OTP 사용버튼 클릭 실패 ERROR")

        OTP = input("OTP 인증번호 입력: ")

        otp_input_box = driver.find_element(By.ID,"otp")
        actions.move_to_element(otp_input_box).click().perform()
        actions.send_keys(OTP)

        confirm = driver.find_element(By.ID,"confirm")
        actions.move_to_element(confirm).click().perform()

        print("로그인 완료 PASS")

# =================== 클래스 및 함수 ==========================
nb = neighbor()
nb.login()

# driver.quit()