from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('addpost/', views.AddPostView.as_view(), name='add_post'),
    path('<int:pk>/update', views.UpdatePostView.as_view(), name='edit_post'),
    path('<int:pk>/delete', views.DeletePostView.as_view(), name='delete_post'),
]
