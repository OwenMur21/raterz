from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, ProfileForm
from .models import Project, Profile





@login_required(login_url='/accounts/login/')
def index(request):
    projects = Project.objects.all().order_by('-posted_on')
    return render(request, 'index.html', locals())


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


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    """
    Function that enables one to edit their profile information
    """
    current_user = request.user
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('landing')
    else:
        form = ProfileForm()
    return render(request, 'profile/edit-profile.html', {"form": form,})


@login_required(login_url='/accounts/login/')
def view_project(request, id):
    """
    Function that enables one to view specific project
    """
    title = "View Project"
    project = Project.get_pro_by_id(id=id)
    return render(request, 'view_project.html', locals())




