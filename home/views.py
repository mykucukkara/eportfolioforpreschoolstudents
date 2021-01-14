import users as users
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

import student
from home.models import Setting, ContactFormu, ContactFormMessage
from student.models import Student, Classroom


def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'page': 'home'}
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)



def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'page': 'referanslar'}
    return render(request, 'referanslar.html', context)

def iletisim(request):

    if request.method == 'POST': #form post edildiyse
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage() # model ile bağlantı kur
            data.name = form.cleaned_data['name'] #formdan bilgi al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save() #formu kaydet
            messages.success(request, "Mesajınız başarı ile gönderilmiştir. Teşekkür ederiz")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting,
               'page': 'iletisim',
               'form': form}
    return render(request, 'iletisim.html', context)

def list_students(request):
    classroom = Classroom.objects.all()
    students = Student.objects.filter(user_id=request.user.id)
    context = {'students' : students,
               'classroom' : classroom,
               'request': request}
    return render(request,'students.html', context)


