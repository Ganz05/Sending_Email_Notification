from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def send_email(request):
    EUFO=userForm()
    EPFO=profileForm()
    d={'EUFO':EUFO,'EPFO':EPFO}
    if request.method=='POST' and request.FILES:
        CUFO=userForm(request.POST)
        CPFO=profileForm(request.POST,request.FILES)
        if CUFO.is_valid() and CPFO.is_valid():
            MCUFO=CUFO.save(commit=False)
            pw=CUFO.cleaned_data['password']
            MCUFO.set_password(pw)
            MCUFO.save()

            MCPFO=CPFO.save(commit=False)
            MCPFO.username=MCUFO
            MCPFO.save()

            send_mail('Registration',
                      'registration is succussfull',
                      'ganesh.poojary2001@gmail.com',
                       [MCUFO.email],
                       fail_silently=True)

            return HttpResponse('Registration Succussfull')
        else:
            return HttpResponse('Invalid data')
    return render(request,'send_email.html',d)
