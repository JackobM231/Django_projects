from django.urls import path
from django.conf.urls.static import static
from posts.views import posts_list, post_details


app_name = 'posts'
urlpatterns = [
    path('', posts_list, name='list'),
    path('<int:post_id>', post_details, name='post_details'),
]