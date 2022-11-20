from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

@login_required(login_url='/accounts/signin')
def la(request):
    return render(request, 'articles/la.html')

@login_required(login_url='/accounts/signin')
def paris(request):
    return render(request, 'articles/paris.html')

@login_required(login_url='/accounts/signin')
def tokyo(request):
    return render(request, 'articles/tokyo.html')