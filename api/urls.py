from .views import classes,contact,plan,getplan
from django.urls import path

urlpatterns = [
    path('contact/',contact),
    path('class/',classes),
    path('plan/',plan),
    path('plan/<str:pk>',getplan),
]
    
