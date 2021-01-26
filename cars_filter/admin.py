from django.contrib import admin
from cars_filter import models

# Register your models here.
@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    pass


