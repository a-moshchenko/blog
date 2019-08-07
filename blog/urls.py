from . import views
from django.urls import path


urlpatterns = [
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post,
         name='add_comment_to_post'),
    path('admin/', views.return_to_admin, name='return')
]
