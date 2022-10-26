from django.shortcuts import render
from blog.models import Post
# Create your views here.

def index(request):
    # 전체 포스팅을 가져올 준비 아직 가져오지는 않음
    post_qs = Post.objects.all().order_by('-id')
    return render(request,'blog/index.html', {
        "post_list": post_qs,
    })

def single_post_page(request, pk):
    # 한개만 가져오려고 쓰는 함수 get
    # pk를 인자로 받아서 키워드 pk가 인자로 받은 pk가 동일하면 함수 수행
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/single_post_page.html', {
        'post' : post
    })