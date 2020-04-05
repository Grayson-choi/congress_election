from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json

from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
from django.db import models
from crawl_elect.models import Candidate,Precinct




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

def search_sgg(request, dong):
    all_sgg = Precinct.objects.all()

    sggs = Precinct.objects.filter(dong=dong)

    sgg_list = []

    context = {
        'sggs': all_sgg
    }
    return render(request, 'kakao/search_sgg.html', context)


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


def name_candidates(request, name):
    # 이름으로 후보자 조회
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

    return render(request, 'kakao/name.html', context)

@csrf_exempt
def filter_name(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)

    return_str = return_json_str['action']['params']['sgg']
    print(return_json_str)
    # print(return_str)
    # print(return_json_str['action']['params']['sgg'])
    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': f"2020 국회의원 선거 후보자 정보입니다.\nhttps://cff01795.ngrok.io/kakao/name/{return_str}"
                }
            }],
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
            ]
        }
    })






@csrf_exempt
def send_url(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)

    return_str = return_json_str['action']['params']['sgg']
    print(return_json_str)
    # print(return_str)
    # print(return_json_str['action']['params']['sgg'])
    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': f"2020 국회의원 선거 후보자 정보입니다.\nhttps://cff01795.ngrok.io/kakao/filter/{return_str}"
                }
            }],
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
            ]
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
                    'text': "2020 국회의원 선거 후보자 정보입니다.\nhttps://cff01795.ngrok.io/kakao/"
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

    if return_str == '후보자':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': "2020 국회의원 선거 후보자 정보입니다.\nhttps://0d328970.ngrok.io/kakao/"
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
                        'text': "2020 국회의원 선거 후보자 정보입니다.\nhttps://0d328970.ngrok.io/kakao/"
                    }
                }],
                'quickReplies': [{
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                }]
            }
        })

from pprint import pprint

@csrf_exempt
def context(request):
    answer = ((request.body).decode('utf-8'))
    res = json.loads(answer)

    pprint(res)

    output ={
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "컨텍스트 1"
                    }
                }
            ]
        }
    }
    return JsonResponse(output)


@csrf_exempt
def context2(request):
    answer = ((request.body).decode('utf-8'))
    res = json.loads(answer)

    pprint(res)

    output ={
        "version": "2.0",
        "context": {
            "values": [
                {
                    "name": "c_2",
                    "lifeSpan": 10,
                    "params": {
                    "key2": "여기 컨텍스트 두번째 데이터 저장 되었습니다.",
                    }
                },
            ]
        },
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "컨텍스트 2"
                    }
                }
            ]
        }
    }
    return JsonResponse(output)

@csrf_exempt
def context3(request):
    answer = ((request.body).decode('utf-8'))
    res = json.loads(answer)

    pprint(res)

    # c_1 = res.get('contexts')[0]
    # c_1 = c_1.get('params').get('key1').get("value") # 첫번째 블록에서 전달된 내용

    # c_2 = res.get('contexts')[1]
    # c_2 = c_2.get('params').get('key3').get("value") # 두번째 블록에서 전달된 내용
    c_1= '1'
    c_2='2'
    output ={
        "version": "2.0",
        "context": {
            "values": [
                {
                    "name": "c_1",
                    "lifeSpan": 0,
                },
                {
                    "name": "c_2",
                    "lifeSpan": 0,
                },
            ]
        },
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": f"컨텍스트 3\n{c_1}\n{c_2}"
                    }
                }
            ]
        }
    }
    return JsonResponse(output)

