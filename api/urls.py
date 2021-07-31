from re import L
from django.urls import path

from api.views.list_items import ListItems
from api.views.add_item import AddItem


urlpatterns = [
    path('list-items', ListItems.as_view(), 'list-items'),
    path('add-item', AddItem.as_view(), 'add-item'),
]
