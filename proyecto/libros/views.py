from django.shortcuts import render, redirect
from libros.models import Libro, Autores
from libros.forms import LibroForms
def index(request):
    return render(request,"libros/index.html")

def lista_libros(request):
    busqueda = request.GET.get("busqueda",None)
    if busqueda:
        print(busqueda)
        consulta = Libro.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = Libro.objects.all()
    contexto = {"libros": consulta}
    return render(request,"libros/lista_libros.html",contexto)

def libros_create(request):
    if request.method == "POST":
        form = LibroForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("libros:lista_libros")
    else:
        form = LibroForms()
    return render(request,"libros/libros_create.html",{"form":form})

def lista_autores(request):
    busqueda = request.GET.get("busqueda",None)
    if busqueda:
        print(busqueda)
        consulta = Autores.objects.filter(nombre__icontains=busqueda)
    else:
       consulta = Autores.objects.all()
    contexto = {"autores": consulta}
    return render(request,"libros/lista_autores.html",contexto)


