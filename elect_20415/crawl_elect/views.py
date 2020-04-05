from django.shortcuts import render
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import election_test
import craw_sgg
import election_url
import brae_election_url
from .models import Candidate, Precinct, Brae

# Create your views here.

def index(request):

    li, pic,url = election_test.crawl()
    
    key_list = [
        'ep', 'pic', 'num', 'belong', 'name', 
        'gender','birth', 'address', 'job', 'level',
        'career', 'wealth', 'military', 'tax_total', 'tax_5y',
        'tax_defalt', 'crim_cnt', 'candi_cnt'
    ]
    cand_list = []
    for cnt in range(len(li)//18):
        data = dict(zip(key_list, li[cnt*18: (cnt+1)*18]))
        data['pic'] = pic[cnt]
        cand_list.append(data)

    # 새로 만드는 코드
    for candi in cand_list:
        c = Candidate(**candi)
        c.save()
    # print(cand_list)

    context = {
        'cand_list': cand_list
        # 'pic': pic
    }

    return render(request, 'crawl_elect/index.html', context)


def update_candidate(request):
    li, img, detail_url, gong_url = election_url.crawl()

    key_list = [
        'ep', 'pic', 'num', 'belong', 'name',
        'gender', 'birth', 'address', 'job', 'level',
        'career', 'wealth', 'military', 'tax_total', 'tax_5y',
        'tax_defalt', 'crim_cnt', 'candi_cnt'
    ]

    cand_list = []
    for cnt in range(len(li) // 18):
        data = dict(zip(key_list, li[cnt * 18: (cnt + 1) * 18]))
        data['pic'] = img[cnt]
        data['detail_url'] = detail_url[cnt]
        data['gong_url'] = gong_url[cnt]
        cand_list.append(data)

    # 업데이트 코드
    for candi in cand_list:
        c = Candidate.objects.filter(name=candi['name'], belong=candi['belong']).first()
        c.detail_url = candi['detail_url']
        c.gong_url = candi['gong_url']
        c.save()
    print(cand_list)

    context = {
        'cand_list': cand_list
        # 'pic': pic
    }

    return render(request, 'crawl_elect/index.html', context)


def add_sgg(request):
    dong_list = craw_sgg.sgg_crawl()

    context = {
        'dong_list': dong_list
        # 'pic': pic
    }

    # 디비에 넣는 코드
    for dong in dong_list:
        dong_db = Precinct(**dong)
        dong_db.save()

    return render(request, 'crawl_elect/add_sgg.html', context)

def brae_add(request):
    li, pic, detail_url, gong_url = brae_election_url.crawl()

    key_list = [
        'ep', 'pic', 'belong', 'suggest_num', 'name',
        'gender', 'birth', 'address', 'job', 'level',
        'career', 'wealth', 'military', 'tax_total', 'tax_5y',
        'tax_defalt', 'crim_cnt', 'candi_cnt'
    ]

    cand_list = []
    for cnt in range(len(li) // 18):
        data = dict(zip(key_list, li[cnt * 18: (cnt + 1) * 18]))
        data['pic'] = pic[cnt]
        data['detail_url'] = detail_url[cnt]
        data['gong_url'] = gong_url[cnt]
        cand_list.append(data)

    # 새로 만드는 코드
    for candi in cand_list:
        c = Brae(**candi)
        c.save()
    # print(cand_list)

    context = {
        'cand_list': cand_list
        # 'pic': pic
    }

    return render(request, 'crawl_elect/brae.html', context)