from django.urls import path

from .views import index, pupil


urlpatterns = [
    path("", index.index, name="index"),
    path("pupil/", pupil.pupil_list),
    path("pupil/<int:uid>/", pupil.pupil),
]
