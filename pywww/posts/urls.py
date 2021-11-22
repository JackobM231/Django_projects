from django.urls import path
from posts.views import posts_list, post

urlpatterns = [
    path('', posts_list),
    path('1', post)
]