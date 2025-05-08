from django.urls import path
from .views import landingview, productlistview, supplierlistview, addsupplier, addproduct
from .views import deleteproduct, confirmdeleteproduct, deletesupplier, confirmdeletesupplier
from .views import edit_product_post, edit_product_get, edit_supplier_post, edit_supplier_get, searchsuppliers
from .views import products_filtered

urlpatterns = [
    path('', landingview),

    # Products url's
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
    path('products-by-supplier/<int:id>/', products_filtered),

    # Supplier url's
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('edit-supplier-get/<int:id>/', edit_supplier_get),
    path('edit-supplier-post/<int:id>/', edit_supplier_post),
    path('search-suppliers/', searchsuppliers),
]
