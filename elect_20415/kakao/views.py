from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json

from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
from django.db import models
from crawl_elect.models import Candidate





# Create your views here.
def index(request):

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

    return render(request, 'kakao/index.html', context)


def filter_candidates(request, sgg):

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
def send_url(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    print(return_json_str)
    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': f"2020 국회의원 선거 후보자 정보입니다.\nhttps://568cb99c.ngrok.io/kakao/filter/{return_str}"
                }
            }],
            'quickReplies': [{
                'label': '처음으로',
                'action': 'message',
                'messageText': '처음으로'
            }]
        }
    })




# Create your views here.
def keyboard(request):
    return JsonResponse({
        'type': 'text'
    })

@csrf_exempt
def message(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': "2020 국회의원 선거 후보자 정보입니다.\nhttps://568cb99c.ngrok.io/kakao/"
                }
            }],
            'quickReplies': [{
                'label': '처음으로',
                'action': 'message',
                'messageText': '처음으로'
            }]
        }
    })


SIM_MSG = 0
SIM_IMG = 1
SIM_CARD = 2

BTN_MSG = 0
BTN_LNK = 1


@csrf_exempt
def checkserver(request):
    req = json.loads(request.body)

    print('---' * 20)
    pprint(req)
    print('***' * 20)
    img = "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
    json_res = makeMessage(SIM_IMG, img, 'hello kakao', 1)

    return JsonResponse(json_res, safe=False)


def makeMessage(type, *args):
    if type == SIM_MSG:
        output = {
            "simpleText": {
                "text": f'{args[0]}'
            }
        }
    elif type == SIM_IMG:
        output = {
            "simpleImage": {
                "imageUrl": f'{args[0]}',
                "altText": f'{args[1]}'
            }
        }
    elif type == SIM_CARD:
        output = makeCard()

    message = {
        "version": "2.0",
        "template": {
            "outputs": [
                output
            ]
        }
    }

    return message


def makeCard():
    btns = makeButton()

    result = {
        "basicCard": {
            "title": "보물상자",
            "description": "보물상자 안에는 뭐가 있을까",
            "thumbnail": {
                "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
            },

            "buttons": [
                {
                    "action": "message",
                    "label": "열어보기",
                    "messageText": "짜잔! 우리가 찾던 보물입니다"
                },
                {
                    "action": "webLink",
                    "label": "구경하기",
                    "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                }
            ],

            "profile": {
                "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
                "nickname": "보물상자"
            },

            "social": {
                "like": 1238,
                "comment": 8,
                "share": 780
            }
        }
    }

    return result


def makeBtn(*args):
    result = []

    for i in range(num):
        btn = {}
        btn["action"] = args[i][0]
        btn['label'] = args[i][1]
        # ---
        btn['webLinkUrl'] = args[i][2]
        btn['messageText'] = args[i][2]

    return result

