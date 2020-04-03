from django.contrib import admin

# Register your models here.
from .models import Empresa, Camera, Local, Analise

'''class EmpresaAdmin(admin.ModelAdmin):
	list_display = ['razaosocial', 'cnpj']
	search_fields = ['razaosocial', 'cnpj']

admin.site.register(Empresa, EmpresaAdmin)'''

#those models will apear in django admin panel
admin.site.register(Empresa)
admin.site.register(Camera)
admin.site.register(Local)
admin.site.register(Analise)