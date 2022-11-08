from django.views import generic
from django.urls import reverse_lazy

from .models import BlogPost
from .forms import AddPost


class PostListView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return BlogPost.objects.filter(status='pub').order_by('-date_modified')


class PostDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post_detail'


class AddPostView(generic.CreateView):
    form_class = AddPost
    template_name = 'blog/add_post.html'


class UpdatePostView(generic.UpdateView):
    model = BlogPost
    form_class = AddPost
    template_name = 'blog/add_post.html'


class DeletePostView(generic.DeleteView):
    model = BlogPost
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('post_list')
