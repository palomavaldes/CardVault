from django.urls import path
from .views import cart_add, cart_detail, cart_remove

app_name = 'cart'
urlpatterns = [
    path('add/<int:item_pk>/', cart_add, name="cart_add"),
    path('',cart_detail, name="cart_detail"),
    path('remove/<int:item_pk>/', cart_remove, name="remove")
]