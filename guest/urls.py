from django.urls import path
from django.urls import path
from .views import (about_view, contact_view, home_view, instant_logout, login_view, service_view, signup_view, thanks_view)


urlpatterns = [
    path('', home_view),
    path('login/', login_view),
    path('logout/', instant_logout),
    path('signup/', signup_view),
    path('home/', home_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('service/', service_view),
    path('thanks/', thanks_view)
]