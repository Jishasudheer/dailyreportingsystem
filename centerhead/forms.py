from django.forms import ModelForm
from centerhead.models import Course,Batch

from drs.models import MyUser


class CourseAddForm(ModelForm):
    class Meta:
        model=Course
        fields=["course"]

class CourseUpdateForm(ModelForm):
    class Meta:
        model = Course
        fields = ["course"]


class BatchAddForm(ModelForm):
    class Meta:
        model=Batch
        fields=["course","batch","active_status"]

class BatchUpdateForm(ModelForm):
    class Meta:
        model=Batch
        fields=["course","batch","active_status"]



class EmployeeForm(ModelForm):
    class Meta:
        model=MyUser
        fields=["email","phone","role","password"]

class EmployeeUpdateForm(ModelForm):
    class Meta:
        model=MyUser
        fields=["email","phone","role","password"]
