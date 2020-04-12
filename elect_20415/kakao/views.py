
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
from selenium import webdriver
import time

from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
from django.db import models

from crawl_elect.models import Candidate, Precinct, Brae, Jd

ngrok_url = "http://ec2-3-133-86-208.us-east-2.compute.amazonaws.com:8080"

quick_replies = [
                {'label': '국회의원 조회',
                 'action': 'message',
                 'messageText': '전체 후보자 조회'},
                {'label': '선거구별 후보',
                 'action': 'message',
                 'messageText': '선거구별 조회'},
                {'label': '후보 이름 검색',
                 'action': 'message',
                 'messageText': '이름으로 조회'},
                {'label': '내주소로 후보 찾기',
                 'action': 'block',
                 'blockId': '5e889e80b1fdff0001d6758c'},
                {'label': '정당으로 조회',
                 'action': 'message',
                 'messageText': '정당으로 조회'}

                ]

brae_quick_replies = [
    {'label': '비례대표 전체',
     'action': 'message',
     'message': '비례 대표 전체 조회'},
    {'label': '비례대표 이름',
     'action': 'message',
     'messageText': '비례대표_이름 조회'},
    {'label': '비례대표 정당',
     'action': 'message',
     'messageText': '비례대표_정당으로_조회'}

]

jd_quick_replies = [
    {'label': '국회의원 검색',
      'action': 'message',
      'messageText': '전체 후보자 조회'},

    {'label': '비례대표 검색',
     'action': 'message',
     'messageText': '비례 대표 전체 조회'}
]


#
# @csrf_exempt
# def index(request):
#     answer = request.body.decode('utf-8')
#     return_json_str = json.loads(answer)
#     print(return_json_str)
#     output = {
#         "version": "2.0",
#         "template": {
#             "outputs": [
#                 {
#                     "basicCard": {
#                         "title": f"국회의원 후보자를 검색하시려면",
#                         "description": "아래 버튼을 눌러주세요.",
#                     }
#                 }
#
#             ],
#             'quickReplies': quick_replies
#
#         }
#     }
#
#     return JsonResponse(output)

@csrf_exempt
def show_jd(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    print(return_json_str)
    output = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": f"정당를 정보 확인하시려면",
                        "description": "아래 버튼을 눌러주세요.",
                        # "thumbnail": {
                        #     "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                        # },

                        "buttons": [
                            {
                                "action": "webLink",
                                "label": "정당 확인",
                                "webLinkUrl": f"{ngrok_url}/kakao/jd/searchall"
                            }
                        ],
                    }
                }

            ],
            'quickReplies': jd_quick_replies

        }
    }

    return JsonResponse(output)


def jd_searchall(request):
    jds = Jd.objects.all()

    context = {
        'jds': jds
    }

    return render(request, 'kakao/show_jd.html', context)




#
# @csrf_exempt
# def brae_index(request):
#     answer = (request.body).decode('utf-8')
#     return_json_str = json.loads(answer)
#     print(return_json_str)
#     output = {
#         "version": "2.0",
#         "template": {
#             "outputs": [
#                 {
#                     "basicCard": {
#                         "title": f"비례대표 후보자를 검색하시려면",
#                         "description": "아래 버튼을 눌러주세요.",
#                     }
#                 }
#
#             ],
#             'quickReplies': brae_quick_replies
#
#         }
#     }
#
#     return JsonResponse(output)




@csrf_exempt
def brae_all(request):
    answer = (request.body).decode('utf-8')
    return_json_str = json.loads(answer)
    print(return_json_str)
    output = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": f"비례대표 전체 후보자 정보",
                        "description": "아래 버튼을 눌러주세요.",
                        # "thumbnail": {
                        #     "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                        # },

                        "buttons": [
                            {
                                "action": "webLink",
                                "label": "후보자 확인",
                                "webLinkUrl": f"{ngrok_url}/kakao/brae_searchall"
                            }
                        ],
                    }
                }

            ],
            'quickReplies': brae_quick_replies

        }
    }

    return JsonResponse(output)

def brae_searchall(request):
    candidates = Brae.objects.all()

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

    return render(request, 'kakao/brae_filter.html', context)


@csrf_exempt
def brae_jungdang(request):
    answer = ((request.body).decode('utf-8'))
    res = json.loads(answer)
    print(res)
    jungdang = res.get('action').get('params').get('brae_jungdang')
    # print(jungdang)
    candidates = Brae.objects.filter(belong__contains=jungdang)
    if candidates:
        output = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": f"비례대표 {jungdang}별 후보자정보",
                            "description": "아래 버튼을 눌러주세요.",

                            "buttons": [
                                {
                                    "action": "webLink",
                                    "label": "후보자 확인",
                                    "webLinkUrl": f"{ngrok_url}/kakao/brae_searchjungdang/{jungdang}/"
                                }
                            ],
                        }
                    }

                ],
                'quickReplies': brae_quick_replies

            }
        }
    else:
        output = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": f"비례대표{jungdang} 후보자 정보",
                            "description": "찾으시는 후보자 정보가 없습니다.",
                            # "thumbnail": {
                            #     "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                            # },

                        }
                    }
                ],
                'quickReplies': brae_quick_replies
            }
        }
    return JsonResponse(output)

def brae_search_jungdang(request, jungdang):

    candidates = Brae.objects.filter(belong__contains=jungdang)

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

    return render(request, 'kakao/brae_filter.html', context)



@csrf_exempt
def brae_name(request):
    answer = ((request.body).decode('utf-8'))
    res = json.loads(answer)
    print(res)
    # print(res)
    name = res.get('action').get('params').get('brae_HuboName')
    print(name)
    candidates = Brae.objects.filter(name__contains=name)

    if candidates:
        output = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": f"비례대표 {name} 후보자 정보",
                            "description": "아래 버튼을 눌러주세요.",
                            # "thumbnail": {
                            #     "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                            # },

                            "buttons": [
                                {
                                    "action": "webLink",
                                    "label": "후보자 확인",
                                    "webLinkUrl": f"{ngrok_url}/kakao/brae_searchname/{name}"
                                }
                            ],
                        }
                    }
                ],
                'quickReplies': brae_quick_replies
            }
        }
    else:
        output = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": f"{name} 후보자 정보",
                            "description": "찾으시는 후보자 정보가 없습니다.",
                            # "thumbnail": {
                            #     "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                            # },

                        }
                    }
                ],
                'quickReplies': brae_quick_replies
            }
        }

    return JsonResponse(output)


def brae_search_name(request, name):
    candidates = Brae.objects.filter(name__contains=name)

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

    return render(request, 'kakao/brae_filter.html', context)










@csrf_exempt
def all(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    print(return_json_str)
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
                                "webLinkUrl": f"{ngrok_url}/kakao/searchall"
                            }
                        ],
                    }
                }

            ],
            'quickReplies': quick_replies
        }
    }

    return JsonResponse(output)


# Create your views here.
def searchall(request):
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
def name(request):
    answer = ((request.body).decode('utf-8'))
    res = json.loads(answer)


    # pprint(res)
    name = res.get('action').get('params').get('HuboName')

    candidates = Candidate.objects.filter(name__contains=name)
    if candidates:
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
                'quickReplies': quick_replies
            }
        }
    else:
        output = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": f"{name} 후보자 정보",
                            "description": "찾으시는 후보자 정보가 없습니다.",
                            # "thumbnail": {
                            #     "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                            # },

                        }
                    }
                ],
                'quickReplies': quick_replies
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
    # print(sigun)
    # print(dong)

    juso = f'{sigun}_{dong}'
    sigun, dong = juso.split('_')
    data = Precinct.objects.filter(sigun__contains=sigun[:2], dong__contains=dong[:2]).first()
    if data:
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
            'quickReplies': quick_replies
        }
    }
    else:
        output = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": f"{sigun}_{dong} 후보자 정보",
                            "description": "찾으시는 후보자 정보가 없습니다.",
                            # "thumbnail": {
                            #     "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                            # },

                        }
                    }
                ],
                'quickReplies': quick_replies
            }
        }
    return JsonResponse(output)

def search_juso(request, juso):
    sigun, dong = juso.split('_')

    print(sigun[:2], dong)
    data = Precinct.objects.filter(sigun__contains=sigun[:2], dong__contains=dong).first()

    print(data)



    candidates = Candidate.objects.filter(ep=data.sgg)
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
def jungdang(request):
    answer = ((request.body).decode('utf-8'))
    res = json.loads(answer)

    jungdang = res.get('action').get('params').get('jungdang')
    candidates = Candidate.objects.filter(belong__contains=jungdang)
    if candidates:
        output = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                    "title": f"국회의원 {jungdang}별 후보자정보",
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
            'quickReplies': quick_replies

        }
    }
    else:
        output = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": f"{jungdang} 후보자 정보",
                            "description": "찾으시는 후보자 정보가 없습니다.",
                            # "thumbnail": {
                            #     "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                            # },

                        }
                    }
                ],
                'quickReplies': quick_replies
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
