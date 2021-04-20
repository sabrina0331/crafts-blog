from django.shortcuts import render
from login.models import User,Blog

# Create your views here.
def index(request):
    # user =User.object.all()
    # context = {
    #     'user': user
    # }
    return render(request, 'blogs/main.html')

def userBlogs(request):
    user = request.user
    print(user)
    return render(request,'blogs/userBlogs.html')

def createNew(request):
    return render(request,'blogs/createNew.html')