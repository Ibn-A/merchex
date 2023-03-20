from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello django ! </h1>
        <p>Mes groupes préférés sont :</p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
    """)

def about(request):
    return HttpResponse('<h1> A propos </h1> <p>Nous adorons merchex</p>')

def listings(request):
    listings = Listing.objects.all()
    return HttpResponse(f"""
        <h1>Liste des annonces</h1>
        <ul>
            <li>{listings[0].title}</li>
            <li>{listings[1].title}</li>
        </ul>
    """)

def contact(request):
    return HttpResponse('<h1>Et si nous gardions le contact !</h1>')