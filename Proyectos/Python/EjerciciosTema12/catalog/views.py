from django.shortcuts import render

from .models import *

def index(request):
    num_movies=Movie.objects.all().count()
    num_instancias=MovieInstance.objects.all().count()
    num_directores=Director.objects.all().count()
    #publico_general=MovieInstance.objects.filter(status__exact='G').count()

    return render(
        request,
        'index.html',
        context={
            'num_movies' : num_movies,
            'num_instancias' : num_instancias,
            'num_directores' : num_directores,
            #'publico_general' : publico_general,
        }
    )