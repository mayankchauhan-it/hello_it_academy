from django.shortcuts import render

# Create your views here.




def home(request):
    print("Home Page")
    return render (request, 'home/homepage.html')