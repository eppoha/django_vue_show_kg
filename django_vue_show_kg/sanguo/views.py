# from django.http import JsonResponse
from django.shortcuts import render
from .models import People
from rest_framework import viewsets
from rest_framework import filters
from .serizlizers import PeopleSerializers

from .models import People
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from urllib.parse import unquote
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.views import APIView
from .serizlizers import PeopleSerializers

from rest_framework.parsers import JSONParser
# Create your views here.
class PeopleViewSet(viewsets.ModelViewSet):
    """人物视图集"""
    queryset = People.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    serializer_class = PeopleSerializers

# 做一个数据搜索功能
@csrf_exempt
@api_view(["post"])
def search(request):
    # print("=====request.method： ====", request.method)
    # print("request:", request)
    print("request.body:", request.body)
    # json.loads和json.load会报错，所以先按照字符串处理
    # print("request.body:", json.loads(request.body))
    datas = unquote(str(request.body))[1:].replace('=', ':')
    print("datas1:", datas)
    datas = datas.split(":")
    print("datas2:", datas)
    
    name = datas[1].replace('\'', '')
    # 如果没有输入的话则按刘备输入
    if name == '' or name == ' ':
        name = '刘备'
    queryset = People.objects.filter(name__icontains=name)
    res = []
    for obj in queryset:
        # 把所有数据都加上
        res.append({
            "number": obj.number or "", 
            "name": obj.name or "",
            "wuli": obj.wuli or "",
            "zhili": obj.zhili or "",
            "texing1": obj.texing1 or "",
            "texing2": obj.texing2 or "",
            "texing3": obj.texing3 or "",
            "bishaji": obj.bishaji or "",
            "yili": obj.yili or "",
            "xiangxing": obj.xiangxing or "",
            "zhongzu": obj.zhongzu or "",
            "gender": obj.gender or "",
            "img": obj.img or "",
            "figure": obj.figure or "",
            "desc": obj.figure or "",
            "text_all": obj.figure or "",
        })
    print("res:", res)
    return Response({"res": res}, status=200)

# 添加数据功能
@csrf_exempt
@api_view(["post"])
def submit(request):
    print("request:", request)
    print("request.body:", request.body)
    postdata = request.POST
    print("postdata:", postdata)
    data1 = {}
    for key, value in postdata.items():
        print(key, value)
        data1[key] = value
    print("data1:",data1)
    data = PeopleSerializers(data=data1)
    if data.is_valid():
            data.save()
    return Response({"res": data1}, status=200)
