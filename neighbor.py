from selenium import webdriver # 동적 사이트 수집
from selenium.webdriver.chrome.service import Service             # 자동적 접근
from selenium.webdriver.chrome.options import Options             # 크롭 드라이버 옵션 지정
from selenium.webdriver.common.by import By                       # find_element 함수 사용을 위해
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime,timedelta

import time
import logging
chrome_options=Options()
chrome_service=Service()
chrome_options.add_experimental_option("detach", True)                        # 브라우저 꺼짐 방지 옵션(driver위에 위치해야 한다.)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])    # 자동화 메시지 끄기

driver = webdriver.Chrome(service=chrome_service,options=chrome_options)      # 크롬 드라이버 실행(설치불필요 ver.4 이상)
                                                             # 네이버 접속

# 세팅 클래스
class setting_up():
    # 스크린샷 세팅 함수
    def screenshot_method(self, external_call=False):
        screenshot_path = 'C:\\Users\\Daou\\PycharmProjects\\screenshot\\screenshot' + datetime.today().strftime("%Y%m%d_%H%M%S") + '.png'
        driver.save_screenshot(screenshot_path)
        try:
            if external_call == False:
                self.logger.info("특이사항 발생 시 스크린샷 촬영 및 저장합니다.")
            else:
                self.logger.error("!!!!! 특이사항 감지하여 스크린샷 촬영 및 저장")
        except Exception as e:
            self.logger.error(f'스크린샷 저장실패: {e}')

    # 로그 세팅 함수
    def logging_method(self):
        self.logger = logging.getLogger("add_neighbor")
        self.logger.setLevel(level=logging.DEBUG)  # Output level //DEBUG, INFO, WARNING, ERROR, CRITICAL
        self.user_id = "userID"

        formatter = logging.Formatter("[%(asctime)s] %(levelname)s %(name)s " + self.user_id + "[%(thread)d] [%(funcName)s : line %(lineno)d] - %(message)s")
        # 콘솔 출력
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)  # 콘솔에만 DEBUG 이상 로그 표시
        stream_handler.setFormatter(formatter)

        # 파일에 출력
        self.logfile = r'D:\파이썬\RPA_home\log\log' + datetime.today().strftime("%Y%m%d_%H%M%S") + '.log'  # 로그파일 주소
        file_handler = logging.FileHandler(self.logfile, 'w', encoding="UTF-8")
        file_handler.setLevel(logging.INFO)  # 파일에만  INFO 이상 로그 표시
        file_handler.setFormatter(formatter)

        # 중복 핸들러 추가 방지
        if self.logger.hasHandlers():
            self.logger.handlers.clear()
        # 핸들러 추가
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)
        self.logger.info("*************** 자동화(RPA) 로그 시 작 ***************")  # 첫번째 로그 메시지
# 이웃 추가 클래스
class neighbor():
    # 로그인 함수
    def login(self):
        driver.implicitly_wait(30)  # 웹페이지 로딩 될때까지 5초 wait
        driver.maximize_window()  # 화면 최대화
        url = "https://www.naver.com/"
        driver.get(url)

        login_button_xpath = '//*[@id="account"]//*[contains(@class,MyView-module__link_login___HpHMW)]'
        login_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,login_button_xpath))
        )
        actions = ActionChains(driver)
        actions.move_to_element(login_button).click().perform()
        sup.logger.info("네이버 홈페이지에서 로그인 버튼 클릭 PASS")
        login_info = {
                    "id" :'//*[@id="id"]',
                    "password" : '//*[@id="pw"]',
                    "login"  : '//*[@id="log.login"]'
                }
        user_id = "lksday62"
        user_pw = "@navks9562"
        for login_key, login_value in login_info.items():
            if login_key == "id":
                path = driver.find_element(By.XPATH, login_value)
                actions.move_to_element(path).click().perform()
                actions.send_keys(user_id).perform()
                time.sleep(1)
                sup.logger.info(f'{login_key}입력 PASS')
            elif login_key == "password" :
                path = driver.find_element(By.XPATH, login_value)
                actions.move_to_element(path).click().perform()
                actions.send_keys(user_pw).perform()
                sup.logger.info(f'{login_key} 입력 PASS')
            elif login_key == "login":
                path = driver.find_element(By.XPATH, login_value)
                actions.move_to_element(path).click().perform()
                time.sleep(1)
                sup.logger.info("로그인 버튼 클릭 PASS")
        sup.logger.info("로그인 완료 PASS")

# =================== 클래스 및 함수 ==========================
sup = setting_up()
sup.logging_method()
sup.screenshot_method()

nb = neighbor()
nb.login()

# driver.quit()