from bs4 import BeautifulSoup
import urllib
from urllib import request

client_id = "tzNzp0WUJ0fso1rabfsE"
client_cid = "gs7pn8TeRn"

url = "https://openapi.naver.com/v1/datalab/search"
requested = request.Request(url)
requested.add_header("X-Naver-Client-Id", client_id)
requested.add_header("X-Naver-Client-Secret", client_cid)
requested.add_header("Content-Type", "application/json")

