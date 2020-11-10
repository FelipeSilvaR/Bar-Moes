from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "index.html", {'titulo': 'Nuestros productos son lo mejor'}) 

def contacto(request):
    return render(request, "contacto.html")

