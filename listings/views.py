from django.core.mail import send_mail

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from listings.models import Band
from listings.models import Listing

from listings.forms import ListingForm, BandForm, ContactUsForm

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

def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe mis a jour
            return redirect('band-detail', band.id)
    else:

        form = BandForm(instance=band) # on pré-rempli le formulaire avec les données du groupe existant.

    return render(request, 
        'listings/band_update.html',
        {'form':form})

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
    if request.method == 'POST':
        form = ListingForm(request.POST)

        if form.is_valid():
            ad = form.save()
            return redirect('ad-detail', ad.id)
    else :
        form = ListingForm()
        
    return render(request,
        'listings/ad_create.html',
        {'form': form})

def ad_update(request, id):
    ad = Listing.objects.get(id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=ad)
        if form.is_valid():
            # on sauvegarde l'annonce dans la BDD
            form.save()
            # et on redirige vers la page détaillé de l'annonce modifié
            return redirect('ad-detail', ad.id)
    else :
        
        form = ListingForm(instance = ad)

    return render(request, 
            'listings/ad_update.html',
            {'form': form})

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