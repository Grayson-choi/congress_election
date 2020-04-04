from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json

from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
from django.db import models
from crawl_elect.models import Candidate, Precinct


candidates = Candidate.objects.all()

duplicate = []

for candidate in candidates:
    if candidate.name in duplicate:
        print(candidate.name)
    else:
        duplicate.append(candidate.name)


