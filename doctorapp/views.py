from django.shortcuts import render,redirect
from patientapp.models import *
from babyapp.models import *
from django.http import JsonResponse

# Create your views here.

def doctorlogin(request):
    if request.method=='POST':
        username= request.POST['user']
        password= request.POST['Pass1']
        log_exist=Adddoctor.objects.filter(username=username,password=password).exists()
        if log_exist:
            log=Adddoctor.objects.get(username=username,password=password)
            return redirect('doctorapp:log')
        else:

           return render(request,'doctorapp/doctorloginpage.html')
    return render(request,'doctorapp/doctorloginpage.html')
def appointment(request):
    pdts=Booking.objects.all()
    return render(request,'doctorapp/doctorappointment.html',{'booking':pdts})
def deletebooking(request,xid):
    Booking.objects.get(id=xid).delete()
    return redirect ('doctorapp:appoint')
def list(request):
    sdts=Patient.objects.all()
    return render(request,'doctorapp/patientlist.html',{'patient':sdts})
def deletelist(request,lid):
    Patient.objects.get(id=lid).delete()
    return redirect ('doctorapp:list')
def status_update(request,xid):
    p_status= Booking.objects.get(id=xid)
    if p_status.status=='not confirmed':
        Booking.objects.filter(id=xid).update(status='confirmed')
    else:
        Booking.objects.filter(id=xid).update(status='not confirmed')
    return redirect('doctorapp:appoint')
def master(request):
    return render(request,'doctorapp/masterpage.html')