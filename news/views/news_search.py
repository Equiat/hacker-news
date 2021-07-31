import re
from django.views import View
from django.shortcuts import render 

from news.models import NewsItem

class Search(View):

    def get(self, request):
        context = {}

        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword:
                news = NewsItem.objects.filter(title__icontains=keyword)
                context['news'] = news

        return render(request, 'news/search.html', context)

    def post(self, request):

        if 'stories' in request.POST:
            stories = request.POST['stories']
            if stories:
                news =NewsItem.objects.filter(type=stories).exists()

                context = {
                    'news': news,
                }
        return render(request, 'news/home.html', context)
