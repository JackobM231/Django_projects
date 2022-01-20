# from django.shortcuts import render -deleted
# from django.template import loader
# # Imported loader let us use get_template method (replaced with render method)
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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


def add_post_form(request):
  if request.method == "POST" and request.user.is_authenticated:
    form = PostForm(data=request.POST)
    if form.is_valid():
      form.cleaned_data['author'] = request.user
      post = Post.objects.create(**form.cleaned_data)
      return HttpResponseRedirect(reverse('posts:add'))
  else:
    form = PostForm()
    
  return render(request, 'posts/add.html', {'form': form})

