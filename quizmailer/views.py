from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
# Create your views here.
from django.core.mail import send_mail
def home(request):
    return render(request, "home.html")

def send_email(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        print(name, subject, message)

        send_mail(
            subject,
            message,
            "paulkadabo@gmail.com",
            ["hr.villagetech@gmail.com"],
            fail_silently = False,
        )

        return HttpResponseRedirect(reverse("home"))
    else:
        return HttpResponse("Invalid Response")