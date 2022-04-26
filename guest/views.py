from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from guest.models import Customer
from.models import (get_id, Appointment, Service, PageDescription, Contact, Customer )


def home_view(request):
    
    context = {
        'marketing': get_page_details(),
        'contacts': get_contact_details(),
        'services': get_service_details()
    }
    
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        service = request.POST['service']
        apt_time = request.POST['atime']
        apt_date = request.POST['adate']
        phone = request.POST['phone']

        if create_appointment(name, email, phone, service, apt_time + apt_date):
            return redirect("/thanks")
        
        
    return render(request, "guest/home.html", context)


def about_view(request):
    context = {
        'marketing': get_page_details(),
        'contacts': get_contact_details()
    }
    return render(request, "guest/about.html", context)


def contact_view(request):
    context = {
        'marketing': get_page_details(),
        'contacts': get_contact_details()
    }
    return render(request, "guest/contact.html", context)


def service_view(request):
    context = {
        'marketing': get_page_details(),
        'contacts': get_contact_details(),
        'services': get_service_details()
    }
    return render(request, "guest/services.html", context)


def thanks_view(request):
    context = {
        'marketing': get_page_details(),
        'contacts': get_contact_details()
    }
    return render(request, "guest/thank-you.html", context)


def login_view(request):
    if request.POST:
        name = request.POST["name"]
        pswd = request.POST["pswd1"]
        
        usr = authenticate(request, username = name, password = pswd)
        if usr is not None:
            login(request, usr)
            return redirect("/home")
        else:
            print("*****Wrong vals******")
        
    context = {
        'marketing': get_page_details(),
        'showNav': True
    }
    
    return render(request, "guest/login.html", context)


def instant_logout(request):
    logout(request)
    return redirect("/login")


def signup_view(request):
    if request.POST:
        usr_name = request.POST['name']
        usr_email = request.POST['email']
        usr_phone = request.POST['phone']
        usr_pass = request.POST['pswd1']
        create_customer(usr_name, usr_email, usr_phone, usr_pass)
        
    context = {
        'marketing': get_page_details(),
        'showNav': True
    }
    return render(request, "guest/signup.html", context)


# processors
def get_page_details():
    marketing = PageDescription.objects.all()
    return marketing


def get_contact_details():
    contacts = Contact.objects.all()
    return contacts


def get_service_details():
    services = Service.objects.all()
    return services


def create_appointment(name, email, phone, service, apt_date):
    srvc = Service.objects.get(id = int(service))
    apt = Appointment.objects.create(AptNumber = get_id(5), Name = name, Email = email, PhoneNumber = phone, Service = srvc, AptStrTime = apt_date)
    apt.save()
    
    return True


def create_customer(name, email, phone, password):
    try:
        if_exist = User.objects.get(username = name)
        print("User Exist")
    except:
        new_user = create_new_user(name, email, password)
        new_customer = Customer.objects.create(user = new_user, PhoneNumber = phone)
        new_customer.save()
        return redirect("/login")
    
    
def create_new_user(name, email, password):
    new_user = User.objects.create_user(username = name, password = password, email = email)
    new_user.save()
    return new_user

