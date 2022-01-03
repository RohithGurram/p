from django.db import models
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView
from .models import Project
def HomeView(request):
    return render(request,'home.html')

def ContactView(request):
    return render(request,'contact.html')

class ProjectView(ListView):
    model=Project
    template_name='project.html'
    context_object_name="project"
class ProjectDetailView(DetailView):
    model=Project
    template_name='project_detail.html'
    fields='__all__'


