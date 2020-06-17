from django.shortcuts import render ,redirect, get_object_or_404
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from django.db.models import Count

from .models import Post, Subscriber

# Create your views here.

def category_count():
    qs = Post.objects.values('categories__title').annotate(Count('categories'))
    return qs
def home(request):
    cat_count = category_count()
    print(cat_count)
    featured_post = Post.objects.filter(Featured=True)
    all_post = Post.objects.order_by('-timestamp')
    popular_post = Post.objects.order_by('view_count')[:2]
    paginator = Paginator(all_post, 2)
    page_req_var = 'page'
    page = request.GET.get(page_req_var)
    try:
        paginated_qs = paginator.page(page)
    except PageNotAnInteger:
        paginated_qs = paginator.page(1)

    except EmptyPage:
        paginated_qs = paginator.page(paginator.num_pages)


    if request.method == "POST":
        email = request.POST["email"]
        new_subscriber= Subscriber()
        new_subscriber.email = email
        new_subscriber.save()
        return redirect('home')


    context ={
        'featured_post':featured_post,
        'all_post': paginated_qs,
        'page_req_var': page_req_var,
        'cat_count':cat_count,
        'popular_post':popular_post
    }
    return render(request,'index.html',context)

def post_view(request,id):
    cat_count = category_count()
    post = get_object_or_404(Post, id=id)
    context={
        'post':post,
        'cat_count':cat_count,
    }
    return render(request,'post.html',context)