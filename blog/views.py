from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import BlogPost


class BlogListView(ListView):
    model = BlogPost


class BlogCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content')
    success_url = reverse_lazy('blog:blogpost_list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        else:
            print('ошибка')
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content')
    success_url = reverse_lazy('blog:blogpost_list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)


class BlogDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:blogpost_list')
