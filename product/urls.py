from django.urls import path
from .views import Product_RegisterView, ProductListView
from . import views


app_name = 'product'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    # path(''), = 등록된 상품들 보기 -> 구매버튼 클릭시 order로
    path('register/', Product_RegisterView.as_view(), name='register'),
]
