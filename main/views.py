from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        "app_name": "KickMart",   # nama aplikasi
        "user_name": "Deslee Jever Phillipa",  
        "class_name": "PBP D",    
    }
    
    return render(request, "main.html", context)  
