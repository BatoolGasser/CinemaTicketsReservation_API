from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest, Movie, Reservation

# Create your views here.


# 1 without rest framework and no model query (FBV)
def no_rest_no_model(request):
    guests = [
        {
            'id': 1,
            'name': 'omar',
            'mobile': 71224354
        },
        {
            'id': 2,
            'name': 'batool',
            'mobile': 595965556
        }
    ]
    return JsonResponse(guests, safe=False)


# 2 no rest framework and from model
def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        'guests': list(data.values('name', 'mobile'))
    }
    return JsonResponse(response)

