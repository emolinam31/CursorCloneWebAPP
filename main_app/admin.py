from django.contrib import admin
from .models import Feature, Testimonial

# Register your models here.

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Testimonial) 
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'position', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('author', 'position', 'content') 