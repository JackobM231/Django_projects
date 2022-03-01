from multiprocessing import context
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Gallery, Photo, Status
from .forms import AddGalleryForm, AddGalleryPhotoForm

# Create your views here.

def galleries(request):
  pub_photos = Photo.objects.filter(status=Status.PUBLISHED)
  # Zdjęcia o statusie PUBLISHED
  gall_id = pub_photos.values_list('gallery_id', flat=True).distinct()
  # Zwraca QuerySet zawierający id wszystkich galerii ze zdjęciami
  pub_gall_with_photos = Gallery.objects.filter(status=Status.PUBLISHED, id__in=gall_id)
  # Do template zostaną przekazane jedynie galerie ze statusem published
  context = {'pub_gall_with_photos': pub_gall_with_photos}
  return render(request, 'galleries/list.html', context)


def gallery_photos(request, gallery_slug):
  # Przekazuje zdjęcia z konkretnej galerii
  gallery = Gallery.objects.get(slug=gallery_slug)
  if gallery.status != Status.PUBLISHED:
    context = {'info': 'Galeria nie jest upubliczniona'}
  else:
    photos = Photo.objects.filter(gallery_id=gallery.id, status=Status.PUBLISHED)
    
    # Ilość elementów na stronie
    if request.method == 'POST':
      elem_on_page = int(request.POST.get('selected').strip('-'))
    # Elementy na stronie po wybraniu
    if request.method == 'GET':
      try:
        elem_on_page = int(request.GET.get('elem'))
      except:
        elem_on_page = 5
        # Ilość elementów na stronie domyślnie
        
    paginator = Paginator(photos, elem_on_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'info': f'Galeria "{gallery.title}"',
               'gallery_slug': gallery_slug,
               'photos': photos,
               'page_obj': page_obj,
               'elem_on_page': elem_on_page}
  return render(request, 'galleries/gallery_photos.html', context)


def add_gallery(request):
  if request.method == 'POST' and request.user.is_authenticated:
    form = AddGalleryForm(request.POST)
    if form.is_valid():
      gallery = form.save()
      return HttpResponseRedirect(reverse('galleries:add_gallery_photo', args=[gallery.slug]))
  else:
    form = AddGalleryForm()
  return render(request, 'galleries/add_gallery.html', {'form': form})


def add_gallery_photo(request, gallery_slug):
  if request.method == 'POST' and request.user.is_authenticated:
    form = AddGalleryPhotoForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      info = 'Zdjęcie zostało dodane'
      form = AddGalleryPhotoForm()
      context = {'info': info, 'form': form}
      return render(request, 'galleries/add_gallery_photo.html', context)
  else:
    form = AddGalleryPhotoForm()
  return render(request, 'galleries/add_gallery_photo.html', {'form': form})