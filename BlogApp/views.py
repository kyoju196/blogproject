from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.

def home(request):
    Blog_element = Blog.objects
    return render(request, './home.html', {'Blog_element':Blog_element})

def detail(request,blog_id):
    Blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'Blog_detail': Blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    Blog_element_new = Blog()
    Blog_element_new.title = request.GET['title']
    Blog_element_new.body = request.GET['body']
    Blog_element_new.pub_date = timezone.datetime.now()
    Blog_element_new.save()
    return redirect('/blog/'+str(Blog_element_new.id))