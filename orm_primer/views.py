from django.shortcuts import render

from django.http import HttpResponse

from .models import Post, Operator, Station, Work_in_station


def index(request):
    operators = Operator.objects.all().prefetch_related("stations")
    stations = Station.objects.all()
    working = Work_in_station.objects.all()
    data = []
    for operator in operators:
        operators_stations = Work_in_station.objects.filter(operator=operator)
        stations = [item.station.station_name for item in operators_stations]
        data.append((operator.name, stations))
    return render(
        request, 
        "index.html", 
        {
            "operators": operators,
           # "stations": stations,
           # "working": working,
           # "data": data,
            }
        )


def sql(request):
    data = []
    op1= Operator.objects.get(id=1)
    data.append((op1, op1.station_works.all()))
    return render(
        request,
        "index.html",
        {
            "data": data,
        }
    )


def prefetch(request):
    operators = Operator.objects.all().prefetch_related("stations")
    data = []
    for operator in operators:
        data.append((operator, operator.stations))
    return render(
        request,
        "index.html",
        {
            "data": data,
            "operators": operators,
            }
    )
