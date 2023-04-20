from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def index(request):
    about = About.objects.last
    project = Projects.objects.all()
    serv = Services.objects.all()
    friend = Friends.objects.all()
    blog = Blog.objects.all()
    context = {
        'about': about,
        'project': project,
        'friend': friend,
        'blog': blog,
        'serv': serv
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        Contact.objects.create(email=email, name=name, text=comment)

    return render(request, 'index.html', context)



def project_detail(request, pk):
    contex = {
        'project': Projects.objects.get(id=pk),
    }
    return render(request, 'project_detail.html', contex)




def blog_detail(request, pk):
    contex = {
        'blog': Blog.objects.get(id=pk),
    }
    return render(request, 'blog_detail.html', contex)