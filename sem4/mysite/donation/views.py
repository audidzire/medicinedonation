from django.shortcuts import render,redirect
from .models import m_donation
from django.core.mail import send_mail
from twilio.rest import Client

from django.http import HttpResponse
from django.contrib import messages
#from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
User = get_user_model()
def index(request):
    total_donations = m_donation.objects.count()
    total_users= User.objects.count()
    return render(request, "index.html", {'DonationCount': total_donations, 'TotalUsers':total_users})


def donations(request):
    all_donations = m_donation.objects.all()
    return render(request, "donations.html", {'Donations': all_donations})


def add_donation(request):
    if request.method == 'POST':
        brand_name = request.POST['brand_name']
        generic_name = request.POST['generic_name']
        type = request.POST['type']
        quantity = request.POST['quantity']
        manufacturing_date = request.POST['mdate']
        expiry_date = request.POST['edate']
        description = request.POST['description']


        user_id_id = request.user.id


        donation_obj = m_donation(brand_name=brand_name, generic_name=generic_name, type=type, quantity=quantity,
                                  manufacturing_date=manufacturing_date, expiry_date=expiry_date,
                                  description=description, user_id_id=user_id_id)
        donation_obj.save()
        messages.info(request, 'Donated Successfully')
        return render(request, "index.html")
    else:
        messages.info(request, 'Something went wrong')
        return render(request, "index.html")


def requestinfo(request):
    if request.method == 'POST':
        id = request.POST['id']
        info = m_donation.objects.filter(id=id)

        if request.user.is_active:

            user_name = request.user.full_name
            user_mobile = request.user.mobile_number
            user_city = request.user.city
            for i in info:
                uid = i.user_id_id

            user_info = User.objects.filter(id=uid)

            from_email_id = request.user.email
            for j in user_info:
                to_email_id = j.email
                to_mobile_number = j.mobile_number
            send_mail(
                'Request Medicines', #subject
                user_name +" " + 'has requested for'+" " +i.brand_name + " " + 'medicines' +' '
                + '\nContact Details :' + user_mobile + " " +'\nCity :' + " "
                + user_city
            , #message
                from_email_id, #from email
                [to_email_id], #to email
                fail_silently=False,

            )
            account_sid = 'AC94637694e7f6cdddd3acbf0794baf659'
            auth_token = 'fc8b2d1ac220980b8b647385834ea295'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                body=user_name +" " + 'has requested for'+" " +i.brand_name + " " + 'medicines' +' '
                + '\nContact Details :' + user_mobile + " " +'\nCity :' + " "
                + user_city,
                from_='+12083579681',
                to='+91' + to_mobile_number,
            )

            print(message.sid)
            return render(request, 'requestinfo.html', {'Donationinfo': info, 'Information': user_info})
        else :
             return render(request, 'requestinfo.html', {'Donationinfo': info})
       # return render(request, 'requestinfo.html' )
    #return redirect(request,'donations')

def mydonations(request):
    current_user = request.user
    c_user_id = current_user.id
    my_donations = m_donation.objects.filter(user_id_id=c_user_id)
    return render(request, "mydonations.html", {'MyDonations': my_donations})

def edit_mydonations(request):
    if request.method == 'POST':
        r_id = request.POST['id']
        dinfo = m_donation.objects.filter(id=r_id)
        return render(request, "edit_mydonations.html", {'EditDonations': dinfo})



def update_mydonations(request):
    if request.method == 'POST':
        d_id = request.POST['d_id']
        brand_name = request.POST['e_brand_name']
        generic_name = request.POST['e_generic_name']
        type = request.POST['e_type']
        quantity = request.POST['e_quantity']
        manufacturing_date = request.POST['e_mdate']
        expiry_date = request.POST['e_edate']
        description = request.POST['e_description']
        availability_status = request.POST['e_available']
        user_id_id = request.user.pk

        update_donation_obj = m_donation.objects.filter(id=d_id).update(id=d_id,brand_name=brand_name, generic_name=generic_name, type=type, quantity=quantity,
                                  manufacturing_date=manufacturing_date, expiry_date=expiry_date,
                                  description=description, user_id_id=user_id_id, availability_status=availability_status)

        return redirect('/mydonations')


