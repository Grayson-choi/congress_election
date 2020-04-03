from selenium import webdriver
import time
import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par
import os
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome("./chromedriver")
# 윈도우는 아래 코드를 실행
# browser = webdriver.Chrome("./chromedriver.exe")

# 선거구 및 읍면동현황 이
browser.get("http://info.nec.go.kr/main/showDocument.xhtml?electionId=0020200415&topMenuId=BI&secondMenuId=BIGI05")
time.sleep(4)

#국회의원 선거 클릭
browser.find_element_by_css_selector("#electionId2").click()
time.sleep(2)

#도시 선택 cityCode
select_city = Select(browser.find_element_by_id('cityCode'))
city_list = browser.find_elements_by_css_selector("select#cityCode > option")
city_list = list(map(lambda x: x.text, city_list))
print(city_list[1:])


#서울 특별시 선택
select_city.select_by_visible_text("서울특별시")
time.sleep(1)

# 조회 버튼 선택 (홈페이지에서 img 타입의 버튼이 하나라서 이렇게 씀)
browser.find_element_by_css_selector("#spanSubmit").click()


sgg_list = browser.find_elements_by_css_selector(".table01 .alignL")
# cnt = 0
# # while True:
# #     if cnt // 3 == 0:

# sgg_list = list(map(lambda x: x.text, sgg_list))
# print(sgg_list)

# 긁어오는 코드
# dong_list = []
# cnt = 1
# sgg = browser.find_element_by_css_selector(f"#table01 > tbody > tr:nth-child({cnt}) > td.alignL.rowspan")
# sigun = browser.find_element_by_css_selector(f"#table01 > tbody > tr:nth-child({cnt}) > td:nth-child(3)")
# dong = browser.find_element_by_css_selector(f"#table01 > tbody > tr:nth-child({cnt}) > td:nth-child(4)")
# print("sgg: " + sgg.text)
# print("sigun: " + sigun.text)
# print(dong.text)
# for i in dong.text.split(","):
#     print(i)




# cnt = 0
# while True:
#     try:
#         cnt += 1
#         sgg = browser.find_element_by_css_selector(f"#table01 > tbody > tr:nth-child({cnt}) > td.alignL.rowspan")
#         dong = browser.find_element_by_css_selector(f"#table01 > tbody > tr:nth-child({cnt}) > td:nth-child(4)")
#         dong_list.append(sgg.text)
#         dong_list.append(dong.text)
#     except:
#         break

print(dong_list)

# sgg_list2 = list(map(lambda x: x.text, sgg_list2))
# print(sgg_list2)
# for i in sgg_list2:
#     print(i.text)
#table01 > tbody > tr:nth-child(1) > td:nth-child(4)
