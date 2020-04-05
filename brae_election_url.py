from selenium import webdriver
import time
import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par
import os
from selenium.webdriver.support.ui import Select


def crawl():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")
    browser = webdriver.Chrome("/Users/jw/Desktop/study/project/congress_election/chromedriver", options=options)
    # browser = webdriver.Chrome("./chromedriver")
    browser.get("http://info.nec.go.kr/main/showDocument.xhtml?electionId=0020200415&topMenuId=CP&secondMenuId=CPRI03")
    time.sleep(4)

    #국회의원 선거 클릭
    browser.find_element_by_css_selector("#electionId2").click()
    time.sleep(2)

    #도시 선택 cityCode

    city_list = browser.find_elements_by_css_selector("select#cityCode > option")
    city_list = list(map(lambda x: x.text, city_list))
    city_list = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']
    all_candidate_list = []
    all_candidate_image_list = []
    all_candidate_deatil_urllist = []
    all_candidate_gong_urllist = []

    for city in city_list:
        print("도시: "+city)
        select_city = Select(browser.find_element_by_id('cityCode'))
        #서울 특별시 선택
        select_city.select_by_visible_text(city)
        time.sleep(1)

        # 선거구 선택 sggCityCode
        sgg_list = browser.find_elements_by_css_selector("select#sggCityCode > option")
        sgg_list = list(map(lambda x: x.text, sgg_list))[1:]
        time.sleep(1)

        for sgg in sgg_list:
            print("선거구: " + sgg)
            select_sgg = Select(browser.find_element_by_id("sggCityCode"))
            # 선거구 종로구 선거 선택
            select_sgg.select_by_visible_text(sgg)
            time.sleep(1)

            # 조회 버튼 선택 (홈페이지에서 img 타입의 버튼이 하나라서 이렇게 씀)
            browser.find_element_by_css_selector("#spanSubmit").click()

            # 국회의원 정보 크롤
            candidate_list = browser.find_elements_by_css_selector("table#table01 td")
            candidate_list = list(map(lambda x: x.text, candidate_list))
            all_candidate_list += candidate_list


            # 국회의원 얼굴 이미지 URL 크롤링
            candidate_image_list = browser.find_elements_by_css_selector("table#table01 tr input[type=image]")
            candidate_image_list = list(map(lambda  x: x.get_attribute('src'), candidate_image_list))
            # print(candidate_image_list)
            # print(candidate_list, candidate_image_list)
            all_candidate_image_list += candidate_image_list

            #image_url 에서 url 검색

            for image_url in candidate_image_list:
                index = image_url.find("Hb")
                huboid = image_url[index + 2: index + 11]

                detail_url = f"http://info.nec.go.kr/electioninfo/candidate_detail_info.xhtml?electionId=0020200415&huboId={huboid}"
                gong_url = f"http://policy.nec.go.kr/plc/popup/initUMAPopup.do?sgId=20200415&subSgId=220200415&huboid={huboid}#none"
                all_candidate_deatil_urllist.append(detail_url)
                all_candidate_gong_urllist.append(gong_url)


        browser.get("http://info.nec.go.kr/main/showDocument.xhtml?electionId=0020200415&topMenuId=CP&secondMenuId=CPRI03")
        time.sleep(4)

        # 국회의원 선거 클릭
        browser.find_element_by_css_selector("#electionId2").click()
        time.sleep(2)

        print(all_candidate_list)
        print(all_candidate_image_list)
        print(all_candidate_deatil_urllist)
        print(all_candidate_gong_urllist)

    return all_candidate_list, all_candidate_image_list, all_candidate_deatil_urllist, all_candidate_gong_urllist

# crawl()


if __name__ == "__main__":
    li, img, detail_url, gong_url = crawl()
    print(li)
    print(img)
    print(detail_url)
    print(gong_url)
