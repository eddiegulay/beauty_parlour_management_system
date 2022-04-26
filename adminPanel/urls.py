from django.urls import path
from adminPanel.views import (add_customer, add_service_view, adminPanel_view, all_customer,
    appointment_accepted_view, appointment_all_view, appointment_new_view,appointment_search_view,
    appointment_rejected_view, appointment_viewApt_view, bw_dates, bw_dates_report, dashboard_view,
    edit_service_view, invoice_search_view, invoice_view, manage_service_view, pages_about_us_view, pages_contact_us_view)

urlpatterns = [
    path('', adminPanel_view),
    path('dashboard/', dashboard_view, name = 'dashboard'),
    path('add-service/', add_service_view, name = 'add-service'),
    path('manage-service/',manage_service_view , name = 'manage-service'),
    path('edit-service/', edit_service_view, name = 'edit-service'),
    path('about-us/', pages_about_us_view, name = 'about-us'),
    path('contact-us/', pages_contact_us_view, name = 'contact-us'),
    path('all-appointment/', appointment_all_view, name = 'all-appointment'),
    path('view-appointment/', appointment_viewApt_view, name='view-appointment'),
    path('new-appointment/', appointment_new_view, name='new-appointment'),
    path('accepted-appointment/', appointment_accepted_view, name='accepted-appointment'),
    path('rejected-appointment/', appointment_rejected_view, name='rejected-appointment'),
    path('add-customer/', add_customer, name='add-customer'),
    path('customer-list/', all_customer, name='all-customer'),
    path('bw-dates/', bw_dates, name='bw-dates'),
    path('bw-dates-report/', bw_dates_report, name='bw-dates-report'),
    path('invoice/', invoice_view, name='invoice' ),
    path('invoice-search/', invoice_search_view, name='search-invoice' ),
    path('appointment-search/', appointment_search_view, name = 'search-appointment')
    
]