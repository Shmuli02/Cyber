from django.urls import path

from .views import homePageView, adduserView, editView, newbikeView

urlpatterns = [
    path('', homePageView, name='home'),
    path('edit/',editView, name='edit'),
    path('login/adduser/',adduserView, name='adduser'),
    path('newbike/',newbikeView, name='newbike')
]
