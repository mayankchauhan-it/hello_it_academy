from django.shortcuts import render

# Create your views here.




def home(request):
    print("Home Page")
    return render (request, 'home/homepage.html')


def aboutus(request):
    print("aboutus Page")
    return render(request, "home/aboutus.html")


def projects(request):
    print("porjects Page")
    return render(request, "home/projects.html")


def courses(request):
    print("porjects Page")
    return render(request, "home/courses.html")


def contactus(request):
    print("contactus Page")
    return render(request, "home/contactus.html")


def blog(request):
    print("blog Page")
    return render(request, "home/blog.html")

def login(request):
    print("login Page")
    return render(request, "home/login.html")


def registration(request):
    print("registration Page")
    return render(request, "home/registration.html")
