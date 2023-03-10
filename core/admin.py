from django.contrib import admin
from .models import Produto, Cliente

class Produtoadmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome','email')

admin.site.register(Produto, Produtoadmin)
admin.site.register(Cliente, ClientAdmin)

