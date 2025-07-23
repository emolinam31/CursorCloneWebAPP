# Cursor Clone - Simulación de la Página Principal de Cursor

Un proyecto Django que simula la página principal del editor de código Cursor, implementando una arquitectura MVC (Model-View-Controller) con tecnologías web básicas.

## 🚀 Características

- **Arquitectura MVC**: Implementación clara de la arquitectura Modelo-Vista-Controlador con Django
- **Diseño Responsivo**: Interfaz moderna que simula Cursor con Bootstrap 5
- **Interfaz Interactiva**: Navegación suave, animaciones CSS y efectos JavaScript
- **Gestión de Datos**: Modelos Django para características, testimonios y suscripciones
- **Newsletter**: Sistema de suscripción con validación de emails
- **Panel de Administración**: Interfaz de administración Django completamente funcional

## 📋 Requisitos del Sistema

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Navegador web moderno

## 🛠️ Instalación

### 1. Clonar o Descargar el Proyecto

```bash
git clone <url-del-repositorio>
cd WebCursor
```

### 2. Crear Entorno Virtual (Recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar Base de Datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear Usuario Administrador (Opcional)

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el Servidor de Desarrollo

```bash
python manage.py runserver
```

El proyecto estará disponible en: `http://127.0.0.1:8000/`

## 📁 Estructura del Proyecto

```
WebCursor/
├── cursor_clone/           # Configuración principal del proyecto
│   ├── __init__.py
│   ├── settings.py         # Configuración de Django
│   ├── urls.py            # URLs principales
│   ├── wsgi.py            # Configuración WSGI
│   └── asgi.py            # Configuración ASGI
├── main_app/              # Aplicación principal
│   ├── __init__.py
│   ├── admin.py           # Configuración del admin
│   ├── apps.py            # Configuración de la app
│   ├── models.py          # Modelos (M en MVC)
│   ├── views.py           # Vistas/Controladores (C en MVC)
│   ├── urls.py            # URLs de la aplicación
│   └── tests.py           # Tests unitarios
├── templates/             # Templates HTML (V en MVC)
│   ├── base.html          # Template base
│   └── main_app/
│       ├── home.html      # Página principal
│       ├── features.html  # Página de características
│       ├── pricing.html   # Página de precios
│       └── download.html  # Página de descarga
├── static/                # Archivos estáticos
│   ├── css/
│   │   └── style.css      # Estilos principales
│   └── js/
│       └── main.js        # JavaScript principal
├── manage.py              # Utilidad de Django
├── requirements.txt       # Dependencias del proyecto
└── README.md             # Este archivo
```

## 🏗️ Arquitectura MVC

### Modelos (Model)
- **Feature**: Características destacadas de Cursor
- **Testimonial**: Testimonios de usuarios
- **NewsletterSubscription**: Suscripciones al newsletter

### Vistas (View)
- Templates HTML con Django Template Language
- Diseño responsivo con Bootstrap 5
- Animaciones y efectos CSS

### Controladores (Controller)
- **HomeView**: Página principal con características y testimonios
- **FeaturesView**: Página detallada de características
- **PricingView**: Página de planes y precios
- **DownloadView**: Página de descarga
- **SubscribeView**: API para suscripciones al newsletter

## 🎨 Características de la Interfaz

### Página Principal
- Hero section con gradiente y animaciones
- Editor de código simulado
- Grid de características
- Sección de testimonios
- Call-to-action

### Página de Características
- Lista detallada de funcionalidades
- Demos interactivos
- Ejemplos de código
- Showcase de capacidades

### Página de Precios
- Planes de suscripción
- Toggle mensual/anual
- FAQ accordion
- Comparación de características

### Página de Descarga
- Detección automática del SO
- Instrucciones de instalación
- Requisitos del sistema
- Múltiples formatos de descarga

## 🔧 Funcionalidades

### Backend
- Sistema de administración Django
- API REST para newsletter
- Validación de formularios
- Gestión de base de datos SQLite

### Frontend
- Navegación responsive
- Efectos de scroll
- Animaciones CSS
- JavaScript vanilla para interactividad
- Formularios Ajax

### Características Técnicas
- Arquitectura MVC clara
- Código limpio y documentado
- Tests unitarios incluidos
- SEO optimizado
- Performance optimizada

## 🧪 Ejecutar Tests

```bash
python manage.py test
```

## 📊 Panel de Administración

Accede al panel de administración en: `http://127.0.0.1:8000/admin/`

Desde aquí puedes:
- Gestionar características
- Administrar testimonios
- Ver suscripciones al newsletter
- Configurar usuarios

## 🚀 Despliegue

### Variables de Entorno
Crea un archivo `.env` para configuración de producción:

```env
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=False
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com
```

### Producción
Para despliegue en producción, considera:
- Usar PostgreSQL en lugar de SQLite
- Configurar archivos estáticos con WhiteNoise
- Usar Gunicorn como servidor WSGI
- Configurar HTTPS

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto es una simulación educativa de la interfaz de Cursor para demostrar capacidades de desarrollo web con Django.

## 🔍 Detalles Técnicos

### Tecnologías Utilizadas
- **Backend**: Django 4.2.7, Python 3.8+
- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Frameworks CSS**: Bootstrap 5.3.2
- **Iconos**: Font Awesome 6.4.0
- **Fuentes**: Google Fonts (Inter)
- **Base de Datos**: SQLite (desarrollo), PostgreSQL (recomendado para producción)

### Patrones de Diseño
- **MVC**: Separación clara de responsabilidades
- **DRY**: Don't Repeat Yourself
- **Responsive Design**: Mobile-first approach
- **Progressive Enhancement**: Funcionalidad básica sin JavaScript

### Rendimiento
- CSS y JS minificados para producción
- Imágenes optimizadas
- Lazy loading para contenido pesado
- Caching de templates Django

## 📞 Soporte

Para preguntas o problemas, por favor:
1. Revisa la documentación
2. Busca en issues existentes
3. Crea un nuevo issue si es necesario

---

**Nota**: Este es un proyecto educativo que simula la interfaz de Cursor con fines de demostración de habilidades de desarrollo web con Django y arquitectura MVC. 