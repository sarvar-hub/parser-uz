from django.views import generic
from .models import Post
import urllib.parse
from django.core.paginator import Paginator
from .filters import PostFilter
from django.shortcuts import render


class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 3

    # def get_queryset(self):
    #     return Post.objects.order_by('-created_on', '-id')[:20]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        paginator = Paginator(context['filter'].qs, self.paginate_by)
        page = self.request.GET.get('page')
        posts = paginator.get_page(page)
        context['posts'] = posts
        gt = self.request.GET.copy()
        if 'page' in gt:
            del gt['page']
        

        context['params'] =  urllib.parse.urlencode(gt)
        return context

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def top(request):

    post_list = Post.objects.order_by('-created_on', '-id')[:10]
    paginator = Paginator(post_list, 5) 
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'top.html', {'posts': posts})

