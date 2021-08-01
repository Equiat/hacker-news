from django.urls import path

from api.views import ListItems
from api.views import AddItem, UpdateItem


urlpatterns = [
    path('list-items/', ListItems.as_view(), name='list-items'),
    path('list-items/<id>', UpdateItem.as_view(), name='update-item'),
    path('add-item', AddItem.as_view(), name='add-item'),
]
