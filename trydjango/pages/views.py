from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print (request.user)
    print (args, kwargs)
    # return HttpResponse("<h1>Hello World!</h1>") # string of HTML code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
    # return HttpResponse("<h2>Contact Info Page</h2>")

def about_view(request, *args, **kwargs):
    my_contacts = {
        "my_text": "This is about me.",
        "my_number": 123,
        "my_list": ["First", "Second", 3]
    }
    return render(request, "about.html", my_contacts)
    # return HttpResponse("<h1>About Page</h1>")