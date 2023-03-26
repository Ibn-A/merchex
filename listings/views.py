from django.core.mail import send_mail

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from listings.models import Band
from listings.models import Listing

from listings.forms import ContactUsForm

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
    if request.method == 'POST':
        # créer un instance de notre formulaire et le remplir avec les données POST.
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Merchex Contact Us Form',
                message = form.cleaned_data['message'],
                from_email = form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else:
        # ceci doit être une requête GET, donc crée un formulaire vide.
        form = ContactUsForm()

    return render(request,
        'listings/contact.html',
        {'form':form})

def email_sent(request):
    return render(request, 'listings/email-sent.html')