from django.shortcuts import render
from django.http import HttpResponse
from .models import Exercise


def home(request):
    return render(request, 'home.html')


def intro(request):
    return render(request, 'intro.html')


def biceps(request):
    return render(request, 'biceps.html')


def triceps(request):
    return render(request, 'triceps.html')


def leg_extension(request):
    return render(request, 'leg-extensions.html')


def side_lateral_raises(request):
    return render(request, 'side-lateral-raises.html')


def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercise-lists.html', {'exercises': exercises})
