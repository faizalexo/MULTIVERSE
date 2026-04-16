from django.urls import path
from apps.ecommerce.views import product_views, cart_views, product_list
from apps.ecommerce.views.product_views import home


urlpatterns = [
    path('product_list/', product_views.product_list, name='product_list'),
   
]   

urlpatterns = [
    path('', product_views.home, name='shop_home'),
    path('cart/', cart_views.view_cart,name='cart'),
    path('add/<int:product_id>/', cart_views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_id>/', cart_views.remove_from_cart, name='remove_from_cart'),
]

