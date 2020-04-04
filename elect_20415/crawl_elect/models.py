from django.db import models

# Create your models here.
class Candidate(models.Model):
    ep = models.CharField(max_length=20) # 선거구
    pic = models.CharField(max_length=200) # 사진
    num = models.IntegerField() # 기호
    belong = models.CharField(max_length=30) # 소속 정당
    name = models.CharField(max_length=30) # 이름
    gender = models.CharField(max_length=10) # 성별
    birth = models.CharField(max_length=30) # 생년월일 (연령)
    address = models.CharField(max_length=30) # 주소
    job = models.CharField(max_length=30) # 직업
    level = models.CharField(max_length=50) # 학력
    career = models.CharField(max_length=100) # 경력
    wealth = models.CharField(max_length=50) # 재산
    military = models.CharField(max_length=50) # 병역
    tax_total = models.CharField(max_length=50) # 납부액
    tax_5y = models.CharField(max_length=50) # 최근 5년 체납
    tax_defalt = models.CharField(max_length=50) # 현 체납액
    crim_cnt = models.CharField(max_length=50) # 전과 횟수
    candi_cnt = models.CharField(max_length=50) # 입후보 횟수

    def __str__(self):
        return self.name

class Precinct(models.Model):
    city = models.CharField(max_length=20) # 특별시, 광역시, 도
    sigun = models.CharField(max_length=20) # 시군구
    dong = models.CharField(max_length=20) # 행정동

    sgg = models.CharField(max_length=20) # 선거구

    def __str__(self):
        return f'City: {city} / Sigun: {sigun} / Dong: {dong} => {sgg}'


# class Gusigun(models.Model):
#     precint = models.ForeignKey(Precinct, on_delete=models.CASCADE)
#     gu = models.CharField(max_length=20)
