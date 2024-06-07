from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def gallery(request):
    return render(request, 'gallery.html')

def tours(request):
    return render(request, 'tours.html')

def bookings(request):
    return render(request, 'bookings.html')

def about(request):
    return render(request, 'about.html')
