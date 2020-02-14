from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
	path('checkout/', views.check_out.as_view(), name='checkout'),
	path('order-summary/', views.order_summary_view.as_view(), name='order-summary'),
	path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
	path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
	path('remove-single-item-from-cart/<slug>/', views.remove_single_item_from_cart, name='remove-single-item-from-cart'),
	path('detail-product/<slug>/', views.detail_product.as_view(), name='detail-product'),
	path('detail-productlast/<slug>/', views.detail_product.as_view(), name='detail-productlast'),
	path('detail-productforu/<slug>/', views.detail_product.as_view(), name='detail-productforu'),
	path('signin/', views.log_in.as_view(), name='signin'),
    path('index/', views.index.as_view(), name='index'),
    path('signup/', views.join_in.as_view(), name='signup'),
]