from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json

from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
from django.db import models
from crawl_elect.models import Candidate, Precinct





# Create your views here.
def index(request):
    key_list = [
        'ep', 'pic', 'num', 'belong', 'name',
        'gender', 'birth', 'address', 'job', 'level',
        'career', 'wealth', 'military', 'tax_total', 'tax_5y',
        'tax_defalt', 'crim_cnt', 'candi_cnt'
    ]

    candidates = Candidate.objects.all()
    context = {
        'candidates':candidates
    }

    return render(request, 'kakao/index.html', context)


SIM_MSG = 0
SIM_IMG = 1
SIM_CARD = 2

BTN_MSG = 0
BTN_LNK = 1


@csrf_exempt
def checkserver(request):
    req = json.loads(request.body)

    print('---'*20)
    pprint(req)
    print('***'*20)
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
                    "action":  "webLink",
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

    if return_str == '삼청동':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': "삼청동"
                    }
                }],
                'quickReplies': [{
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                }]
            }
        })
    else:
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': "테스트 성공입니다."
                    }
                }],
                'quickReplies': [{
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                }]
            }
        })