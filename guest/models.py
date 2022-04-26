from django.db import models
from django.contrib.auth.models import User
import random

# random id generator
def get_id(size):
    size = int(size)
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','@','#','$','&']
    randId = ""
    for i in range(1, size):
        randId += chars[random.randint(0, len(chars))]
        
    return randId


# Services
class Service(models.Model):
    ServiceName = models.CharField(max_length=200)
    Cost = models.FloatField()
    CreationDate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.ServiceName


# appointments
class Appointment(models.Model):
    AptNumber = models.CharField(max_length=80)
    Name = models.CharField(max_length= 120)
    Email = models.EmailField(max_length=120)
    PhoneNumber = models.CharField(max_length=15)
    AptDate = models.DateTimeField(auto_now=True)
    Service = models.ForeignKey(to = Service, on_delete=models.CASCADE)
    ApplyDate = models.DateTimeField(auto_now=True)
    AptStrTime = models.CharField(max_length=30, default="")
    Remark = models.CharField(max_length=250, default = "")
    Status = models.CharField(max_length=50, default = "")
    accepted = models.BooleanField(default=False)
    Waiting = models.BooleanField(default=False)
    Done = models.BooleanField(default=False)
    
# customers
class Customer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    PhoneNumber = models.CharField(max_length = 15)
    CreationDate = models.DateTimeField(auto_now=True)
    
    

# invoice
class Invoice(models.Model):
    UserId = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    ServiceId = models.ForeignKey(to=Service, on_delete=models.CASCADE)
    BillingId = models.CharField(max_length=10)
    PostingDate = models.DateTimeField(auto_now=True)
    
# company contact details    
class Contact(models.Model):
    Email = models.EmailField(max_length=200)
    PhoneNumber = models.CharField(max_length=15)
    Location = models.CharField(max_length=200)
    MapLocation = models.CharField(max_length=500)

# page ad like descriptions    
class PageDescription(models.Model):
    company_name = models.CharField(max_length=120, default = "Beauty Parlour")
    front_one = models.CharField(max_length=500)
    front_two = models.CharField(max_length=500)
    front_title_one = models.CharField(max_length=500)
    front_title_two = models.CharField(max_length=500)
    footer_one = models.CharField(max_length=500)
    about_details = models.CharField(max_length= 500, default="")
    service_details = models.CharField(max_length=500, default = "")
    contact_details = models.CharField(max_length=500, default = "")
    
    
    
