from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . models import Contact,Plansdetails,Class
from django.contrib.auth.decorators import login_required
from django import forms
# Create your views here.
def home(request):
    bmi = None
    bmi_status = None

    if request.method == 'POST':
        try:
            weight = float(request.POST.get('weight'))
            height = float(request.POST.get('height'))

            if weight > 0 and height > 0:
                bmi = round(weight / (height ** 2), 2)

                if bmi < 18.5:
                    bmi_status = "You are underweight. Consider consulting a nutritionist."
                elif 18.5 <= bmi < 24.9:
                    bmi_status = "You have a normal weight. Keep up the great work!"
                elif 25 <= bmi < 29.9:
                    bmi_status = "You are overweight. A balanced diet and regular exercise can help."
                else:
                    bmi_status = "You are in the obese category. Please consult a healthcare provider for advice."
            else:
                bmi_status = "Please enter positive values for weight and height."

        except ValueError:
            bmi_status = "Invalid input. Please enter numeric values for weight and height."
    print(bmi,bmi_status)
    return render(request,"home.html",{"bmi":bmi,"bmi_status":bmi_status})
def signup(request):
    if request.method == "POST":
       
        email=request.POST.get('email')
        password=request.POST.get('pass1')
        confirm_password=request.POST.get('pass2')
        if len(password) != 6:
            messages.warning(request,"Please enter password of length 6 digits or letters ")
            return redirect('signup')
        if password != confirm_password:
            messages.warning(request,"password is not matching")
            return render(request,"signup.html")
        try:
            
            if User.objects.get(username=email):
                messages.info(request,"Email already exist")
                return render(request,"signup.html")
        except Exception as identifier:
            pass
        user= User.objects.create_user(email,email,password)
        user.save()
        return redirect('login')
    return render(request,"signup.html")
def handlelogin(request):
    if request.method == "POST":
        user_name=request.POST.get('email')
        password=request.POST.get('pass1')
        user=authenticate(username=user_name,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.warning(request,"Invalid credentials")
            return redirect("login")
    return render(request,"login.html")
    

def handlelogout(request):
    logout(request)
    messages.success(request,"Logout successfully")
    return redirect("login")


def about(request):
    return render(request,"about.html")

def plan(request):
    return render(request,"plan.html")


def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone')
        subject=request.POST.get('subject')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phoneno=phone_no,subject=subject,description=desc)
        contact.save()
        messages.success(request,"We will reach you soon")
        return redirect('/')
    return render(request,"contact.html")


@login_required(login_url='/login/')
def pricing(request):
    
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneno=request.POST.get('phone')
        plan=request.POST.get('plan')
        sdate=request.POST.get('sdate')
        duration=request.POST.get('duration')
        payment=request.POST.get('payment')
        password=request.POST.get('password')
        try:
            
            person = Plansdetails.objects.filter(email=email)
            if not person.exists():
                user = authenticate(username=email, password=password)
                if user is not None:                  
                    plans = Plansdetails(name=name, email=email, phoneno=phoneno, plan=plan,
                                         sdate=sdate, duration=duration, payment=payment)
                    plans.save()
                    messages.success(request, "Plan registered successfully!")
                    return redirect('plan')
                else:
                    messages.warning(request, "Invalid email or password. Please try again.")
                    return redirect('pricing')
            else:
                
                messages.warning(request, "Email already registered with a plan.")
        except Exception as identifier:
            
            messages.error(request, "An error occurred. Please try again.")
   
    return render(request,'pricing.html')
        

@login_required(login_url='/login/')
def upgrade(request):
    user = request.user
    try:
        plan = Plansdetails.objects.get(user=user)
    except Plansdetails.DoesNotExist: 
        plan = None
    if request.method == 'POST':
        plan.name=request.POST.get('name')
        plan.email=request.POST.get('email')
        plan.phoneno=request.POST.get('phone')
        plan.plan=request.POST.get('plan')
        plan.sdate=request.POST.get('sdate')
        plan.duration=request.POST.get('duration')
        plan.payment=request.POST.get('payment')
        plan.save()
        messages.success(request,"Your Plan Upgraded Successfully")
        return redirect('profile')
    context={"plan":plan}
    return render(request, 'upgradeplan.html',context)


def profile(request):
    
    user = request.user
    try:
        plan_details = Plansdetails.objects.get(user=user)
    except Plansdetails.DoesNotExist: 
        plan_details = None
    context = {
        'user': user,
        'plan_details': plan_details
    }
    return render(request,'profile.html',context)



def cancel(request):
    user = request.user
    plan = Plansdetails.objects.filter(user=user)

    if plan:
        plan.delete()  
        messages.success(request, "Your plan has been successfully canceled.")
    else:
        messages.warning(request, "No active plan found to cancel.")
    
    return redirect('profile')  


def classes(request):
    post=Class.objects.all()
    context={"post":post}
    return render(request,"class.html",context)

