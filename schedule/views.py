from django.http import HttpResponse
from django.shortcuts import render

from .models import Subject


def index(request):
    # Test value
    subject = Subject.objects.all()[0]

    context = {'subject': subject}

    return render(request, 'schedule/index.html', context)


def about(request):
    return HttpResponse("About")


def contact(request):
    return HttpResponse("Contact")
