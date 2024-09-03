from django.shortcuts import render, redirect
from django.contrib import messages

# import todo form and models

from .forms import TodoForm,LoginForm,SignUpForm
from .models import Todo,User

###############################################


def index(request):

    username = request.session.get('username')
    if not username:
        return redirect('login')
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()
    page = {
        "username":username,
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Invalid form')
    else:
        form = SignUpForm()
    page = {
        "forms": form,
        "title": "Sign Up",
    }
    return render(request, 'signup.html', page)
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form["username"].value()
            password = form["password"].value()
            try:
                userDetails = User.objects.get(username=username,password=password)
                request.session['username'] = username
                return redirect('todo')
            except User.DoesNotExist:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    page = {
        "forms": form,
    }
    return render(request, "login.html",page)

def logout(request):
    request.session.flush()
    return redirect('login')

### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')

def viewDetails(request, item_id):
    item = Todo.objects.get(id=item_id)
    page = {
        "item": item,
        "title": "TODO DETAILS",
    }
    return render(request, 'todo/details.html', page)
