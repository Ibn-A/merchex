from django.core.mail import send_mail

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from listings.models import Band
from listings.models import Listing

from listings.forms import BandForm, ContactUsForm

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id) # pour obtenir le band avec cet id
    return render(request,
            'listings/band_detail.html',
            {'band': band}) # pour passer le groupe(band)au gabarit

def band_create(request):
    if request.method == 'POST':
        # on crée une instance du formulaire qu'on rempli avec les données POST
        form = BandForm(request.POST)

        if form.is_valid():
            # creer un nouveau groupe et sauvegarde dans la bdd
            # redirection vers page de détail du groupe nouvellement crée
            band = form.save()
            return redirect('band-detail', band.id)
    else : 
        form = BandForm()

    return render(request, 
            'listings/band_create.html',
            {'form': form})

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

def ad_create(request):
    return render(request,
        'listings/ad_create.html'
        )

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