# from django.shortcuts import render -deleted
# from django.template import loader
# # Imported loader let us use get_template method (replaced with render method)
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator

from posts.models import Post
from posts.forms import PostForm

# Create your views here.
def posts_list(request):
  published_posts = Post.objects.filter(published=True)
  all_posts = Post.objects.count()
  context = {'posts_list': published_posts, 'all_posts_number': all_posts, 'topics': ['fantasy', 3, True]}
  return render(request, "posts/list.html", context)


def post_details(request, post_id):
  post = Post.objects.get(id=post_id)
  context = {"post": post}
  return render(request, "posts/details.html", context)


def add_post(request):
  return render(request, "posts/add.html")


# def add_post_form(request): Wcześniejsza wersja do PostForm(forms.Form)
#   if request.method == "POST" and request.user.is_authenticated:
#     form = PostForm(data=request.POST)
#     if form.is_valid():
#       form.cleaned_data['author'] = request.user
#       post = Post.objects.create(**form.cleaned_data)
#       return HttpResponseRedirect(reverse('posts:add'))
#   else:
#     form = PostForm()
    
#   return render(request, 'posts/add.html', {'form': form})


def add_post_form(request):
  if request.method == "POST" and request.user.is_authenticated:
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.author = request.user
      instance.save()
      form.save_m2m()
      # Zapis relacji ManyToMany
      return HttpResponseRedirect(reverse('posts:add'))
  else:
    form = PostForm()
    
  return render(request, 'posts/add.html', {'form': form})


def edit_post(request, post_id):
  post = get_object_or_404(Post, id=post_id)
  if request.method == "POST":
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('posts:post_details', args=[post_id]))
  else:
    form = PostForm(instance=post)

  return render(request, 'posts/add.html', {'form': form})


def listing(request):
  # Paginacja
  content_list = Post.objects.all()
  paginator = Paginator(content_list, 10)
  
  page_num = request.GET.get('page')
  page_obj = paginator.get_page(page_num)
  return render(request, 'posts/pag_list.html', {'page_obj': page_obj})