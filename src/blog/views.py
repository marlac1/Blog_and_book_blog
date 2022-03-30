from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from blog.models import BlogPost
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from website.forms import BlogPostForm
from datetime import datetime

# Create your views here.
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required, user_passes_test

class BlogIndexView(ListView):
    model = BlogPost
    template_name = 'blog/index.html'
    context_object_name = "articles"

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post.html'
    context_object_name = "article"

class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/create_article.html'
    form_class = BlogPostForm
    success_url = reverse_lazy("blog-index")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        form.instance.published = True
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Créer"
        return context

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/create_article.html'
    form_class = BlogPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Modifier"
        return context

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/delete_article.html'
    context_object_name = "article"
    success_url = reverse_lazy("blog-index")


def article_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        init_values = {}
        if request.user.is_authenticated:
            init_values["author"] = request.user
        init_values["date"] = datetime.today()
        form = BlogPostForm(initial=init_values)
    return render(request, "blog/create_article.html", {"form":form})

def blog_posts(request):
    posts = BlogPost.objects.all()
    blog_post = get_object_or_404(BlogPost, pk=25)
    return render(request, "blog/index.html", context={"posts":posts})

def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, "blog/post.html", context={"post": post})
