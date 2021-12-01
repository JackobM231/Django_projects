# from django.shortcuts import render -deleted
from django.http import HttpResponse
# from django.template import loader
# # Imported loader let us use get_template method (replaced with render method)
from django.shortcuts import render

from posts.models import Post

# Create your views here.
def posts_list(request):
  posts = Post.objects.all()
  context = {'posts_list': posts, 'posts_number': len(posts), 'topics': ['fantasy', 3, True]}
  return render(request, "posts/list.html", context)

# def post(request):
#   post = Post.objects.first()
#   html = f"<h2>{post.title}</h2>"
#   html += f'''<div>
#                 <small>Utworzono: {post.created}, zmodyfikowano: {post.modified}</small>
#               </div>
#               <div>
#                 <p>{post.content}.</p>
#               </div>'''
#   return HttpResponse(html)

def posts_details(request):
  post = Post.objects.first()
  context = {"post": post}
  return render(request, "posts/details.html", context)

  