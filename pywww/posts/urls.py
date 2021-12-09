from django.urls import path
from posts.views import posts_list, post_details

app_name = 'posts'
urlpatterns = [
    path('', posts_list, name='list'),
    # int: Lets us to define what type of data we want
    path('<int:post_id>', post_details, name='post_details'),
]