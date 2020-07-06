from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .models import Post

 
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #get_object_or_404(Post, pk=pk) 이 방법은 pk를 못찾으면 404 페이지를 띄움
    #Post.objects.get(pk=pk) 이 방법은 pk를 못찾았을 때 오류가 뜸
    return render(request, 'blog/post_detail.html', {'post': post})