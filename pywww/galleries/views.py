from multiprocessing import context
from django.shortcuts import render
from django.db.models import Avg, Min, Max, Count
from django.forms import modelformset_factory
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
  '''
  pub_gall = Gallery.objects.filter(status=Status.PUBLISHED)
  # Galerie o statusie published
  pub_gall_with_photos = pub_gall.annotate(photos_count=Count('photos')).filter(photos_count__gt=0)
  # Galerie posiadające więcej niż jedno zdjęcie zastosownie annotacji
  '''
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
  gallery = Gallery.objects.get(slug=gallery_slug)
  PhotosFormSet = modelformset_factory(Photo, form=AddGalleryPhotoForm, extra=1)
  # Tworzymy zbiór formularzy na podsatawie modelu Photo oraz formularzu AddGalleryPhotoForm (wyświetlanie jednego domyślnie)
  formset = PhotosFormSet(queryset=gallery.photos.none())
  # Formularze istniejących zdjęć nie będą zaliczane do formset
  if request.method == 'POST' and request.user.is_authenticated:
    formset = PhotosFormSet(request.POST, request.FILES)
    if formset.is_valid():
      print(formset)
      for f in formset.cleaned_data:
        if f:
          print(f)
          Photo.objects.create(gallery=gallery, **f)
    return HttpResponseRedirect(reverse('galleries:add_gallery_photo', args=[gallery_slug]))
  # if request.method == 'POST' and request.user.is_authenticated:
  #   form = AddGalleryPhotoForm(request.POST, request.FILES)
  #   if form.is_valid():
  #     form.save()
  #     info = 'Zdjęcie zostało dodane'
  #     form = AddGalleryPhotoForm()
  #     context = {'info': info, 'form': form}
  #     return render(request, 'galleries/add_gallery_photo.html', context)
  else:
    # form = AddGalleryPhotoForm()
    return render(request, 'galleries/add_gallery_photo.html', {'formset': formset})