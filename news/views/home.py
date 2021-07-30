from django.views.generic import ListView
from django.views import View
from django.shortcuts import render 
from django.core.paginator import Paginator

from news.models.news_item import NewsItem

# class Home(ListView):
#     model = News

#     template_name = 'news/home.html'  # Default: <app_label>/<model_name>_list.html
#     context_object_name = 'news'  # Default: object_list
#     paginate_by = 10
#     queryset = News.objects.all()  # Default: Model.objects.all()


class Home(View):

    def get(self, request):
        news = NewsItem.objects.all().order_by('-added_at')
        paginator = Paginator(news, 10)
        page = request.GET.get('page')
        paged_news = paginator.get_page(page)

        context = {
            'news': paged_news,
        }
        return render(request, 'news/home.html', context)