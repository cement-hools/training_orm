from random import random

from django.shortcuts import render

from django.http import HttpResponse

from .models import Post, Operator, Station, Work_in_station


def index(request):
    operators = Operator.objects.all().prefetch_related("stations").order_by('?')
    stations = Station.objects.all()
    stations_names = [station.name for station in stations]
    data = {}
    for operator in operators:
        data[operator] = operator.stations.all()
    rotation = {}
    for station in stations:
        for operator, operator_stations in data.items():
            if station in operator_stations and operator not in rotation.values():
                    rotation[station] = operator
                    break
            else:
                rotation[station] = "absent"

    return render(
        request,
        "index.html",
        {
            "data": data,
            "operators": operators,
            "stations": stations,
            "stations_names": stations_names,
            "rotation": rotation,
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
    stations = list(Station.objects.all())
    data = []
    for operator in operators:
        data.append((operator, operator.stations))
    return render(
        request,
        "index.html",
        {
            "data": data,
            "operators": operators,
            "stations": stations,
            }
    )
