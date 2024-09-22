from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Ensure you have home.html in your templates
