from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.http import HttpResponse
from .models import add_pension
from django.template.response import TemplateResponse
from django.http import Http404,HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.views.decorators.http import require_POST
import math


def nennkin_list(request):    #一覧画面    ページ操作つき
    products = add_pension.objects.order_by('kinngaku')
    paginator = Paginator(products, 5)

    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except (EmptyPage, PageNotAnInteger):
        products = paginator.page(1)
    return TemplateResponse(request, 'home.html',
                            {'products': products})


def product_detail(request, product_id):    #詳細画面
    try:
        product = add_pension.objects.get(id=product_id)
    except add_pension.DoesNotExist:
        raise Http404
    
    cart = request.session.get('cart')
    
    if product_id == 5 or product_id == 6 or product_id == 8: #３子以降の加給年金のID。この場合は何度でも追加できるようにする。
        a = []
        a.append("n")

    elif product_id in cart:
        a = []#すでにカートに追加されてればなにもいれない
        
    else:
        a = []
        a.append("n")#まだカートに追加されていなければnにして同じ年金はカートに一回しか追加できないようにする。




    if product_id == 6 or product_id == 8: #6は障害年金のこと。8は遺族年金のこと。カートに追加する必要がないIDはこちらにまとめておく。
        b = []
        b.append("n")
    else:
        b = []

    return TemplateResponse(request, 'product_detail.html',
                            {'product': product,
                             'a':a,
                             'b':b})



@require_POST     #カートに追加
def cart_add(request, product_id):
    if not add_pension.objects.filter(id=product_id).exists():
        raise Http404
    cart = request.session.get('cart')
    if cart:
        cart.append(product_id)
        request.session['cart'] = cart
    else:
        request.session['cart'] = [product_id]
    return HttpResponseRedirect(reverse('pension_lists'))




def cart_list(request):    #カートの中身
    cart = request.session.get('cart')
    if cart:
        products = []
        for product_id in cart:
            try:
                product = add_pension.objects.get(id=product_id)
                products.append(product)
            except add_pension.DoesNotExist:
                pass
    else:
        products = []

    total_price = 0
    total_getugaku = 0
    for product in products:
        total_price += product.kinngaku
    total_getugaku = math.floor(total_price/12)

    return TemplateResponse(request, 'cart.html',
                            {'products': products,
                             'total_price': total_price,
                             "total_getugaku":total_getugaku})


@require_POST    #カートからの削除
def cart_delete(request, product_id):
    cart = request.session.get('cart')
    if cart:
        filtered = []
        for p in cart:
            if p != product_id:
                filtered.append(p)
        request.session['cart'] = filtered
    return HttpResponseRedirect(reverse('cart_lists'))

"""
class Home(ListView):
    template_name = "home.html"
    model = add_pension
#一旦休止
"""