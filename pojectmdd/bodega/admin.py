from django.contrib import admin

from .models import Bodega, Delegacion, Universidad, Bodeguero, Elemento, Ciudad, Region, Deportista, Tiene
# Register your models here.
admin.site.register(Bodeguero)
admin.site.register(Bodega)
admin.site.register(Elemento)
admin.site.register(Delegacion)
admin.site.register(Universidad)
admin.site.register(Ciudad)
admin.site.register(Region)
admin.site.register(Deportista)
admin.site.register(Tiene)
