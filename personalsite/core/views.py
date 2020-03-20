from django.shortcuts import render
from django.views import View
from .models import Project

# Create your views here.

class index(View):
	def get(self, request):
		project = Project.objects.all()
		my_project = {'projects': project}
		return render(request, 'homepage/index.html', my_project)