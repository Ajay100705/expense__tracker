
from django.urls import path
from expense.views import index,deleteTransaction,registration,login_page,logout_page

urlpatterns = [
    path('', index, name='index'),
    path('registration/', registration, name='registration'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('delete-transaction/<uuid>/',deleteTransaction, name='deleteTransaction'),
]