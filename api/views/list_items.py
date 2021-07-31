from rest_framework import status
from rest_framework.generics import ListAPIView

from api.serializers import NewsItemSerializer
from news.models import NewsItem
from api.response import Response

# Create your views here.
class ListItems(ListAPIView):
    serializer_class = NewsItemSerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = NewsItem.objects.all()
        keyword = self.request.query_params.get('keyword', None)
        if keyword is not None:
            queryset = queryset.filter(title__icontains=keyword)
            return queryset
        
        job = self.request.query_params.get('job', None)
        if job is not None:
            queryset = queryset.filter(type=job)
            return queryset
        
        story = self.request.query_params.get('story', None)
        if story is not None:
            queryset = queryset.filter(type=story)
            return queryset
        
        return queryset
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(data={'data': serializer.data}, status=status.HTTP_200_OK)

