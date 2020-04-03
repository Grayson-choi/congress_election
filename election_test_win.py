from selenium import webdriver
import time
import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par
import os
from selenium.webdriver.support.ui import Select


# browser = webdriver.Chrome("./chromedriver")
# # 윈도우는 아래 코드를 실행
# # browser = webdriver.Chrome("./chromedriver.exe")



# browser.get("http://info.nec.go.kr/main/showDocument.xhtml?electionId=0020200415&topMenuId=CP&secondMenuId=CPRI03")
# time.sleep(4)

# # candidate = input("궁금한 후보자를 입력하세요. >> ")
# # 선거 사이트로 이동

# #국회의원 선거 클릭
# browser.find_element_by_css_selector("#electionId2").click()
# time.sleep(2)

# #도시 선택 cityCode
# select_city = Select(browser.find_element_by_id('cityCode'))
# city_list = browser.find_elements_by_css_selector("select#cityCode > option")
# city_list = list(map(lambda x: x.text, city_list))
# # city = input(""str(city_list[1:]))

# #서울 특별시 선택
# select_city.select_by_visible_text("서울특별시")
# time.sleep(1)

# # 선거구 선택 sggCityCode
# select_sgg = Select(browser.find_element_by_id("sggCityCode"))
# sgg_list = browser.find_elements_by_css_selector("select#sggCityCode > option")
# sgg_list = list(map(lambda x: x.text, sgg_list))
# time.sleep(1)
# # 선거구 종로구 선거 선택
# select_sgg.select_by_visible_text("종로구")
# time.sleep(1)


# # 조회 버튼 선택 (홈페이지에서 img 타입의 버튼이 하나라서 이렇게 씀)
# browser.find_element_by_css_selector("#spanSubmit").click()

# # 국회의원 정보 크롤
# candidate_list = browser.find_elements_by_css_selector("table#table01 td")
# candidate_list = list(map(lambda x: x.text, candidate_list))
# print(candidate_list)

# # 국회의원 얼굴 이미지 URL 크롤링
# candidate_image_list = browser.find_elements_by_css_selector("table#table01 tr input[type=image]")
# candidate_image_list = list(map(lambda  x: x.get_attribute('src'), candidate_image_list))
# print(candidate_image_list)

# # 이미지 저장
# for index, value in enumerate(candidate_image_list):
#     req.urlretrieve(value, f"./image/{index}.png")

# time.sleep(5)
# browser.quit()

# cityCode

def crawl():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")
    browser = webdriver.Chrome("E:\dev\pydev\elect\congress_election\chromedriver_win.exe", chrome_options=options)
    browser.get("http://info.nec.go.kr/main/showDocument.xhtml?electionId=0020200415&topMenuId=CP&secondMenuId=CPRI03")
    time.sleep(4)

    #국회의원 선거 클릭
    browser.find_element_by_css_selector("#electionId2").click()
    time.sleep(2)

    #도시 선택 cityCode
    select_city = Select(browser.find_element_by_id('cityCode'))
    city_list = browser.find_elements_by_css_selector("select#cityCode > option")
    city_list = list(map(lambda x: x.text, city_list))
    city_list = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']


    for city in city_list:
        #서울 특별시 선택
        select_city.select_by_visible_text(city)
        time.sleep(1)

        # 선거구 선택 sggCityCode
        sgg_list = browser.find_elements_by_css_selector("select#sggCityCode > option")
        sgg_list = list(map(lambda x: x.text, sgg_list))[1:]
        time.sleep(1)

        for sgg in sgg_list:
            select_sgg = Select(browser.find_element_by_id("sggCityCode"))
            # 선거구 종로구 선거 선택
            select_sgg.select_by_visible_text(sgg)
            time.sleep(1)

            # 조회 버튼 선택 (홈페이지에서 img 타입의 버튼이 하나라서 이렇게 씀)
            browser.find_element_by_css_selector("#spanSubmit").click()

            # 국회의원 정보 크롤
            candidate_list = browser.find_elements_by_css_selector("table#table01 td")
            candidate_list = list(map(lambda x: x.text, candidate_list))
            # print(candidate_list)

            # 국회의원 얼굴 이미지 URL 크롤링
            candidate_image_list = browser.find_elements_by_css_selector("table#table01 tr input[type=image]")
            candidate_image_list = list(map(lambda  x: x.get_attribute('src'), candidate_image_list))
            # print(candidate_image_list)



    return candidate_list, candidate_image_list


if __name__ == "__main__":
    li, url = crawl()
    print(li)
    print(url)