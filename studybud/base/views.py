from django.shortcuts import render

# Create your views here.

 
def home(request):
    return render(request, 'base/home.html')

def rooms(request,pk):
    return render(request, 'base/room.html')
    
 