from django.shortcuts import render
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import election_test
import craw_sgg
from .models import Candidate, Precinct

# Create your views here.

def index(request):

    li, pic = election_test.crawl()
    
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

    for candi in cand_list:
        c = Candidate(**candi)
        c.save()
    # print(cand_list)

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
