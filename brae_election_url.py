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
    browser.find_element_by_css_selector("#electionId7").click()
    time.sleep(2)

    gd_list = ['더불어민주당', '미래통합당', '민생당', '미래한국당', '더불어시민당', '정의당', '우리공화당', '민중당', '한국경제당', '국민의당', '친박신당', '열린민주당',
     '코리아', '가자!평화인권당', '가자환경당', '공화당', '국가혁명배당금당', '국민새정당', '국민참여신당', '기독당', '기독자유통일당', '기본소득당', '깨어있는시민연대당', '남북통일당',
     '노동당', '녹색당', '대한당', '대한민국당', '미래당', '미래민주당', '미래자영업당', '민중민주당', '사이버모바일국민정책당', '새누리당', '시대전환', '여성의당', '우리당',
     '자유당', '새벽당', '정치개혁연합', '자영업당', '직능자영업당', '충청의미래당', '친박연대', '통일민주당', '통합민주당', '한국국민당', '한국복지당', '한나라당', '한반도미래연합',
     '홍익당']

    #정당 선택 cityCode
    gd_list = browser.find_elements_by_css_selector("select#proportionalRepresentationCode > option")
    # set_city = Select(browser.find_element_by_css_selector('proportionalRepresentationCode'))
    # set_city.select_by_index(0)
    time.sleep(1)

    # 조회 버튼 선택 (홈페이지에서 img 타입의 버튼이 하나라서 이렇게 씀)
    browser.find_element_by_css_selector("#spanSubmit").click()
    time.sleep(1)
    # gd_list = list(map(lambda x: x.text, gd_list))
    # print(gd_list)
    all_candidate_image_list = []
    all_candidate_list = []
    all_candidate_deatil_urllist = []
    all_candidate_gong_urllist = []

    candidate_list = browser.find_elements_by_css_selector("table#table01 td")
    candidate_list = list(map(lambda x: x.text, candidate_list))
    print(candidate_list)
    all_candidate_list += candidate_list


    # 국회의원 얼굴 이미지 URL 크롤링
    candidate_image_list = browser.find_elements_by_css_selector("table#table01 tr input[type=image]")
    candidate_image_list = list(map(lambda  x: x.get_attribute('src'), candidate_image_list))
    print(candidate_image_list)
    # print(candidate_list, candidate_image_list)
    all_candidate_image_list += candidate_image_list

    #image_url 에서 url 검색

    for image_url in candidate_image_list:
        index = image_url.find("Hb")
        huboid = image_url[index + 2: index + 11]

        detail_url = f"http://info.nec.go.kr/electioninfo/candidate_detail_info.xhtml?electionId=0020200415&huboId={huboid}"
        gong_url = f"http://policy.nec.go.kr/plc/popup/initUMAPopup.do?sgId=20200415&subSgId=220200415&huboid={huboid}#none"
        print(detail_url)
        print(gong_url)
        all_candidate_deatil_urllist.append(detail_url)
        all_candidate_gong_urllist.append(gong_url)

    return all_candidate_list, all_candidate_image_list, all_candidate_deatil_urllist, all_candidate_gong_urllist

# crawl()


if __name__ == "__main__":
    li, img, detail_url, gong_url = crawl()
    print(li)
    print(img)
    print(detail_url)
    print(gong_url)
