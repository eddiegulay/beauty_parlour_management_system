
from django.shortcuts import render, redirect
from guest.models import Appointment, Customer, Service
from guest.views import create_customer, get_page_details
from django.contrib.auth import login, authenticate



def adminPanel_view(request):
    if request.POST:
        name = request.POST["username"]
        pswd = request.POST["password"]
        
        usr = authenticate(request, username = name, password = pswd)
        if usr is not None:
            login(request, usr)
            return redirect("/adminPanel/dashboard")
        else:
            print("*****Wrong vals******")
            
            
    return render(request, "admin/index.html")

def dashboard_view(request):
    customer = Customer.objects.all()
    customers = len(customer)
    
    appointmment = Appointment.objects.all()
    appointmments = len(appointmment)
    accepted = Appointment.objects.filter(accepted = True)
    accptd = len(accepted)
    rejected = Appointment.objects.filter(accepted = False)
    rejects = len(rejected)
    
    service = Service.objects.all()
    services = len(service)
    
    context = {
        'customers': customers,
        'appointmments': appointmments,
        'accepted': accptd,
        'rejects':rejects,
        'services': services
    }
    
    return render(request, "admin/dashboard.html", context)

def add_service_view(request):
    return render(request, 'admin/add-services.html')

def manage_service_view(request):
    return render(request, 'admin/manage-services.html')

def edit_service_view(request):
    return render(request, 'admin/edit-services.html')

def pages_about_us_view(request):
    return render(request, 'admin/about-us.html')

def pages_contact_us_view(request):
    return render(request, 'admin/contact-us.html')

def appointment_all_view(request):
    return render(request, 'admin/all-appointment.html')

def appointment_viewApt_view(request):
    return render(request, 'admin/view-appointment.html')

def appointment_new_view(request):
    return render(request, 'admin/new-appointment.html')

def appointment_accepted_view(request):
    return render(request, 'admin/accepted-appointment.html')

def appointment_rejected_view(request):
    return render(request, 'admin/rejected-appointment.html')

def add_customer(request):
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
    return render(request, 'admin/add-customer.html')

def all_customer(request):
    return render(request, "admin/customer-list.html")

def bw_dates(request):
    return render(request, "admin/bwdates-reports-ds.html")

def bw_dates_report(request):
    return render(request, 'admin/bwdates-reports-details.html')

def invoice_view(request):
    return render(request, 'admin/invoices.html')

def invoice_search_view(request):
    return render(request, 'admin/search-invoices.html')

def appointment_search_view(request):
    return render(request, 'admin/search-invoices.html')