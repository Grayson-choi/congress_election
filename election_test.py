from selenium import webdriver
import time
import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par
import os
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome("./chromedriver")
browser.get("http://info.nec.go.kr/main/showDocument.xhtml?electionId=0020200415&topMenuId=CP&secondMenuId=CPRI03")
time.sleep(4)



# candidate = input("궁금한 후보자를 입력하세요. >> ")
# 선거 사이트로 이동

#국회의원 선거 클릭
browser.find_element_by_css_selector("#electionId2").click()
time.sleep(2)

#도시 선택 cityCode
select_city = Select(browser.find_element_by_id('cityCode'))
city_list = browser.find_elements_by_css_selector("select#cityCode > option")
city_list = list(map(lambda x: x.text, city_list))
# city = input(""str(city_list[1:]))

#서울 특별시 선택
select_city.select_by_visible_text("서울특별시")
time.sleep(1)



# 선거구 선택 sggCityCode
select_sgg = Select(browser.find_element_by_id("sggCityCode"))
sgg_list = browser.find_elements_by_css_selector("select#sggCityCode > option")
sgg_list = list(map(lambda x: x.text, sgg_list))

time.sleep(1)

select_sgg.select_by_visible_text("종로구")
time.sleep(1)


# 조회 버튼 선택 (홈페이지에서 img 타입의 버튼이 하나라서 이렇게 씀)
browser.find_element_by_css_selector("#spanSubmit").click()
#
# time.sleep(5)
# browser.quit()

# cityCode