import users as users
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

import student
from home.models import Setting, ContactFormu, ContactFormMessage
from student.models import Student, Classroom, Images, Kazanim


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


def student_detail(request,id,slug):
    #students = Student.objects.all()
    st = Student.objects.get(pk=id)
    images = Images.objects.filter(student_id=id)
    context = {'student': st,
               'images': images}
    return render(request, 'student_detail.html', context)

def material_detail(request,st_id,m_id,slug):
    student = Student.objects.get(pk=st_id)
    image = Images.objects.get(pk=m_id)
    kazanim = Kazanim.objects.filter(student_id=st_id, image_id= m_id)
    context = {'student': student,
               'image': image,
               'kazanim': kazanim
               }
    return render(request, 'materyal.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST': #form post edildiyse
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')

        else:
            messages.warning(request, "Giriş başarısız. Tekrar Deneyiniz.")
            return HttpResponseRedirect('/login')


    return render(request,'login.html')

    # Return an 'invalid login' error message.


