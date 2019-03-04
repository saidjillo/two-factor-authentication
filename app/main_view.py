from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


from django.views.generic import ListView, TemplateView



# main view starts here
class Home(TemplateView):
    template_name = "index.html"


