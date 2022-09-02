from .views import kennsaku,kennsaku_botann    #関数をここに追加することを忘れずに
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


app_name="w" #sekaiは%urlとかではwをつけて呼び出す

urlpatterns = [
    path('zoy',kennsaku,name='kennsakus'),
    path('zoyzoy',kennsaku_botann,name='kennsaku_botanns'),
    ]    #検索画面