from django.db import models

# Create your models here.
class Elect(models.Model):
    ep = models.CharField(max_length=20) # 선거구
    pic = models.CharField(max_length=200) # 사진
    num = models.IntegerField() # 기호
    belong = models.CharField(max_length=30) # 소속 정당
    name = models.CharField(max_length=30) # 이름
    gender = models.CharField(max_length=10) # 성별
    birth = models.CharField(max_length=30) # 생년월일 (연령)
    adress = models.CharField(max_length=30) # 주소
    job = models.CharField(max_length=30) # 직업
    level = models.CharField(max_length=50) # 학력
    career = models.CharField(max_length=100) # 경력
    wealth = models.IntegerField() # 재산
    military = models.CharField(max_length=50) # 병역
    tax_total = models.IntegerField() # 납부액
    tax_5y = models.IntegerField() # 최근 5년 체납
    tax_defalt = models.IntegerField() # 현 체납액
    crim_cnt = models.IntegerField() # 전과 횟수
    candi_cnt = models.IntegerField() # 입후보 횟수



class Precinct(models.Model):
    election = models.CharField(max_length=20) # 선거구
    lawlocation = models.CharField(max_length=20) # 법정동
