from .models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from profiles.models import UserProfile
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog(request):
    """ Renders all post"""
    query = None
    all_post = Post.objects.all()
    page_number = request.GET.get('page')
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('blog'))
            queries = Q(title__icontains=query) | Q(content__icontains=query)
            all_post = all_post.filter(queries)
    # 3 items per page
    paginator = Paginator(all_post, 3)
    try:
        post = paginator.page(page_number)
        # This can raise an error
    except PageNotAnInteger:
        # If the page number is not an integer
        # show the first page
        post = paginator.page(1)
    except EmptyPage:
        # If the page number is out of range
        # show the last page
        post = paginator.page(paginator.num_pages)

    context = {
        'post': post,
        'search_term': query,
    }
    return render(request, 'blog/blog.html', context)


@login_required
def post_detail(request, post_id):
    """ Renders the post details """
    profile = UserProfile.objects.get(user=request.user)
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)
    new_comment = None
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
    context = {
        'post': post,
        'profile': profile,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def add_post(request):
    """ Add a post to the Blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Fit & Lift owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            created_updated(Post, request)
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request,
                           'Failed to add post. The form is not valid.')
    else:
        form = PostForm()
    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    """ Edit a post in the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request,
                           'Failed to update post. The form is not valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ Delete a post from the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Fit & Lift staff can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))
