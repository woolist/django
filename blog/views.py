from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models  import Post, Category
# Create your views here.

# 장고에서 제공해주는 class 이용

# 장고 class ListVieew 상속
class PostList(ListView):
    model = Post
    ordering = '-pk' # 최근글부터 가져오기 위해 pk의 역순

    def get_context_data(self, **kwargs):
        context = super(PostList,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

# 장고 class DetailView 상속
class PostDetail(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super(PostDetail,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

def category_page(request, slug): # slug는 일반적으로 이미 얻은 데이터를 사용하여 유효한 url을 생성하는 방법
    if slug == 'no category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list':post_list,
            'categories': Category.objects.all(),
            'no_category_post_count':Post.objects.filter(category=None).count(),
            'category':category,
        }
    )
