from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def main(request):
    
    if request.method != 'GET':
        return JsonResponse({'error':'El método GET es necesario'}, status=400)
    
    productos = Producto.objects.all()
    serialized_productos = [producto.serialize() for producto in productos]
    response_data = {
        'productos' : serialized_productos
    }
    
    return JsonResponse(response_data, status=200, safe=False)

@csrf_exempt
def product_add(request):
    
    if request.method != 'POST':
        return JsonResponse({'error':'El método POST es necesario'}, status=400)
    
    try:
        data = json.loads(request.body)
        product_name = data['product_name']
        product_price = data['product_price']
        
        new_product = Producto.objects.create(nombre=product_name, precio=product_price)
        
        return JsonResponse({'success' : 'El producto se almacenó correctamente'}, status=204)
    
    except KeyError:
        return JsonResponse({'error' : 'Por favor, complete todos los campos'}, status=400)
    except Exception as e:
        return JsonResponse({'error' : 'Hubo un error al agregar el producto: {e}'}, status=500)
# 200 -> Respuestas
# 300 -> Redireccionamiento
# 400 -> Errores del usuario

# Django API Rest Framework