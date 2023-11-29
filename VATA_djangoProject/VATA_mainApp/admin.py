from django.contrib import admin

from .models import testModel, Object, Place,User,Favorito

# Register your models here.
# admin.site.register(testModel)
admin.site.register(Object)
admin.site.register(Place)
admin.site.register(Favorito)

