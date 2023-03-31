from django.contrib import admin
from .models import Report,Message,criminal,Offense,Category
# Register your models here.
admin.site.register(Report)
admin.site.register(Message)
admin.site.register(Offense)
admin.site.register(criminal)
admin.site.register(Category)




class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
