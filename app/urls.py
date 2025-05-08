from django.urls import path
from .views import landingview, productlistview, supplierlistview, addsupplier, addproduct
from .views import deleteproduct, confirmdeleteproduct, deletesupplier, confirmdeletesupplier
from .views import edit_product_post, edit_product_get

urlpatterns = [
    path('', landingview),

    # Products url's
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),

    # Supplier url's
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
]
