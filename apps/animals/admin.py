from django.contrib import admin
from apps.animals.models import AnimalBread, AnimalSpecies, Animals

@admin.register(Animals)
class AnimalsAdmin(admin.ModelAdmin):
    list_display = ('species', 'breed')

@admin.register(AnimalBread)
class AnimalBreadAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(AnimalSpecies)
class AnimalSpecies(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)