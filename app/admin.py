# Jos rekisteröi tällä tavalla adminille oman appin
# modelit, voi myös admin sivuilta muokata näitä tietoja.

from django.contrib import admin

from app.models import Supplier, Product, Employee, Store

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass