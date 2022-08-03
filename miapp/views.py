from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Curso
from django.contrib import messages

def index(request):
    estudiantes = ['Gomez Marcos Emily',
                   'Pinedo Romero Kevin']
 
    return render(request,'index.html', {
        'titulo':'Inicio',
        'mensaje':'Examen Final LP3 :c',
        'estudiantes': estudiantes
    })

def curso(request):
    curso = Curso.objects.all();
    return render(request, 'curso.html', {
        'curso': curso,
        'titulo':'Listado de cursos'
    })

def carrera(request):
    return render(request, 'carrera.html', {
        'titulo': 'Carreras',
        'mensaje':'Listado de carreras'
    })

def save_curso(request):
    
    if request.method == 'POST':
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        hora = request.POST['hora']
        creditos = request.POST['creditos']
        estado = request.POST['estado']

        curso = Curso(
            codigo = codigo,
            nombre = nombre,
            hora = hora,
            creditos = creditos,
            estado = estado
        )
        curso.save()

        messages.success(request, f'Se agregó correctamente el curso {curso.id}')

        return redirect('curso')
        #return HttpResponse(f"Curso Creado: {curso.codigo} - {curso.nombre} - {curso.hora} - {curso.creditos} - {curso.estado}")
    else:
        return HttpResponse("<h2>No se ha podido registrar el curso</h2>")

def crearcurso(request):
    return render(request, 'crear-curso.html')

def eliminar_curso(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('curso')

'''
def crearcurso(request):
    return render(request, 'crear-curso.html', {
        'titulo': 'Crear Curso',
        'mensaje':'Agregar cursos'
    })
'''
def crearcarrera(request):
    return render(request, 'crear-carrera.html', {
        'titulo': 'Crear Carrera',
        'mensaje':'Agregar carreras'
    })