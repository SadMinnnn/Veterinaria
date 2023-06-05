from django.contrib import admin
from .models import registrar
from .models import historiaclinica
from .models import recetarmedicamentos
from .models import ventasmedicamentos


admin.site.register(registrar)
admin.site.register(historiaclinica)
admin.site.register(recetarmedicamentos)
admin.site.register(ventasmedicamentos)