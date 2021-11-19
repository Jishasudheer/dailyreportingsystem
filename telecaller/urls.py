from django.urls import path
from telecaller import views
from django.views.generic import TemplateView


urlpatterns=[
    path("login",views.LoginView.as_view(),name="loginview"),
    path("logout",views.logout_view,name="logoutview"),
    path("enquiries/add",views.EnquiryCreate.as_view(),name="enquirycreate"),
    path("home",TemplateView.as_view(template_name="telecaller/telecallerhome.html"),name="telecallerhome"),
    path("enquries/update/<int:id>",views.EnquiryUpdate.as_view(),name="enquiryupdate"),
    path("enquries/list",views.Enquirylist.as_view(),name="enquirylist"),
    path("enquiries/followups",views.ViewFolloups.as_view(),name="viewfollowups"),
    path("reports/count",views.ViewReport.as_view(),name="viewreport")
]