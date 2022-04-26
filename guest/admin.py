from django.contrib import admin
from.models import (Customer, Appointment, Service, Invoice,PageDescription, Contact)

# model admins
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'PhoneNumber')
    
    
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('ServiceName', 'Cost')
    
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('AptNumber', 'Name','Email', 'PhoneNumber', 'Service', 'ApplyDate', 'Done', 'Waiting')
    
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('UserId', 'ServiceId', 'BillingId', 'PostingDate')
    
    
# admin site register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Appointment,AppointmentAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(PageDescription)
admin.site.register(Contact)