

from .models import Post, Category
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404

# Create your views here.

def homepage(request):

    cats = Category.objects.all()
    posts = Post.objects.filter()[0:9]
    # featured = Post.objects.filter(featured=True)
    # latest = Post.objects.order_by('-timestamp')[0:3]
    context= {
        # 'object_list': featured,
        # 'latest': latest,

        'posts':posts,
        'cats':cats,
    }
    return render(request, 'index.html',context)


def contact(request):
    return render(request, 'contact.html')

def team(request):
    return render(request, 'team.html')


# for post detail
def detail(request, slug):


    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    # post= Post.objects.get(slug=slug)
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog-detail.html', {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

    # context = {
    #     'post': post,
    # }
    # return render(request, 'blog-detail.html', context)

# def Blog (request ):
#     cats = Category.objects.get(cat_id = id)
#     posts=Post.objects.filter(category=cats)
#     posts = Post.objects.filter(categories__in=[category])
#     context = {
#         'cat':cats,
#         'posts': posts,
#     }
#     return render(request, 'blog.html')

#categorywise item
def postByCategory(request,slug):
    cats = Category.objects.all()
    cat=Category.objects.get(slug=slug)
    posts=Post.objects.filter(categories_id=cat)
    return render(request, "blog.html",{'cat':cat, 'posts':posts,'cats':cats})