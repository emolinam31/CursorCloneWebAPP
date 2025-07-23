from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Feature, Testimonial, NewsletterSubscription

# Create your views here.

def home(request):
    """
    Vista principal - Controller para la página de inicio
    Simula la página principal de Cursor
    """
    # Obtener características activas (Modelo)
    features = Feature.objects.filter(is_active=True)[:6]
    
    # Obtener testimonios activos (Modelo)
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    
    context = {
        'features': features,
        'testimonials': testimonials,
        'page_title': 'Cursor - The AI-first Code Editor',
        'hero_title': 'Build software faster',
        'hero_subtitle': 'The AI-first code editor. Built to make you extraordinarily productive, Cursor is the best way to code with AI.',
    }
    
    # Renderizar template (Vista)
    return render(request, 'main_app/home.html', context)


def features(request):
    """
    Vista de características - Controller para la página de características
    """
    all_features = Feature.objects.filter(is_active=True)
    
    context = {
        'features': all_features,
        'page_title': 'Características - Cursor',
    }
    
    return render(request, 'main_app/features.html', context)


def pricing(request):
    """
    Vista de precios - Controller para la página de precios
    """
    context = {
        'page_title': 'Precios - Cursor',
    }
    
    return render(request, 'main_app/pricing.html', context)


def download(request):
    """
    Vista de descarga - Controller para la página de descarga
    """
    context = {
        'page_title': 'Descargar - Cursor',
    }
    
    return render(request, 'main_app/download.html', context)


@csrf_exempt
def subscribe_newsletter(request):
    """
    Vista para suscripción al newsletter
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            
            if email:
                subscription, created = NewsletterSubscription.objects.get_or_create(
                    email=email
                )
                
                if created:
                    return JsonResponse({
                        'success': True, 
                        'message': '¡Gracias por suscribirte!'
                    })
                else:
                    return JsonResponse({
                        'success': False, 
                        'message': 'Este email ya está suscrito.'
                    })
            else:
                return JsonResponse({
                    'success': False, 
                    'message': 'Email requerido.'
                })
                
        except Exception as e:
            return JsonResponse({
                'success': False, 
                'message': 'Error al procesar la suscripción.'
            })
    
    return JsonResponse({'success': False, 'message': 'Método no permitido.'}) 