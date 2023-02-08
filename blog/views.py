from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models  import Post
# Create your views here.

# 장고에서 제공해주는 class 이용

# 장고 class ListVieew 상속
class PostList(ListView):
    model = Post
    ordering = '-pk' # 최근글부터 가져오기 위해 pk의 역순

# 장고 class DetailView 상속
class PostDetail(DetailView):
    model = Post
