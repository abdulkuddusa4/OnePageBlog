from django.contrib import admin
from .models import Post


@admin.register(Post)
class ModelPost(admin.ModelAdmin):
    list_display = [
        'title',
        'creation_date',
        'updation_date',
    ]
    pass
