from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
from selenium import webdriver
import time

from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
from django.db import models

from crawl_elect.models import Candidate, Precinct

ngrok_url = "http://c3c9c90a.ngrok.io"

quick_replies = [
                {'label': '전체 조회',
                 'action': 'message',
                 'messageText': '전체 후보자 조회'},
                {'label': '선거구별 조회',
                 'action': 'message',
                 'messageText': '선거구별 조회'},
                {'label': '이름으로 조회',
                 'action': 'message',
                 'messageText': '이름으로 조회'},
                {'label': '주소로찾기',
                 'action': 'block',
                 'blockId': '5e889e80b1fdff0001d6758c'}

                ]

brae_quick_replies = [

]



# Create your views here.
def index(request):
    #전체 후보자 조회
    candidates = Candidate.objects.all()

    for candidate in candidates:
        if "아니한" in candidate.military:
            candidate.military = "X"
        elif "마친사람" in candidate.military:
            candidate.military = "O"
        else:
            candidate.military = "-"

    context = {
        'candidates': candidates
    }

    return render(request, 'kakao/filter.html', context)


def filter_candidates(request, sgg):
    #선거구 별 후보 조회
    candidates = Candidate.objects.filter(ep=sgg).order_by('num')

    for candidate in candidates:
        if "아니한" in candidate.military:
            candidate.military = "X"
        elif "마친사람" in candidate.military:
            candidate.military = "O"
        else:
            candidate.military = "-"

    context = {
        'candidates': candidates
    }

    return render(request, 'kakao/filter.html', context)


@csrf_exempt
def sgg(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)

    return_str = return_json_str['action']['params']['sgg']
    print(return_json_str)

    output = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": f"{return_str} 후보자 정보",
                        "description": "아래 버튼을 눌러주세요.",
                        # "thumbnail": {
                        #     "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                        # },

                        "buttons": [
                            {
                                "action": "webLink",
                                "label": "후보자 확인",
                                "webLinkUrl": f"{ngrok_url}/kakao/filter/{return_str}"
                            }
                        ],
                    }
                }

            ],
            'quickReplies': [
                {'label': '전체 조회',
                 'action': 'message',
                 'messageText': '전체 후보자 조회'},
                {'label': '선거구별 조회',
                 'action': 'message',
                 'messageText': '선거구별 조회'},
                {'label': '이름으로 조회',
                 'action': 'message',
                 'messageText': '이름으로 조회'},
                {'label': '주소로찾기',
                 'action': 'block',
                 'blockId': '5e889e80b1fdff0001d6758c'}
            ]

        }
    }


    return JsonResponse(output)

@csrf_exempt
def message(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    output = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": f"전체 후보자 정보",
                        "description": "아래 버튼을 눌러주세요.",
                        # "thumbnail": {
                        #     "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                        # },

                        "buttons": [
                            {
                                "action": "webLink",
                                "label": "후보자 확인",
                                "webLinkUrl": f"{ngrok_url}/kakao/"
                            }
                        ],
                    }
                }

            ],
            'quickReplies': [
                {'label': '전체 조회',
                 'action': 'message',
                 'messageText': '전체 후보자 조회'},
                {'label': '선거구별 조회',
                 'action': 'message',
                 'messageText': '선거구별 조회'},
                {'label': '이름으로 조회',
                 'action': 'message',
                 'messageText': '이름으로 조회'},
                {'label': '주소로찾기',
                 'action': 'block',
                 'blockId': '5e889e80b1fdff0001d6758c'}
            ]

        }
    }

    return JsonResponse(output)


@csrf_exempt
def name(request):
    answer = ((request.body).decode('utf-8'))
    res = json.loads(answer)

    # pprint(res)
    name = res.get('action').get('params').get('HuboName')

    output = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                    "title": f"{name} 후보자 정보",
                    "description": "아래 버튼을 눌러주세요.",
                    # "thumbnail": {
                    #     "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                    # },

                    "buttons": [
                        {
                            "action": "webLink",
                            "label": "후보자 확인",
                            "webLinkUrl": f"{ngrok_url}/kakao/searchname/{name}"
                        }
                    ],
                }
                }
            ],
            'quickReplies': [
                {'label': '전체 조회',
                 'action': 'message',
                 'messageText': '전체 후보자 조회'},
                {'label': '선거구별 조회',
                 'action': 'message',
                 'messageText': '선거구별 조회'},
                {'label': '이름으로 조회',
                 'action': 'message',
                 'messageText': '이름으로 조회'},
                {'label': '주소로찾기',
                 'action': 'block',
                 'blockId': '5e889e80b1fdff0001d6758c'}
            ]
        }
    }

    return JsonResponse(output)


def search_name(request, name):
    candidates = Candidate.objects.filter(name__contains=name)

    for candidate in candidates:
        if "아니한" in candidate.military:
            candidate.military = "X"
        elif "마친사람" in candidate.military:
            candidate.military = "O"
        else:
            candidate.military = "-"

    context = {
        'candidates': candidates
    }

    return render(request, 'kakao/filter.html', context)

@csrf_exempt
def juso(request):
    answer = ((request.body).decode('utf-8'))
    res = json.loads(answer)

    # pprint(res)
    sigun = res.get('action').get('params').get('sigun')
    dong = res.get('action').get('params').get('dong')

    juso = f'{sigun}_{dong}'

    output = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                    "title": f"{juso} 후보자 정보",
                    "description": "아래 버튼을 눌러주세요.",
                    # "thumbnail": {
                    #     "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                    # },

                    "buttons": [
                        {
                            "action": "webLink",
                            "label": "후보자 확인",
                            "webLinkUrl": f"{ngrok_url}/kakao/searchjuso/{juso}"
                        }
                    ],
                }
                }

            ],
            'quickReplies': [
                {'label': '전체 조회',
                 'action': 'message',
                 'messageText': '전체 후보자 조회'},
                {'label': '선거구별 조회',
                 'action': 'message',
                 'messageText': '선거구별 조회'},
                {'label': '이름으로 조회',
                 'action': 'message',
                 'messageText': '이름으로 조회'},
                {'label': '주소로찾기',
                         'action': 'block',
                'blockId': '5e889e80b1fdff0001d6758c'}
            ]

        }
    }

    return JsonResponse(output)

def search_juso(request, juso):
    sigun, dong = juso.split('_')

    # print(sigun[:2], dong[:2])
    data = Precinct.objects.filter(sigun__contains=sigun[:2], dong__contains=dong[:2]).first()
    # print(data)



    if data:
        candidates = Candidate.objects.filter(ep=data.sgg)
        for candidate in candidates:
            if "아니한" in candidate.military:
                candidate.military = "X"
            elif "마친사람" in candidate.military:
                candidate.military = "O"
            else:
                candidate.military = "-"
    else:
        candidates = []
    context = {
        'candidates': candidates
    }

    return render(request, 'kakao/filter.html', context)


@csrf_exempt
def jungdang(request):
    answer = ((request.body).decode('utf-8'))
    res = json.loads(answer)

    jungdang = res.get('action').get('params').get('jungdang')


    output = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                    "title": f"{jungdang} 후보자별 정보",
                    "description": "아래 버튼을 눌러주세요.",

                    "buttons": [
                        {
                            "action": "webLink",
                            "label": "후보자 확인",
                            "webLinkUrl": f"{ngrok_url}/kakao/searchjungdang/{jungdang}"
                        }
                    ],
                }
                }

            ],
            'quickReplies': [
                {'label': '전체 조회',
                 'action': 'message',
                 'messageText': '전체 후보자 조회'},
                {'label': '선거구별 조회',
                 'action': 'message',
                 'messageText': '선거구별 조회'},
                {'label': '이름으로 조회',
                 'action': 'message',
                 'messageText': '이름으로 조회'},
                {'label': '주소로찾기',
                         'action': 'block',
                'blockId': '5e889e80b1fdff0001d6758c'}
            ]

        }
    }

    return JsonResponse(output)

def search_jungdang(request, jungdang):

    candidates = Candidate.objects.filter(belong__contains=jungdang)

    for candidate in candidates:
        if "아니한" in candidate.military:
            candidate.military = "X"
        elif "마친사람" in candidate.military:
            candidate.military = "O"
        else:
            candidate.military = "-"

    context = {
        'candidates': candidates
    }

    return render(request, 'kakao/filter.html', context)


# def show_gong(request, gong):
#     browser = webdriver.Chrome("./chromedriver")
#     browser.get(f"{gong}")
#     time.sleep(1)
#     browser.find_element_by_css_selector(".fl-r a").click()
#
#     return render(request, 'kakao/gong')