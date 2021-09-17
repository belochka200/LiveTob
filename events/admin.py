from django.contrib import admin
from .models import *


class CafeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class HotelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class EntertainmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CafeCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}


class HotelCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}


class EntertainmentCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}


admin.site.register(CafeCategory, CafeCategoryAdmin)
admin.site.register(HotelCategory, HotelCategoryAdmin)
admin.site.register(EntertainmentCategory, EntertainmentCategoryAdmin)
admin.site.register(Cafe, CafeAdmin)
admin.site.register(CafeImage)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelImage)
admin.site.register(Entertainment, EntertainmentAdmin)
admin.site.register(EntertainmentImage)
