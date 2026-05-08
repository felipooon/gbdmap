import os
import json
import requests
from django.http import JsonResponse
from django.core.cache import cache
from django.conf import settings
from django.views.decorators.http import require_GET

@require_GET
def ebird_proxy(request, ebird_path):
    """Proxy para eBird que inyecta la API Key en secreto, bloquea robos de código y cachea respuestas"""
    


    # 2. LÓGICA DE CACHÉ: Crear una llave única para esta consulta
    # Esto asegura que si se piden datos distintos (ej. otra región), se guarden por separado
    cache_key = f"ebird_{ebird_path}_{request.GET.urlencode()}"
    
    # 3. Revisar si la respuesta ya está en memoria
    datos_cacheados = cache.get(cache_key)
    if datos_cacheados:
        # Si está en caché, devolvemos el dato inmediatamente sin consultar a eBird
        return JsonResponse(datos_cacheados, safe=False)

    # 4. Si no hay caché, construimos la URL hacia eBird
    url = f"https://api.ebird.org/v2/{ebird_path}"
    
    # Inyectar la API Key desde las variables de entorno de Render
    headers = {"X-eBirdApiToken": settings.EBIRD_API_KEY}
    
    # Pasar los parámetros originales (como locale=es_CL)
    params = request.GET.dict()
    
    try:
        response_ebird = requests.get(url, headers=headers, params=params)
        response_ebird.raise_for_status()
        
        datos_nuevos = response_ebird.json()
        cache.set(cache_key, datos_nuevos, 300)
        
        # 2. Le decimos al navegador que confiamos en este origen
        response = JsonResponse(datos_nuevos, safe=False)
            
        return response
        
    except requests.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)
    

def get_species_dict(request):
    """Lee el diccionario local y lo devuelve como JSON puro con CORS público"""
    file_path = os.path.join(settings.BASE_DIR, 'tienda', 'species.json')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # 1. Guardamos la respuesta en una variable en vez de retornarla de inmediato
        response = JsonResponse(data, safe=False)
        
        # 2. Le pegamos la cabecera CORS universal
        response["Access-Control-Allow-Origin"] = "*"
        
        # 3. Ahora sí, devolvemos la respuesta
        return response
        
    except FileNotFoundError:
        return JsonResponse({"error": "Archivo no encontrado"}, status=404)