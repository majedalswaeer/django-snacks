from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class BaseView(TemplateView):
    template_name = "base.html"


class HomeView(TemplateView):
    template_name = "home.html"


class AboutUsView(TemplateView):
    template_name = "aboutus.html"

