from django.shortcuts import render
from django.template.response import TemplateResponse
import random



def kennsaku(request): #検索ページへ飛ばす
    return TemplateResponse(request, 'kennsakusuru.html')

def kennsaku_botann(request):      #1から5までランダムに番号を生成
    x = random.randint(1,5)
    
    return TemplateResponse(request, 'kennsakusuru.html',
                            {'x': x})
    
