from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.urls import reverse
# Create your views here.

def contacto(request):
    formulario = ContactForm()
    if request.method == "POST":
        formulario = ContactForm(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get("nombre",'')
            correo = request.POST.get('correo','')
            telefono = request.POST.get('telefono','')
            mensaje = request.POST.get('mensaje','')
            email = EmailMessage("Le han contactado",
            "{}, correo: {}, telefono: {}: Dijo {}".format(nombre,correo,telefono,mensaje),
            "gamesmoes.duoc@gmail.com",
            ['gamesmoes.duoc@gmail.com'],
            reply_to=[correo])
            try:
                email.send()
                #TODO:mejorar esto para que mande el ok
                return redirect(reverse('contacto')+"?ok")
            except Exception as e:
                return redirect(reverse('contacto')+"?error")
    return render(request, "contacto.html", {'form':formulario})