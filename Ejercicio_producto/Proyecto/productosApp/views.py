from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def electronica(request):
    data = {
        'titulo': 'Electronica',
        'productos': [
            {'nombre': 'Dipositivo', 'imagen': 'imagenes/Electronica.jfif', 'descripcion': 'Ordenador portátil de alta gama.'},
            {'nombre': 'Celular', 'imagen': 'imagenes/Celular.jpg', 'descripcion': 'La mejor herramienta'},
            {'nombre': 'Playstation', 'imagen': 'imagenes/Play.jpeg', 'descripcion': 'Consola de videojuegos de última generación.'},
        ]
    }
    return render(request, 'productos.html', data)

def jugueteria(request):
    data = {
        'titulo': 'Jugueteria',
        'productos': [
            {'nombre': 'Pelota', 'imagen': 'imagenes/Pelota.jfif', 'descripcion': 'Pelota de fútbol para niños.'},
            {'nombre': 'Figura de Acción', 'imagen': 'imagenes/Figura.jfif', 'descripcion': 'Figura coleccionable de superhéroe.'},
            {'nombre': 'Muñeca Barbie', 'imagen': 'imagenes/Muñeca.jfif', 'descripcion': 'Muñeca clásica con ropa y accesorios.'},
        ]
    }
    return render(request, 'productos.html', data)

def deportes(request):
    data = {
        'titulo': 'Deportes',
        'productos': [
            {'nombre': 'Polera', 'imagen': 'imagenes/polera.jfif', 'descripcion': 'Polera deportiva cómoda y estilosa.'},
            {'nombre': 'Raqueta', 'imagen': 'imagenes/Raqueta.jpg', 'descripcion': 'Raqueta de tenis de alta calidad.'},
            {'nombre': 'Pala', 'imagen': 'imagenes/Pala.jpg', 'descripcion': 'Pala de pádel para jugadores exigentes.'},
        ]
    }
    return render(request, 'productos.html', data)