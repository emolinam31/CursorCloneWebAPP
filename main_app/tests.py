from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Feature, Testimonial, NewsletterSubscription
import json

# Create your tests here.

class FeatureModelTest(TestCase):
    """Tests para el modelo Feature"""
    
    def setUp(self):
        self.feature = Feature.objects.create(
            title="Test Feature",
            description="Test description",
            icon="test",
            is_active=True
        )
    
    def test_feature_creation(self):
        """Test de creación de Feature"""
        self.assertEqual(self.feature.title, "Test Feature")
        self.assertEqual(self.feature.description, "Test description")
        self.assertEqual(self.feature.icon, "test")
        self.assertTrue(self.feature.is_active)
    
    def test_feature_str(self):
        """Test del método __str__ de Feature"""
        self.assertEqual(str(self.feature), "Test Feature")


class TestimonialModelTest(TestCase):
    """Tests para el modelo Testimonial"""
    
    def setUp(self):
        self.testimonial = Testimonial.objects.create(
            author="Test Author",
            position="Test Position",
            content="Test testimonial content",
            is_active=True
        )
    
    def test_testimonial_creation(self):
        """Test de creación de Testimonial"""
        self.assertEqual(self.testimonial.author, "Test Author")
        self.assertEqual(self.testimonial.position, "Test Position")
        self.assertEqual(self.testimonial.content, "Test testimonial content")
        self.assertTrue(self.testimonial.is_active)
    
    def test_testimonial_str(self):
        """Test del método __str__ de Testimonial"""
        self.assertEqual(str(self.testimonial), "Test Author - Test Position")


class NewsletterSubscriptionModelTest(TestCase):
    """Tests para el modelo NewsletterSubscription"""
    
    def setUp(self):
        self.subscription = NewsletterSubscription.objects.create(
            email="test@example.com",
            is_active=True
        )
    
    def test_subscription_creation(self):
        """Test de creación de NewsletterSubscription"""
        self.assertEqual(self.subscription.email, "test@example.com")
        self.assertTrue(self.subscription.is_active)
    
    def test_subscription_str(self):
        """Test del método __str__ de NewsletterSubscription"""
        self.assertEqual(str(self.subscription), "test@example.com")


class ViewsTest(TestCase):
    """Tests para las vistas"""
    
    def setUp(self):
        self.client = Client()
        
        # Crear objetos de prueba
        self.feature = Feature.objects.create(
            title="Test Feature",
            description="Test description",
            icon="robot",
            is_active=True
        )
        
        self.testimonial = Testimonial.objects.create(
            author="Test Author",
            position="Developer",
            content="Great product!",
            is_active=True
        )
    
    def test_home_view(self):
        """Test de la vista home"""
        response = self.client.get(reverse('main_app:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Build software faster")
        self.assertContains(response, self.feature.title)
        self.assertContains(response, self.testimonial.author)
    
    def test_features_view(self):
        """Test de la vista features"""
        response = self.client.get(reverse('main_app:features'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Características Avanzadas")
    
    def test_pricing_view(self):
        """Test de la vista pricing"""
        response = self.client.get(reverse('main_app:pricing'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Planes y Precios")
    
    def test_download_view(self):
        """Test de la vista download"""
        response = self.client.get(reverse('main_app:download'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Descarga Cursor")
    
    def test_subscribe_newsletter_valid_email(self):
        """Test de suscripción al newsletter con email válido"""
        response = self.client.post(
            reverse('main_app:subscribe_newsletter'),
            data=json.dumps({'email': 'test@example.com'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertIn('Gracias por suscribirte', data['message'])
        
        # Verificar que se creó la suscripción
        self.assertTrue(
            NewsletterSubscription.objects.filter(
                email='test@example.com'
            ).exists()
        )
    
    def test_subscribe_newsletter_duplicate_email(self):
        """Test de suscripción con email duplicado"""
        # Crear suscripción inicial
        NewsletterSubscription.objects.create(email='test@example.com')
        
        response = self.client.post(
            reverse('main_app:subscribe_newsletter'),
            data=json.dumps({'email': 'test@example.com'}),
            content_type='application/json'
        )
        
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertIn('ya está suscrito', data['message'])
    
    def test_subscribe_newsletter_invalid_method(self):
        """Test de suscripción con método inválido"""
        response = self.client.get(reverse('main_app:subscribe_newsletter'))
        
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertIn('Método no permitido', data['message'])


class URLsTest(TestCase):
    """Tests para las URLs"""
    
    def test_home_url_resolves(self):
        """Test de resolución de URL home"""
        url = reverse('main_app:home')
        self.assertEqual(url, '/')
    
    def test_features_url_resolves(self):
        """Test de resolución de URL features"""
        url = reverse('main_app:features')
        self.assertEqual(url, '/features/')
    
    def test_pricing_url_resolves(self):
        """Test de resolución de URL pricing"""
        url = reverse('main_app:pricing')
        self.assertEqual(url, '/pricing/')
    
    def test_download_url_resolves(self):
        """Test de resolución de URL download"""
        url = reverse('main_app:download')
        self.assertEqual(url, '/download/')
    
    def test_subscribe_url_resolves(self):
        """Test de resolución de URL subscribe"""
        url = reverse('main_app:subscribe_newsletter')
        self.assertEqual(url, '/subscribe/')


class AdminTest(TestCase):
    """Tests para la interfaz de administración"""
    
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        self.client = Client()
        self.client.login(username='admin', password='adminpass123')
    
    def test_admin_access(self):
        """Test de acceso al admin"""
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
    
    def test_feature_admin(self):
        """Test del admin de Feature"""
        feature = Feature.objects.create(
            title="Admin Test Feature",
            description="Test description",
            icon="test",
            is_active=True
        )
        
        response = self.client.get('/admin/main_app/feature/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, feature.title)


class IntegrationTest(TestCase):
    """Tests de integración"""
    
    def setUp(self):
        self.client = Client()
    
    def test_full_user_flow(self):
        """Test del flujo completo de usuario"""
        # 1. Usuario visita la página principal
        response = self.client.get(reverse('main_app:home'))
        self.assertEqual(response.status_code, 200)
        
        # 2. Usuario navega a características
        response = self.client.get(reverse('main_app:features'))
        self.assertEqual(response.status_code, 200)
        
        # 3. Usuario revisa precios
        response = self.client.get(reverse('main_app:pricing'))
        self.assertEqual(response.status_code, 200)
        
        # 4. Usuario va a la página de descarga
        response = self.client.get(reverse('main_app:download'))
        self.assertEqual(response.status_code, 200)
        
        # 5. Usuario se suscribe al newsletter
        response = self.client.post(
            reverse('main_app:subscribe_newsletter'),
            data=json.dumps({'email': 'user@example.com'}),
            content_type='application/json'
        )
        
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        
        # Verificar que la suscripción fue creada
        self.assertTrue(
            NewsletterSubscription.objects.filter(
                email='user@example.com'
            ).exists()
        ) 