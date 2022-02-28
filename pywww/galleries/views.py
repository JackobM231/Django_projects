from multiprocessing import context
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Gallery, Photo
from .forms import AddGalleryForm, AddGalleryPhotoForm

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
    on_page_elem = 5
    # Ilość elementów na stronie
    # if request.method == 'POST':
    #   form = request.POST
    #   print(form)
      # if form.is_valid():
      #   on_page_elem = form.cleaned_data['value']
      # on_page_elem = int(request.POST.get('value'))
    paginator = Paginator(photos, on_page_elem)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'info': f'Galeria {gallery.title}',
               'photos': photos,
               'page_obj': page_obj}
  return render(request, 'galleries/gallery_photos.html', context)


def add_gallery(request):
  if request.method == 'POST' and request.user.is_authenticated:
    form = AddGalleryForm(request.POST)
    if form.is_valid():
      form.save()
      info = 'Galeria została utworzona'
      form = AddGalleryForm()
      context = {'info': info, 'form': form}
      return render(request, 'galleries/add_gallery.html', context)
  else:
    form = AddGalleryForm()
  return render(request, 'galleries/add_gallery.html', {'form': form})


def add_gallery_photo(request, gallery_slug):
  if request.method == 'POST' and request.user.is_authenticated:
    form = AddGalleryPhotoForm(request.POST)
    if form.is_valid():
      form.save()
      info = 'Zdjęcie zostało dodane'
      form = AddGalleryPhotoForm()
      context = {'info': info, 'form': form}
      return render(request, 'galleries/add_gallery_photo.html', context)
  else:
    form = AddGalleryPhotoForm()
  return render(request, 'galleries/add_gallery_photo.html', {'form': form})