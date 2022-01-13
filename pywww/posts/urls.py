from django.urls import path
# from django.conf.urls.static import static
from posts.views import posts_list, post_details, add_post


app_name = 'posts'
urlpatterns = [
    path('', posts_list, name='list'),
    path('add', add_post, name='add'),
    path('<int:post_id>', post_details, name='post_details'),
]