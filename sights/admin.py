from django.contrib import admin
from .models import *

class SightAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}

admin.site.register(Sight, SightAdmin)
admin.site.register(SightImage)
admin.site.register(Category, CategoryAdmin)