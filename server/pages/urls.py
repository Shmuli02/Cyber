from django.urls import path

from .views import homePageView, balanceView, adduserView, editView, newbikeView

urlpatterns = [
    path('', homePageView, name='home'),
    path('balance/', balanceView, name='balance'),
    path('edit/',editView, name='edit'),
    path('login/adduser/',adduserView, name='adduser'),
    path('newbike/',newbikeView, name='newbike')
]
