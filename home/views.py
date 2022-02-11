from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.


def index(request):
    context = {
        "title": "REST API CRUD APPLICATION",
        "features": "Create, READ, Update, DELETE",

    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page")


def about(request):
    return render(request, 'about.html')


def services(request):
    return HttpResponse("This is Services page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, 'contact.html')
