from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band
from listings.models import Listing

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id) # pour obtenir le band avec cet id
    return render(request,
            'listings/band_detail.html',
            {'band': band}) # pour passer le groupe(band)au gabarit

def about(request):
    return render(request, 'listings/about.html')

def ad_list(request):
    ads = Listing.objects.all()
    return render(request, 'listings/ad_list.html',{'ads': ads})

def ad_detail(request, id):
    ad = Listing.objects.get(id=id)
    return render(request, 
        'listings/ad_detail.html',
        {'ad': ad})

def contact(request):
    return render(request, 'listings/contact.html')