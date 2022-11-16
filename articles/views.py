from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def la(request):
    return render(request, 'articles/la.html')