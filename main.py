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
login_btn.click()
print("로그인 완료")

mail_menu = driver.find_element(By.XPATH,'//*[@id="menu-container"]/ul/div[1]/div[2]/div/div/div/li[2]/a/span[1]/span')
mail_menu.click()
time.sleep(2)
print("메일 메뉴 진입")

iframe = driver.find_element(By.XPATH,'//*[@id="mail-viewer"]')
driver.switch_to.frame(iframe)
print("iframe 진입")
mail_write = driver.find_element(By.XPATH,'//*[@id="mailLeftMenuWrap"]/section[2]/a')
mail_write.click()
time.sleep(2)
print("iframe 진입 후, 메일쓰기 버튼 클릭")

# 메일정보 입력
receive_mail_address = "haggis@daou.co.kr"                        # 받는사람 메일주소 입력
cc_mail_address = "soominoh95@daou.co.kr"                         # cc메일주소 입력
title_input = "자동화테스트 메일 입니다 by 이기성"                     # 제목 입력 내용
mail_contents = ("안녕하세요\n"
                 "품질관리팀의 이기성입니다.\n"
                 "자동화테스트 실습 메일보내기를 하고 있습니다.\n"
                 "감사합니다.\n")

receiver = driver.find_element(By.XPATH,'//*[@id="to"]')                       #받는사람
time.sleep(1)
receiver.click()
receiver.send_keys(receive_mail_address)
receiver.send_keys(Keys.ENTER)                                                      #받는사람 메일주소로 인해 아래 CC입력란이 가릴때, 엔터를 쳐준다
print("받는사람 입력완료")

cc = driver.find_element(By.XPATH,'//*[@id="cc"]')                           #CC,참조
time.sleep(1)
cc.click()
cc.send_keys(cc_mail_address)
print("CC 입력완료")

title = driver.find_element(By.ID, "subject")                                 # 제목
time.sleep(1)
title.click()
title.send_keys(title_input)
print("메일제목 입력완료")

iframe_editor = driver.find_element(By.XPATH,'//*[@id="dext_frame_smartEditor"]')
driver.switch_to.frame(iframe_editor)
print("2nd iframe access")

iframe_contents = driver.find_element(By.XPATH,'//*[@id="dext5_design_smartEditor"]')
driver.switch_to.frame(iframe_contents)
print("3rd iframe access")
text_body = driver.find_element(By.XPATH,'//*[@id="dext_body"]')
text_body.click()
text_body.send_keys(mail_contents)
print("메일 내용 입력완료")

driver.switch_to.parent_frame()
print("텍스트박스 iframe 에서 빠져나옴")

driver.switch_to.default_content()                                # 1st iframe 바깥으로 빠져나옴                                              # 로그인 버튼 클릭