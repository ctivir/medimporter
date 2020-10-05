from django.contrib import admin
from .models import Produto, Category, Importadora, Cliente

admin.site.register(Produto)
admin.site.register(Category)
admin.site.register(Importadora)
admin.site.register(Cliente)