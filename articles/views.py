from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_safe
from .models import Review
from .forms import ReviewForm
from django.contrib import messages
from django.core.paginator import Paginator

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

@login_required(login_url='/accounts/signin')
def hk(request):
    return render(request, 'articles/hk.html')

def reindex(request):
    reviews = Review.objects.order_by('-pk')
    
    page = request.GET.get('page', '1')
    paginator = Paginator(reviews, 3)
    posts = paginator.get_page(page)

    context= {
        'reviews' : reviews,
        'posts' : posts,
    }

    return render(request, 'articles/reindex.html', context)

def create(request):
    # disney_name = request.GET.get('disney_name')
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            # review.disney_name = disney_name
            review.save()
            messages.success(request, '소중한 후기 감사합니다:)')
            return redirect('articles:reindex')
    else: 
        review_form = ReviewForm()
    context = {
        'review_form': review_form,
        'disney_name': request.GET.get('disney_name')
    }
    return render(request, 'articles/reform.html', context)