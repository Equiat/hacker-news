from django.views.generic import ListView
from django.views import View
from django.shortcuts import render 
from django.core.paginator import Paginator

from news.models import NewsItem

# class Home(ListView):
#     model = News

#     template_name = 'news/home.html'  # Default: <app_label>/<model_name>_list.html
#     context_object_name = 'news'  # Default: object_list
#     paginate_by = 10
#     queryset = News.objects.all()  # Default: Model.objects.all()


class Home(View):

    def get(self, request):
        news = NewsItem.objects.all().order_by('-added_at')
        paginator = Paginator(news, per_page=10)
        page = request.GET.get('page')
        paged_news = paginator.get_page(page)

        types = None
        types_paginator = None
        types_page = None
        paged_types = None

        context = {
            'news': paged_news,
            'types': paged_types
        }

        # context = {
        #     'news': paged_news
        # }

        # return render(request, 'news/home.html', context)

    # def post(self, request):
        if 'story' in request.GET:
            story = request.GET['story']
            if story:
                types = NewsItem.objects.filter(type=story)
                types_paginator = Paginator(types, per_page=10)
                types_page = request.GET.get('page')
                paged_types = types_paginator.get_page(page)

                context['types'] = paged_types
                
    

        if 'job' in request.GET:
            job = request.GET['job']
            if job:
                types = NewsItem.objects.filter(type=job)
                types_paginator = Paginator(types, per_page=3)
                types_page = request.GET.get('page')
                paged_types = types_paginator.get_page(types_page)

                context['types'] = paged_types
    
        return render(request, 'news/home.html', context)