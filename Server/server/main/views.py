
# viewsets : 자주 사용하는 공통적인 view 로직을 그룹화 한 것
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WonderSerializer
from .models import Wonder
from rest_framework.decorators import api_view
from rest_framework.response import Response
# 아래는 연습용 추가 import
import urllib.request
import urllib.parse
#from bs4 import BeautifulSoup
from django.http import HttpResponse
import requests


# # 인증키를 입력
# key_value ='b56169eae0274d53943d1431cc14a41a'
# # 여러 가지 기본 정보들을 입력
# detail_value = '&Type=xml&pIndex=1&pSize=100&SIGUN_NM='
# # API 중 원하는 정보만을 검색해서 받는 부분
# search = input('원하는 경기도 시군명을 입력해주세요:)')
# final_url = 'https://openapi.gg.go.kr/TourismRestaurant?Key='+ key_value + detail_value + urllib.parse.quote_plus(search)
# request = final_url

# # 웹으로 API 데이터를 전달 - 지금은 연습이므로 localhost 사용
# def store_list(request):
#     req = requests.get(final_url)
#     html=req.text
#     soup = BeautifulSoup(html,'html.parser')
#     store_name = soup.find_all("bizplc_nm")
#     store_address = soup.find_all("refine_lotno_addr")
#     # 웹으로 데이터를 전달하는 부분
#     result = ''
#     for i in range(len(store_name)):
#         result = result + f'<p>{store_name[i]} {store_address[i]}</p>'
#     return HttpResponse(result)


def search_keyword(request):

    if request.method == "GET":
        return render(request, 'main/a.html')

    elif request.method == "POST":
        query = request.POST.get('query')  # 검색어

        url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(
            query)
        headers = {
            "Authorization": "KakaoAK 13f796a480ad63c4e169282f09c34c7f"
        }
        place = requests.get(url, headers=headers).json()['documents']
        return HttpResponse(place)


def search_category(request):
    if request.method == "GET":
        #    return render(request, 'main/a.html')

    elif request.method == "POST":
        x = request.POST.get('x', None)  # 위도
        y = request.POST.get('y', None)  # 경도
        radius = request.POST.get('radius', None)  # 지름
        category = request.POST.get('category', None)  # 카테고리

        url = f'https://dapi.kakao.com/v2/local/search/category.json?category_group_code={category}&x={x}&y={y}&radius={radius}'
    #url ='https://dapi.kakao.com/v2/local/search/category.json?category={}'.format(category)
        headers = {
            "Authorization": "KakaoAK 13f796a480ad63c4e169282f09c34c7f"
        }
        place = requests.get(url, headers=headers).json()['documents']
        return HttpResponse(place)
