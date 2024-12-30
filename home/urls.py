from home import views
from django.urls import path

urlpatterns = [
    
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.handlelogin,name='login'),
    path('logout/',views.handlelogout,name='logout'),
    
    
    
    path('about/',views.about,name='about'),
    path('plan/',views.plan,name='plan'),
    path('contact/',views.contact,name='contact'),
    path('pricing/',views.pricing,name='pricing'),
    path('profile/',views.profile,name='profile'),
    
    path('upgrade/',views.upgrade,name='upgrade'),
    path('cancel/', views.cancel, name='cancel'),
    
    path('class/', views.classes, name='class'),
   


]
