from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
   

    path('home/', views.home.as_view(), name='option2'),
    path('home/productcat/<int:id>', views.productcat, name='productcat'),
    path('single-product/<slug>/', views.single_product.as_view(), name='single-product'),
    path('blog-post/', views.blog_post.as_view(), name='blog-post'),
    path('blog-single/<slug>/', views.blog_single.as_view(), name='blog-single'),
    path('contact/', views.contact_page.as_view(), name='contact'),
    path('about/', views.about_page.as_view(), name='about'),
    path('search-item/', views.search_item, name='search-item'),
]