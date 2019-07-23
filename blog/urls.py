from . import views
from django.urls import path

urlpatterns = [
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]
