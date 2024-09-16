from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, 'core/home.html')

def review(req):
    return render(req, 'core/review.html')

def category (req):
    return render(req, 'core/home.html')