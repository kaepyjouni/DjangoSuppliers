from django.urls import path
from .views import productlistview, supplierlistview, addsupplier, addproduct
from .views import deleteproduct, confirmdeleteproduct, deletesupplier, confirmdeletesupplier
from .views import edit_product_post, edit_product_get, edit_supplier_post, edit_supplier_get, searchsuppliers
from .views import products_filtered, loginview, login_action, logout_action
from .views import storeslistview, employeeslistview, addstore, addemployee, products_by_store
from .views import deletestore, confirmdeletestore, deleteemployee, confirmdeleteempolyee
from .views import edit_employee_get, edit_employee_post, edit_store_get, edit_store_post

urlpatterns = [
    # Landing page after login
    # path('landing/', landingview),

    # Loginview and authentication method
    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),

    # Products url's
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
    path('products-by-supplier/<int:id>/', products_filtered),
    path('products-by-store/<int:id>/', products_by_store, name='products_by_store'),

    # Supplier url's
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('edit-supplier-get/<int:id>/', edit_supplier_get),
    path('edit-supplier-post/<int:id>/', edit_supplier_post),
    path('search-suppliers/', searchsuppliers),

    # Employees url's
    path('employees/', employeeslistview),
    path('add-employee/', addemployee),
    path('delete-employee/<int:id>/', deleteemployee),
    path('confirm-delete-employee/<int:id>/', confirmdeleteempolyee),
    path('edit-employee-get/<int:id>/', edit_employee_get),
    path('edit-employee-post/<int:id>/', edit_employee_post),

    # Stores url's
    path('stores/', storeslistview),
    path('add-store/', addstore),
    path('delete-store/<int:id>/', deletestore),
    path('confirm-delete-store/<int:id>/', confirmdeletestore),
    path('edit-store-get/<int:id>/', edit_store_get),
    path('edit-store-post/<int:id>/', edit_store_post),
]
