from django.shortcuts import render

from django.http import HttpResponse

from .models import Post, Operator, Station, Work_in_station


def index(request):
    operators = Operator.objects.all()
    stations = Station.objects.all()
    working = Work_in_station.objects.all()
    return render(
        request, 
        "index.html", 
        {
            "operators": operators,
            "stations": stations,
            "working": working,
            }
        )
