from django.urls import path
from galleries.views import galleries, gallery_photos

app_name = 'galleries'
urlpatterns = [
  path('', galleries, name='galleries'),
  path('<str:gallery_slug>', gallery_photos, name='gallery_photos'),  
]