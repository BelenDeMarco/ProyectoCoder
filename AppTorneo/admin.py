from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register (Torneo)

admin.site.register (Sede)

admin.site.register (Equipo)
