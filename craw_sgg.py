from selenium import webdriver
import time
import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par
import os
from selenium.webdriver.support.ui import Select


def sgg_crawl():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    browser = webdriver.Chrome("/Users/jw/Desktop/study/project/congress_election/chromedriver", options=options)
    # browser = webdriver.Chrome("./chromedriver")
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
    city_list = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']
    dong_list = []

    confirm_sgg = ""

    for city in city_list:

        browser.get("http://info.nec.go.kr/main/showDocument.xhtml?electionId=0020200415&topMenuId=BI&secondMenuId=BIGI05")
        time.sleep(4)

        # 국회의원 선거 클릭
        browser.find_element_by_css_selector("#electionId2").click()
        time.sleep(2)

        # 도시 선택
        select_city = Select(browser.find_element_by_id('cityCode'))

        #서울 특별시 선택
        select_city.select_by_visible_text(city)
        time.sleep(1)

        # 조회 버튼 선택 (홈페이지에서 img 타입의 버튼이 하나라서 이렇게 씀)
        browser.find_element_by_css_selector("#spanSubmit").click()

        # 긁어오는 코드
        cnt = 1
        while True:
            try:
                sgg = browser.find_element_by_css_selector(f"#table01 > tbody > tr:nth-child({cnt}) > td.alignL.rowspan").text
                sigun = browser.find_element_by_css_selector(f"#table01 > tbody > tr:nth-child({cnt}) > td:nth-child(3)").text
                dong = browser.find_element_by_css_selector(f"#table01 > tbody > tr:nth-child({cnt}) > td:nth-child(4)").text
                # print("sgg: " + sgg.text)
                # print("sigun: " + sigun.text)
                # print(dong.text)
                print("")
                for i in dong.split(", "):
                    dic = {}
                    if not sgg:
                        sgg = confirm_sgg

                    dic["election"] = sgg
                    dic["sigun"] = sigun
                    dic["admin_location"] = i
                    dong_list.append(dic)
                    confirm_sgg = sgg
                cnt += 1
            except:
                break
        print(city+"============================")
        print(dong_list)


    return dong_list


# sgg_crawl()


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

    # print(dong_list)

    # sgg_list2 = list(map(lambda x: x.text, sgg_list2))
    # print(sgg_list2)
    # for i in sgg_list2:
    #     print(i.text)
    #table01 > tbody > tr:nth-child(1) > td:nth-child(4)

if __name__ == "__main__":
    dong_list = sgg_crawl()
