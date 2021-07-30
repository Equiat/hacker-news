from django.urls import path

from news.views.home import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
