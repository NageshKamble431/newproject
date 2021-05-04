from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(movie)
class movieAdmin(admin.ModelAdmin):
    list_display = ['title','discription','genres','id']


@admin.register(collection)
class collectionAdmin(admin.ModelAdmin):
    list_display = ['title','discription','movie','collection_id']


