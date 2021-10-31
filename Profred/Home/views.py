from django.shortcuts import render


def index(request):
    return render(request, 'Home/index.html')


def pricing(request):
    return render( request,'Home/pricing.html')


def about(request):
    return render( request,'Home/about.html')


def blog(request):
    return render( request,'Home/blog.html')

def signup(request):
     return render( request,'Home/signup.html')
