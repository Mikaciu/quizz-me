from django.shortcuts import render
from django.http import HttpResponse
from quizz_backend.models import Pupil


# Create your views here.
def index(request):
    # pupil_list = Pupil.objects.all()
    # print(pupil_list)
    return HttpResponse("Hello, truitos.")


def pupil_list(request): ...
