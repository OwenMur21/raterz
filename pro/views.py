from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project, Profile





@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def new_project(request):
    """
    Function that enables one to upload projects
    """
    profile = Profile.objects.all()
    for profile in profile:
        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                pro = form.save(commit=False)
                pro.profile = profile
                pro.user = request.user
                pro.save()
            return redirect('landing')
        else:
            form = ProjectForm()
    return render(request, 'new_pro.html', {"form": form})