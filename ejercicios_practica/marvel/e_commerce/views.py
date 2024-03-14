from django.shortcuts import render
from django.http import JsonResponse
from e_commerce.models import Comic
# Create your views here.
def hola_mundo(request):    
    datos =  {"mensaje": "hola_mundo", "curso": "python-django"}
    return JsonResponse(datos)




def get_comic_api_view(request):
    if request.method == 'GET':

        _queryset = Comic.objects.all()
      
        print(_queryset)

        _data = list(_queryset.values()) if _queryset.exists() else []
             

        return JsonResponse(data=_data, safe=False, status=200)
        
    else:
        return JsonResponse(
            data={"message": "Método HTTP no permitido."},
            status=405
        )
