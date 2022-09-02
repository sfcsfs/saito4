#from .views import Home
from .views import nennkin_list,product_detail,cart_add,cart_list,cart_delete    #関数をここに追加することを忘れずに
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

"""
urlpatterns = [
    path("home/", Home.as_view(),name='pension_list'),
    ]  + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
#一旦休止
"""

    
urlpatterns = [
    path('products/<int:product_id>/',product_detail,name='product_details'),    #詳細画面
    path('cart/<int:product_id>/', cart_add, name='cart_adds'),    #カートに入れる
    path("home/",nennkin_list,name='pension_lists'),  #一覧画面
    path('cart/', cart_list, name='cart_lists'),    #カートの中身 
    path('cart_delete/<int:product_id>/',cart_delete, name='cart_deletes'),   #カートからの削除
    ]  + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)