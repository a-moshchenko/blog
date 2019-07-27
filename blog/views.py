from django.views.generic import ListView
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render, get_object_or_404


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
                    Q(title__icontains=query) | Q(content__icontains=query)
        )
        return object_list


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_on = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})
