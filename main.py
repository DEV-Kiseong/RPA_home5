print("Hi Selenium \n"
      "Let's start RPA test")

import time


from selenium import webdriver # 동적 사이트 수집
from webdriver_manager.chrome import ChromeDriverManager          # 크롬 드라이버 설치(자동 업데이트)
from selenium.webdriver.chrome.service import Service             # 자동적 접근
from selenium.webdriver.chrome.options import Options             # 크롭 드라이버 옵션 지정
from selenium.webdriver.common.by import By                       # find_element 함수 쉽게 쓰기 위함
from selenium.webdriver.common.keys import Keys

chrome_options=Options()
chrome_service=Service()
chrome_options.add_experimental_option("detach", True)                        # 브라우저 꺼짐 방지 옵션(driver위에 위치해야 한다.)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 불필요한 에러 메세지 없애기

driver = webdriver.Chrome(service=chrome_service,options=chrome_options)      # 크롬 드라이버 실행(설치불필요 ver.4 이상)

driver.implicitly_wait(5)                                                     # 웹페이지 로딩 될때까지 5초 wait
driver.maximize_window()                                                      # 화면 최대화

url = "https://portal.daou.co.kr/"
driver.get(url)                                                               # 다우포탈 접속

myID = "kslee"
myPW = "@Lks622103"

userID = driver.find_element("xpath",'//*[@id="username"]')       # userID 변수 만들기
userID.click()                                                    # 아이디 창 클릭
userID.send_keys(myID)                                            # 아이디 입력키 보내기 ("본인 아이디")

userPW = driver.find_element("xpath",'//*[@id="password"]')       # 비밀번호 태그를 userPW 라는 변수에 넣기
userPW.click()                                                    # 비밀번호 창 클릭
userPW.send_keys(myPW)                                            # 비밀번호 입력키 보내기 ("본인 비번")

login_btn = driver.find_element("xpath",'//*[@id="login_submit"]')      # 로그인 버튼을 login_btn 변수에 넣기
login_btn.click()                                                       # 로그인 버튼 클릭