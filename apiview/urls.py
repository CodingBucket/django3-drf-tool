from django.urls import path

from apiview.views import PostView, PostCreateView, PostListCreateView

urlpatterns = [
    path('', PostView.as_view(), name='test'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('list-create/', PostListCreateView.as_view(), name='list-create'),
]