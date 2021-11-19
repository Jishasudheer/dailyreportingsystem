from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,UpdateView,ListView
from telecaller import forms
from telecaller.models import Enquiries

# Create your views here.
from django.contrib.auth import authenticate,logout,login
from django.urls import reverse_lazy
from datetime import date


class LoginView(TemplateView):
    # template_name = "telecaller/login.html"
    # form=forms.LoginForm
    # success_url=reverse_lazy("employees")
    def get(self,request,*args,**kwargs):
        form = forms.LoginForm()
        return render(request, "telecaller/login.html", {"form": form})
    def post(self,request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                if request.user.role=='telecaller':
                    return render(request,"telecaller/telecallerhome.html")
                else:
                    return redirect("employees")
def logout_view(request):
    logout(request)
    return redirect("loginview")
#telecaller/enquiries/

class EnquiryCreate(CreateView):
    model = Enquiries
    form_class = forms.EnquiryForm
    template_name = "telecaller/addenquiry.html"
    success_url = reverse_lazy("enquirylist")
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            enquiry=form.save(commit=False)
            enquiry.created_by=request.user
            enquiry.save()
            return redirect("enquirylist")

class EnquiryUpdate(UpdateView):
    model = Enquiries
    form_class = forms.EnquiryUpdateForm
    template_name = "telecaller/updateenquiry.html"
    success_url = reverse_lazy("enquirylist")
    pk_url_kwarg = "id"


class Enquirylist(ListView):
    model = Enquiries
    template_name = "telecaller/enquries_list.html"
    context_object_name = "enquiries"
    def get_queryset(self):
        user=self.request.user
        return self.model.objects.filter(created_by=user)

class ViewFolloups(ListView):
    model = Enquiries
    template_name = "telecaller/enquiryfollowups.html"
    context_object_name = "followups"
    def get_queryset(self):
        user=self.request.user
        return self.model.objects.filter(created_by=user,followupdate=date.today())
class ViewReport(ListView):
    model = Enquiries
    template_name = "telecaller/viewreport.html"
    context_object_name = "reports"
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        user = self.request.user
        enp_count = self.model.objects.filter(created_by=user, enquirydate=date.today()).count()
        admission_count = self.model.objects.filter(created_by=user, enquirydate=date.today(), status="admited").count()
        context["reports"]=enp_count
        context["admission_count"]=admission_count
        form=forms.DateFilterForm()
        context["form"]=form
        return context
    def post(self,request,*args,**kwargs):
        form=forms.DateFilterForm(request.POST)
        if form.is_valid():
            fromdate=form.cleaned_data["from_date"]
            todate=form.cleaned_data["to_date"]
            print("fromdate",fromdate)
            admissioncount=self.model.objects.filter(created_by=self.request.user,enquirydate__gte=date(fromdate),enquirydate__lte=date(todate)).count()
            print(admissioncount)
            return redirect("viewreport")


