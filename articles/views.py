from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_safe
from .models import Review
from .forms import ReviewForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Avg, Min, Max, Count, F, Sum, Func
import math

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

@login_required(login_url='/accounts/signin')
def la(request):
    
    reviews = Review.objects.filter(disney_name='Los Angeles').order_by('-pk')
    grade_mean = Review.objects.filter(disney_name='Los Angeles').aggregate(grade=Avg('grade'))
    if grade_mean:
        grade = round(*grade_mean.values(), 1)
    else:
        grade = 0.0
        
    page = request.GET.get('page', '1')
    paginator = Paginator(reviews, 3)
    posts = paginator.get_page(page)
    
    context= {
        'reviews' : reviews,
        'grade' : grade,
        'posts' : posts,
    }
    
    return render(request, 'articles/la.html', context)

@login_required(login_url='/accounts/signin')
def paris(request):
    reviews = Review.objects.filter(disney_name='Paris').order_by('-pk')
    grade_mean = Review.objects.filter(disney_name='Paris').aggregate(grade=Avg('grade'))
    if grade_mean:
        grade = round(*grade_mean.values(), 1)
    else:
        grade = 0.0

    page = request.GET.get('page', '1')
    paginator = Paginator(reviews, 3)
    posts = paginator.get_page(page)
    
    context= {
        'reviews' : reviews,
        'grade' : grade,
        'posts' : posts,
    }
    return render(request, 'articles/paris.html', context)

@login_required(login_url='/accounts/signin')
def tokyo(request):
    reviews = Review.objects.filter(disney_name='Tokyo').order_by('-pk')
    grade_mean = Review.objects.filter(disney_name='Tokyo').aggregate(grade=Avg('grade'))
    if grade_mean:
        grade = round(*grade_mean.values(), 1)
    else:
        grade = 0.0

    page = request.GET.get('page', '1')
    paginator = Paginator(reviews, 3)
    posts = paginator.get_page(page)
    
    context= {
        'reviews' : reviews,
        'grade' : grade,
        'posts' : posts,
    }
    return render(request, 'articles/tokyo.html', context)

@login_required(login_url='/accounts/signin')
def hk(request):
    reviews = Review.objects.filter(disney_name='Hong Kong').order_by('-pk')
    grade_mean = Review.objects.filter(disney_name='Hong Kong').aggregate(grade=Avg('grade'))
    if reviews:
        grade = round(*grade_mean.values(), 1)
    else:
        grade = 0.0
    
    page = request.GET.get('page', '1')
    paginator = Paginator(reviews, 3)
    posts = paginator.get_page(page)
    
    context= {
        'reviews' : reviews,
        'grade' : grade,
        'grade_meam' : grade_mean,
        'posts' : posts,
    }
    return render(request, 'articles/hk.html', context)

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

def delete(request, pk):
    Review.objects.get(pk=pk).delete()

    return redirect('articles:reindex')

def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    # comment_form = CommentForm()
    # template에 객체 전달
    context = {
        'review' : review,
        # 'comments': review.comment_set.all(),
        # 'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)