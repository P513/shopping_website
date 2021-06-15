from django.urls import path
from .views import Product_RegisterView
from . import views


app_name = 'product'

urlpatterns = [
    #    path('questions', views.index, name='index'),
    path('', views.index, name='index'),
    # path(''), = 등록된 상품들 보기 -> 구매버튼 클릭시 order로
    path('register/', Product_RegisterView.as_view(), name='register'),
]
