from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

@login_required(login_url='/accounts/signin')
def la(request):
    return render(request, 'articles/la.html')