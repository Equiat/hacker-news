from rest_framework import status
from rest_framework.views import APIView

from news.models import NewsItem
from api.serializers import NewsItemSerializer
from api.response import Response

class AddItem(APIView):
    
    def post(self, request):
        serializer = NewsItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'status': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

