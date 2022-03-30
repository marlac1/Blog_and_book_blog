from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from website.forms import SignupForm
from django.views import View

class HomeView(TemplateView):
    template_name="index.html"
    title = "default"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context

def home(request):
    return HttpResponse("Accueil site : <br> <a href='/blog/'> ici </a> !")

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print(request.POST)
            print(form.cleaned_data)
            return HttpResponse("Merci pour votre inscription.")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form":form})