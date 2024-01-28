from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name


urlpatterns = [
    path('', BlogListView.as_view(), name='blogpost_list'),
    path('create/', BlogCreateView.as_view(), name='blogpost_create'),
    path('detail/<int:pk>/', cache_page(60)(BlogDetailView.as_view()), name='blogpost_detail'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blogpost_update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blogpost_delete'),
]
