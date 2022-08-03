from django.shortcuts import render, HttpResponse, redirect

def index(request):
    estudiantes = ['Gomez Marcos Emily',
                   'Pinedo Romero Kevin']
 
    return render(request,'index.html', {
        'titulo':'Inicio',
        'mensaje':'Examen Final LP3 :c',
        'estudiantes': estudiantes
    })

def curso(request):
    return render(request, 'curso.html', {
        'titulo': 'Cursos',
        'mensaje':'Listado de cursos'
    })

def carrera(request):
    return render(request, 'carrera.html', {
        'titulo': 'Carreras',
        'mensaje':'Listado de carreras'
    })

def crearcurso(request):
    return render(request, 'crear-curso.html', {
        'titulo': 'Crear Curso',
        'mensaje':'Agregar cursos'
    })

def crearcarrera(request):
    return render(request, 'crear-carrera.html', {
        'titulo': 'Crear Carrera',
        'mensaje':'Agregar carreras'
    })