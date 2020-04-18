from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from crawl_elect.models import Candidate, Precinct, Brae, Jd


ngrok_url = "https://6a213729.ngrok.io"

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

def simple_candidate(candidates):
    for candidate in candidates:
        if "아니한" in candidate.military:
            candidate.military = "X"
        elif "마친사람" in candidate.military:
            candidate.military = "O"
        else:
            candidate.military = "-"
        candidate.wealth = won_to_korean(candidate.wealth)

    return candidates

def make_output(params, button_title, url, q_button):
    output = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": params,
                        "description": "아래 버튼을 눌러주세요.",
                        "buttons": [
                            {
                                "action": "webLink",
                                "label": button_title,
                                "webLinkUrl": url
                            }
                        ],
                    }
                }
            ],
            'quickReplies': q_button
        }
    }
    return output

def make_no_output(title,q_button):
    output = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": title,
                        "description": "찾으시는 후보자 정보가 없습니다.",
                    }
                }
            ],
            'quickReplies': q_button
        }
    }
    return output

def won_to_korean(num):
    num = num.replace(',',"")
    if num[0] == "-":
        if len(num) <= 6:
            return "-" + num[-5:-1] + "만원"
        else:
            return "-" + num[:-5] + "억" + num[-5:-1] + "만원"
    else:
        if len(num) <= 5:
            return num[-5:-1] + "만원"
        else:
            return num[:-5] + "억" + num[-5:-1] + "만원"


@csrf_exempt
def show_jd(request):
    answer = request.body.decode('utf-8')
    return_json_str = json.loads(answer)
    print(return_json_str)
    title = f"정당를 정보 확인하시려면"
    label = "정당 확인"
    url = f"{ngrok_url}/kakao/jd/searchall"
    q_button = jd_quick_replies
    output = make_output(title, label, url, q_button)

    return JsonResponse(output)


def jd_searchall(request):
    jds = Jd.objects.all()

    context = {
        'jds': jds
    }

    return render(request, 'kakao/show_jd.html', context)


@csrf_exempt
def brae_all(request):
    answer = (request.body).decode('utf-8')
    return_json_str = json.loads(answer)
    title = f"비례대표 전체 후보자 정보"
    label = "후보자 확인"
    url = f"{ngrok_url}/kakao/brae_searchall"
    q_button = brae_quick_replies
    output = make_output(title, label, url, q_button)


    return JsonResponse(output)

def brae_searchall(request):
    candidates = Brae.objects.all()
    candidates = simple_candidate(candidates)
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
    title = f"비례대표 {jungdang}별 후보자정보"
    label = "후보자 확인"
    url = f"{ngrok_url}/kakao/brae_searchjungdang/{jungdang}/"
    q_button = brae_quick_replies
    output = make_output(title, label, url, q_button)

    if candidates:
        output = make_output(title, label, url, q_button)
    else:
        output = make_no_output(title,q_button)
    return JsonResponse(output)

def brae_search_jungdang(request, jungdang):

    candidates = Brae.objects.filter(belong__contains=jungdang)

    candidates = simple_candidate(candidates)

    context = {
        'candidates': candidates
    }

    return render(request, 'kakao/brae_filter.html', context)



@csrf_exempt
def brae_name(request):
    answer = ((request.body).decode('utf-8'))
    res = json.loads(answer)
    name = res.get('action').get('params').get('brae_HuboName')
    candidates = Brae.objects.filter(name__contains=name)
    title = f"비례대표 {name} 후보자 정보"
    label = "후보자 확인"
    url = f"{ngrok_url}/kakao/brae_searchname/{name}"
    q_button = brae_quick_replies


    if candidates:
        output = make_output(title, label, url, q_button)
    else:
        output = make_no_output(title, q_button)

    return JsonResponse(output)


def brae_search_name(request, name):
    candidates = Brae.objects.filter(name__contains=name)
    simple_candidate(candidates)
    context = {
        'candidates': candidates
    }

    return render(request, 'kakao/brae_filter.html', context)










@csrf_exempt
def all(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    title = f"전체 후보자 정보"
    label = "후보자 확인"
    url = f"{ngrok_url}/kakao/searchall/"
    q_button = quick_replies
    output = make_output(title, label, url, q_button)

    return JsonResponse(output)


# Create your views here.
def searchall(request):
    #전체 후보자 조회
    candidates = Candidate.objects.all()
    candidates = simple_candidate(candidates)

    context = {
        'candidates': candidates
    }

    return render(request, 'kakao/filter.html', context)






@csrf_exempt
def sgg(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)

    sgg = return_json_str['action']['params']['sgg']
    print(return_json_str)
    candidates = Candidate.objects.filter(ep__contains=sgg)
    title = f"{sgg} 후보자 정보"
    label = "후보자 확인"
    url = f"{ngrok_url}/kakao/filter/{sgg}"
    q_button = quick_replies

    if candidates:
        output = make_output(title, label, url, q_button)
    else:
        output = make_no_output(title, q_button)

    return JsonResponse(output)


def filter_candidates(request, sgg):
    #선거구 별 후보 조회
    candidates = Candidate.objects.filter(ep=sgg).order_by('num')

    candidates = simple_candidate(candidates)
    context = {
        'candidates': candidates
    }

    return render(request, 'kakao/filter.html', context)


@csrf_exempt
def name(request):
    answer = ((request.body).decode('utf-8'))
    res = json.loads(answer)
    name = res.get('action').get('params').get('HuboName')

    candidates = Candidate.objects.filter(name__contains=name)
    title = f"{name} 후보자 정보"
    label = "후보자 확인"
    url = f"{ngrok_url}/kakao/searchname/{name}"
    q_button = quick_replies

    if candidates:
        output = make_output(title, label, url, q_button)
    else:
        output = make_no_output(title, q_button)

    return JsonResponse(output)



def search_name(request, name):
    candidates = Candidate.objects.filter(name__contains=name)
    candidates = simple_candidate(candidates)

    context = {
        'candidates': candidates
    }

    return render(request, 'kakao/filter.html', context)

@csrf_exempt
def juso(request):
    answer = ((request.body).decode('utf-8'))
    res = json.loads(answer)

    sigun = res.get('action').get('params').get('sigun')
    dong = res.get('action').get('params').get('dong')

    juso = f'{sigun}_{dong}'
    sigun, dong = juso.split('_')
    data = Precinct.objects.filter(sigun__contains=sigun[:2], dong__contains=dong[:2]).first()

    title = f"{juso} 후보자 정보"
    label = "후보자 확인"
    url = f"{ngrok_url}/kakao/searchjuso/{juso}"
    q_button = quick_replies

    if data:
        output = make_output(title, label, url, q_button)
    else:
        output = make_no_output(title, q_button)

    return JsonResponse(output)


def search_juso(request, juso):
    sigun, dong = juso.split('_')

    data = Precinct.objects.filter(sigun__contains=sigun[:2], dong__contains=dong).first()

    candidates = Candidate.objects.filter(ep=data.sgg)
    candidates = simple_candidate(candidates)

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


    title = f"국회의원 {jungdang}별 후보자정보"
    label = "후보자 확인"
    url = f"{ngrok_url}/kakao/searchjungdang/{jungdang}"
    q_button = quick_replies

    if candidates:
        output = make_output(title, label, url, q_button)
    else:
        output = make_no_output(title, q_button)
    return JsonResponse(output)

def search_jungdang(request, jungdang):

    candidates = Candidate.objects.filter(belong__contains=jungdang)

    candidates = simple_candidate(candidates)

    context = {
        'candidates': candidates
    }

    return render(request, 'kakao/filter.html', context)
