// Cursor Clone - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for anchor links
    initSmoothScrolling();
    
    // Newsletter subscription
    initNewsletterForm();
    
    // Add scroll effects
    initScrollEffects();
    
    // Initialize animations
    initAnimations();
    
    // Mobile menu handling
    initMobileMenu();
});

// Smooth scrolling for internal links
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                const offsetTop = targetElement.offsetTop - 80; // Account for fixed navbar
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Newsletter subscription form
function initNewsletterForm() {
    const form = document.getElementById('newsletter-form');
    const emailInput = document.getElementById('newsletter-email');
    
    if (form && emailInput) {
        form.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const email = emailInput.value.trim();
            
            if (!email) {
                showNotification('Por favor, ingresa tu email.', 'warning');
                return;
            }
            
            if (!isValidEmail(email)) {
                showNotification('Por favor, ingresa un email válido.', 'warning');
                return;
            }
            
            // Add loading state
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalContent = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
            submitBtn.disabled = true;
            
            try {
                const response = await fetch('/subscribe/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ email: email })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    showNotification(data.message, 'success');
                    emailInput.value = '';
                } else {
                    showNotification(data.message, 'error');
                }
                
            } catch (error) {
                console.error('Error:', error);
                showNotification('Error al procesar la suscripción. Inténtalo de nuevo.', 'error');
            } finally {
                // Restore button
                submitBtn.innerHTML = originalContent;
                submitBtn.disabled = false;
            }
        });
    }
}

// Email validation
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Show notification
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(notification => notification.remove());
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification alert alert-${type === 'error' ? 'danger' : type} alert-dismissible fade show`;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 9999;
        max-width: 400px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    `;
    
    notification.innerHTML = `
        <div class="d-flex align-items-center">
            <i class="fas fa-${getNotificationIcon(type)} me-2"></i>
            <span>${message}</span>
            <button type="button" class="btn-close ms-auto" data-bs-dismiss="alert"></button>
        </div>
    `;
    
    document.body.appendChild(notification);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

// Get icon for notification type
function getNotificationIcon(type) {
    const icons = {
        'success': 'check-circle',
        'error': 'exclamation-circle',
        'warning': 'exclamation-triangle',
        'info': 'info-circle'
    };
    return icons[type] || icons['info'];
}

// Scroll effects
function initScrollEffects() {
    const navbar = document.querySelector('.navbar');
    let lastScrollTop = 0;
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // Navbar background opacity
        if (scrollTop > 50) {
            navbar.style.backgroundColor = 'rgba(45, 52, 54, 0.98)';
        } else {
            navbar.style.backgroundColor = 'rgba(45, 52, 54, 0.95)';
        }
        
        // Hide/show navbar on scroll
        if (scrollTop > lastScrollTop && scrollTop > 100) {
            // Scrolling down
            navbar.style.transform = 'translateY(-100%)';
        } else {
            // Scrolling up
            navbar.style.transform = 'translateY(0)';
        }
        
        lastScrollTop = scrollTop;
    });
}

// Initialize animations
function initAnimations() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animatedElements = document.querySelectorAll('.feature-card, .testimonial-card, .pricing-card');
    animatedElements.forEach(element => {
        observer.observe(element);
    });
}

// Mobile menu handling
function initMobileMenu() {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    if (navbarToggler && navbarCollapse) {
        // Close mobile menu when clicking on a link
        const navLinks = navbarCollapse.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (navbarCollapse.classList.contains('show')) {
                    navbarToggler.click();
                }
            });
        });
        
        // Close mobile menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!navbarCollapse.contains(e.target) && !navbarToggler.contains(e.target)) {
                if (navbarCollapse.classList.contains('show')) {
                    navbarToggler.click();
                }
            }
        });
    }
}

// Download button interactions
function initDownloadButtons() {
    const downloadButtons = document.querySelectorAll('[data-download]');
    
    downloadButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            const platform = this.dataset.download;
            
            // Add loading state
            const originalContent = this.innerHTML;
            this.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Preparando descarga...';
            this.disabled = true;
            
            // Simulate download preparation
            setTimeout(() => {
                this.innerHTML = '<i class="fas fa-check me-2"></i>¡Descarga iniciada!';
                
                setTimeout(() => {
                    this.innerHTML = originalContent;
                    this.disabled = false;
                    
                    showNotification(`Descarga para ${platform} iniciada.`, 'success');
                }, 1500);
            }, 1000);
        });
    });
}

// Feature demo interactions
function initFeatureDemo() {
    const demoTriggers = document.querySelectorAll('[data-demo]');
    
    demoTriggers.forEach(trigger => {
        trigger.addEventListener('click', function(e) {
            e.preventDefault();
            
            const feature = this.dataset.demo;
            
            // Show demo modal or perform demo action
            showFeatureDemo(feature);
        });
    });
}

// Show feature demo
function showFeatureDemo(feature) {
    const demoContent = {
        'ai-completion': 'Demostración de autocompletado con IA...',
        'code-chat': 'Demostración de chat con código...',
        'smart-refactor': 'Demostración de refactoring inteligente...'
    };
    
    const content = demoContent[feature] || 'Demostración no disponible.';
    showNotification(content, 'info');
}

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + K for search (placeholder)
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        showNotification('Búsqueda disponible próximamente.', 'info');
    }
    
    // Escape key to close modals/notifications
    if (e.key === 'Escape') {
        const notifications = document.querySelectorAll('.notification');
        notifications.forEach(notification => notification.remove());
    }
});

// Initialize additional features when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    initDownloadButtons();
    initFeatureDemo();
});

// Performance optimization
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Use debounced scroll handler for better performance
const debouncedScrollHandler = debounce(function() {
    // Additional scroll-based functionality can be added here
}, 100);

window.addEventListener('scroll', debouncedScrollHandler);

// Export functions for potential external use
window.CursorClone = {
    showNotification,
    isValidEmail,
    showFeatureDemo
}; 