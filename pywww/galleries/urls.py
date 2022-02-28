from django.urls import path
from galleries.views import galleries, gallery_photos, add_gallery, add_gallery_photo

app_name = 'galleries'
urlpatterns = [
  path('', galleries, name='galleries'),
  path('add', add_gallery, name='add_gallery'),
  path('<str:gallery_slug>', gallery_photos, name='gallery_photos'),
  path('<str:gallery_slug>/add', add_gallery_photo, name='add_gallery_photo'),
]