from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Exercise

def home(request):
    return render(request, 'home.html')

def intro(request):
    return render(request, 'intro.html')

def exercise_details(request, name):
    exercise = get_object_or_404(Exercise, name__iexact=name)
    return render(request, "exercise_details.html", {"exercise": exercise})

def biceps(request):
    return render(request, 'biceps.html')


def triceps(request):
    return render(request, 'triceps.html')


def leg_extension(request):
    return render(request, 'leg-extensions.html')


def side_lateral_raises(request):
    return render(request, 'side-lateral-raises.html')

def lat_pull_down(request):
    return render(request, '')

def exercise_lists(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercise_lists.html', {'exercises': exercises})

def details(request):
    return HttpResponse
