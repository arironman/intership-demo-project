from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from User.utils import next_url, paginator_stuff
from django.views.decorators.csrf import csrf_exempt

# importing models and forms
from User.models import Post
from django.contrib.auth.models import User
from User.forms import PostForm


# Create your views here.

def show_posts(request):
    posts = Post.objects.all()

    # paginator code
    page_number = request.GET.get('page')
    count = request.GET.get('count')
    posts = paginator_stuff(posts, page_number, count)

    post_form = PostForm()
    params = {
        'posts': posts,
        'title': 'Post',
        'post_form': post_form
    }
    return render(request, 'post/show_posts.html', params)


def login_method(request):
    '''
        login user
    '''
    print(request.method)
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        print(username)
        try:
            # login using email
            user = User.objects.get(email=username)
            user = authenticate(username=user.username, password=password)
        except:
            # login using username
            user = authenticate(username=username, password=password)

        if user == None:
            messages.error(request, 'Invalid Credentials. Try Again!')
            next = request.GET.get('next')
            url = next_url(next)
            return redirect(url)
        else:
            login(request, user)
            next = request.GET.get('next')
            url = next_url(next)
            return redirect(url)
    else:
        return redirect('show_posts')


@login_required()
def logout_method(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out.')
    try:
        next = request.GET.get('next')
        url = next_url(next)
        return redirect(url)
    except:
        return redirect('show_posts')


@csrf_exempt
def available_username(request):
    '''
        Return True if user name is available otherwise False
    '''
    username = request.POST.get('username').lower()
    avaibile = User.objects.filter(username=username).exists()
    if avaibile:
        return HttpResponse(False)
    else:
        return HttpResponse(True)


def signup(request):
    '''
        Handle the signup method.\n
        Handle POST request. No GET request available
    '''
    # Handling the POST request
    if request.method == 'POST':
        username = request.POST['username'].lower()
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email'].lower()
        password = request.POST['password']
        conform_password = request.POST['conform-password']

        # next url
        next = request.GET.get('next')
        redirect_url = next_url(next)

        # checking passwords
        if password != conform_password:
            messages.error(request, 'Oops, Password do not match. Try again!')
            return redirect(redirect_url)

    
        # checking data is not null
        if (username == '' or fname=='' or lname=='' or email==''): 
            messages.error(request, 'Oops, Something went wrong. Try again!')
            return redirect(redirect_url)

        # checking email is registered or not
        registered_email = User.objects.filter(email = email)
        if len(registered_email) > 0:
            messages.error(request, 'Oops, Email is already Registered. Please try with another email.')
            return redirect(redirect_url)

        # creating user
        try:
            user = User.objects.create_user(username=username, email=email, password=password, first_name = fname, last_name=lname)
            user.save()
            messages.success(request, 'Account Created Successfully.')
        except:
            messages.error(request, 'Oops, Something went wrong. Try Again!')
            return redirect(redirect_url)
        
        return redirect(redirect_url)

@login_required()
def add_post(request):
    '''
        This method is used to add post
    '''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid(): 
            post = form.save(commit=False)
            # commit=False means - Don't send this to database yet.

            post.user = request.user # Set the user object here
            post.save() # Now sending object to DB
    return redirect('show_posts')
