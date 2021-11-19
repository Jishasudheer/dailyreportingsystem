from django.urls import path
from centerhead import views


urlpatterns=[
    path("",views.AdminHome.as_view(),name="adminhome"),
    path("courses/add",views.CourseAdd.as_view(),name="courseadd"),
    path("course/change/<int:id>",views.CourseUpdate.as_view(),name="courseupdate"),
    path("batches/add",views.BatchAdd.as_view(),name="batch"),
    path("batch/update/<int:id>",views.BatchUpdateView.as_view(),name="batchupdate"),
    path("employees",views.Employees.as_view(),name="employees"),
    path("employee/update/<int:id>",views.EmployeeUpdate.as_view(),name="employeeupdate"),
    path("employees/delete/<int:id>",views.employee_delete,name="employeedelete")
]