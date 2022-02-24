from multiprocessing import context
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Gallery, Photo

# Create your views here.

def galleries(request):
  gall_with_photos = Photo.objects.values_list('gallery_id', flat=True).distinct()
  # Zwraca QuerySet zawierający id wszystkich galerii ze zdjęciami
  pub_gall_with_photos = Gallery.objects.filter(status='PUBLISHED', id__in=gall_with_photos)
  # Do template zostaną przekazane jedynie galerie ze statusem published
  context = {'pub_gall_with_photos': pub_gall_with_photos}
  return render(request, 'galleries/list.html', context)


def gallery_photos(request, gallery_slug):
  # Przekazuje zdjęcia z konkretnej galerii
  gallery = Gallery.objects.get(slug=gallery_slug)
  if gallery.status != 'PUBLISHED':
    context = {'info': 'Galeria nie jest upubliczniona'}
  else:
    photos = Photo.objects.filter(gallery_id=gallery.id, status='PUBLISHED')
    context = {'info': f'Galeria {gallery.title}',
               'photos': photos}
    
  return render(request, 'galleries/gallery_photos.html', context)