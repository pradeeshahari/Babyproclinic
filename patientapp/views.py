from django.shortcuts import render,redirect
from . models import *

# Create your views here.
def clinichome(request):
    return render(request,'patientapp/clinichomepage.html')
def booking(request):
    if request.method=='POST':
        name=request.POST['name']
        mobile=request.POST['mob']
        time=request.POST['time']
        address=request.POST['address']
        loc=request.POST.get('loc')
        spl=request.POST.get('spl')
        doc=request.POST.get('doct')
        msg=request.POST['message']
        
        booking=Booking(name=name,number=mobile,time=time,address=address,location=loc,specialist=spl,doctors=doc,msg=msg,status='waiting')
        booking.save()
        return redirect('patientapp:booking')
    return render(request,'patientapp/patientbooking.html')
def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mob']
        password=request.POST['password']
        patient=Patient(name=name,email=email,number=mobile,password=password)
        patient.save()
        return redirect('patientapp:login')
    return render(request,'patientapp/patientsignup.html')
def Login(request):
    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['password']  
        try:
            patient=Patient.objects.get(email=username,password=password)
        except Patient.DoesNotExist:
            err='invalid email or password'
            return render(request,'patientapp/patientlogin.html',{'err':err})
        return redirect('patientapp:booking')
    return render(request,'patientapp/patientlogin.html')
def master(request):
    return render(request,'patientapp/masterpatient.html')
def aboutus(request):
    return render(request,'patientapp/aboutus.html')
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        msg=request.POST['msg']
        contact=Contact(name=name,email=email,msg=msg)
        contact.save()

    return render(request,'patientapp/contactus.html')
def bookingstatus(request):
        booking=Booking.objects.all()
        return render(request,'patientapp/bookingstatus.html',{'booking':booking})


