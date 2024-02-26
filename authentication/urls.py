from django.contrib import admin
from django.urls import path,include
from .views import deposit, withdraw, balance,transaction_report

from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("home",views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='sigout'),
    path('deposit', views.deposit, name='deposit'),
    path('withdraw', views.withdraw, name='withdraw'),
    path('balance', views.balance, name='balance'),
    path('transaction-report', transaction_report, name='transaction_report'),
]    
