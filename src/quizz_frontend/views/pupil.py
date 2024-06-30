from django.http import HttpResponse
from quizz_backend.models import Pupil


def list(request):
    return HttpResponse("")


def pupil(_, uid: int):
    try:
        current_pupil = Pupil.objects.get(pk=uid)
        return HttpResponse(f"{current_pupil.first_name} {current_pupil.last_name}")
    except Exception as e:
        return HttpResponse(content=e, status=404)


def pupil_list(_):
    pupil_list = []
    for current_pupil in Pupil.objects.all():
        pupil_list.append(f"{current_pupil.first_name} {current_pupil.last_name}")

    return HttpResponse("".join(pupil_list))
