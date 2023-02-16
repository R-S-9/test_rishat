from django.urls import path

from .payment import Payment
from .item import ItemStripe
from .mainpage import MainPage


urlpatterns = [
    path('buy/<int:buy_id>/<str:currency>', Payment.as_view(), name='buy'),
    path('item/<int:item_id>', ItemStripe.as_view(), name='item'),
    path('', MainPage.as_view(), name='mainpage'),
]
