from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from . models import *
from patientapp.models import Contact
from django.http import JsonResponse

# Create your views here.
def indexhome(request):
    if request.method=='POST':
        adminuser=request.POST['user']
        adminpassword=request.POST['pass1']
        user=authenticate(request,username=adminuser,password=adminpassword)
        if user is not None:
            login(request,user)  
            return redirect('babyapp:portal')          

            
        else :
            return render (request,'babyapp/adminloginpage.html',{'msg':'invalid username or password'})

            

    return render(request,'babyapp/adminloginpage.html')
def adminportal(request):
    return render(request,'babyapp/adminportal.html')
def doctorpanel(request):
    return render(request,'babyapp/bdoctorpanel.html')
def adddoc(request):
    if request.method=='POST':
          username=request.POST['username']
          password=request.POST['password']
          doc_id=request.POST['roll_no']
          age=request.POST['age']
          image=request.FILES['image']
          gender=request.POST.get('gender')
          number=request.POST['no']


          adddoc=Adddoctor(username=username,password=password,doc_id=doc_id,age=age,image=image,gender=gender,number=number)
          adddoc.save()
          return render(request,'babyapp/doctoraddpage.html',{'para':'doctors added successully'})
    else:
          return render (request,'babyapp/doctoraddpage.html')
def updatedoc(request):
    doc1=Adddoctor.objects.all()
    return render(request,'babyapp/doctorupdatepage.html',{'doc2':doc1})

def viewdoc(request):
    srds=Adddoctor.objects.all()
    
    return render(request,'babyapp/doctorviewpage.html',{'doc':srds})
def deletedoctor(request,iid):
    Adddoctor.objects.get(id=iid).delete()
    return redirect('babyapp:view')
def master(request):
    return render(request,'babyapp/master.html')

def P_contact(request):
    contact_msg=Contact.objects.all()

    return render(request,'babyapp/p_contact.html',{'msg':contact_msg})
def deletecontact(request,mid):
    Contact.objects.get(id=mid).delete()
    return redirect('babyapp:contact')
def upt(request,sid):
    doc= Adddoctor.objects.get(id=sid)
    if request.method=='POST':
          username=request.POST['username']
          password=request.POST['password']
          roll=request.POST['roll_no']
          age=request.POST['age']
        #   image=request.FILES['image']
          gender=request.POST['gender']
          number=request.POST['no']
          doc.username=username
          doc.password=password
          doc.doc_id=roll
          doc.age=age
          doc.gender=gender
          doc.number=number
          doc.save()
          return redirect('babyapp:update')
 
    return render(request,'babyapp/update.html',{'s_update':doc})






