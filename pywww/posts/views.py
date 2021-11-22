# from django.shortcuts import render -deleted
from django.http import HttpResponse

from posts.models import Post

# Create your views here.
def posts_list(request):
  html = "<ul>"
  for post in Post.objects.all():
    html += f"<li>{post}</li>"
  html += "</li>"
  return HttpResponse(html)

def post(request):
  post = Post.objects.first()
  html = f"<h2>{post.title}</h2>"
  html += f'''<div>
                <small>Utworzono: {post.created}, zmodyfikowano: {post.modified}</small>
              </div>
              <div>
                <p>{post.content}.</p>
              </div>'''
  return HttpResponse(html)