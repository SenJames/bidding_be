# bidding_app/urls.py
from django.urls import path
from .views import BidListCreateView, BidList, ItemListView, BidAction

urlpatterns = [
    path('bids/', BidListCreateView.as_view(), name='bid-list-create'),
    path('bidlist/', BidList.as_view(), name='bid_list'),
    path('itemlist/', ItemListView.as_view(), name='item_list'),
    path('bidnow/', BidAction.as_view(), name='bid_event'),

]
