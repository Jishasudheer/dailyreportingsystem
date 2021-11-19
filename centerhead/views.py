from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from centerhead.models import Course,Batch
from django.urls import reverse_lazy
from centerhead import forms
from centerhead import forms
from drs.models import MyUser

class AdminHome(TemplateView):
    template_name = "centerhead/adminhome.html"

class CourseAdd(CreateView):
    model = Course
    template_name = "centerhead/addcourse.html"
    form_class = forms.CourseAddForm
    success_url = reverse_lazy("courseadd")
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["courses"]=self.model.objects.all()
        return context

class CourseUpdate(UpdateView):
    model = Course
    template_name = "centerhead/courseupdate.html"
    form_class = forms.CourseUpdateForm
    success_url = reverse_lazy("courseadd")
    pk_url_kwarg = "id"

# class Courses(ListView):
#     model = Course
#     template_name = "course_list"
#     context_object_name = "courses"

class BatchAdd(CreateView):
    form_class = forms.BatchAddForm
    template_name = "centerhead/batches.html"
    success_url = reverse_lazy("batch")
    model = Batch
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["batches"]=self.model.objects.all()
        return context

class BatchUpdateView(UpdateView):
    form_class = forms.BatchAddForm
    model=Batch
    template_name = "centerhead/batchupdate.html"
    success_url = reverse_lazy("batch")
    pk_url_kwarg = "id"


class Employees(CreateView):
    template_name = "centerhead/employees.html"
    form_class = forms.EmployeeForm
    model = MyUser
    success_url = reverse_lazy("employees")
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["employees"]=self.model.objects.all()
        return context
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            employee=form.save(commit=False)
            emp=MyUser.objects.create_user(email=employee.email,phone=employee.phone,role=employee.role,password=employee.password)
            emp.save()
        return redirect("employees")

class EmployeeUpdate(UpdateView):
    model = MyUser
    form_class = forms.EmployeeUpdateForm
    template_name = "centerhead/employeeupdate.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("employees")

def employee_delete(request,id):
    myuser=MyUser.objects.get(id=id)
    myuser.delete()
    return redirect("employees")
