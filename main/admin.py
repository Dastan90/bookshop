from django.contrib import admin

# Register your models here.
from main.models import *

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)