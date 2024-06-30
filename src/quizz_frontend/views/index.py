from django.http import HttpResponse
from quizz_backend.models import Pupil


def index(request):
    # pupil_list = Pupil.objects.all()
    # print(pupil_list)
    return HttpResponse("Hello, truitos.")
