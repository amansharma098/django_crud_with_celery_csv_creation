from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student,ApiCount


def student_list(request):
    if request:
        api_save = ApiCount(api_url=request)
        api_save.save()
    context = {'student_list': Student.objects.all()}
    return render(request, "student_register/student_list.html", context)


def student_form(request, id=0):
    if request:
        api_save = ApiCount(api_url=request)
        api_save.save()
    if request.method == "GET":
        if id == 0:
            form = StudentForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request, "student_register/student_form.html", {'form': form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST,instance= student)
        if form.is_valid():
            form.save()
        return redirect('/student/list')


def student_delete(request,id):
    if request:
        api_save = ApiCount(api_url=request)
        api_save.save()
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('/student/list')