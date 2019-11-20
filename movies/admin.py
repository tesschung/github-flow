from django.contrib import admin
from .models import Genre, Movie, Review

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Review)
