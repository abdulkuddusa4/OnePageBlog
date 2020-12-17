from django.contrib import admin
from .models import EmailValidator


@admin.register(EmailValidator)
class ModelEmailValidator(admin.ModelAdmin):
    list_display = ['user']
