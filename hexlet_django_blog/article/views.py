from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    name, course, group = "Иннокентий", "3", "3103-О"
    return render(
        request,
        'articles/index.html',
        context={'name': name,
                 'course': course,
                 'group': group},
    )