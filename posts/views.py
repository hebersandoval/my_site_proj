from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function base views
def post_home(request):
    return HttpResponse('<h1>Hello</h1>')
    # render()