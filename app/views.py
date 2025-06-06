from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier, Product, Employee, Store
from django.contrib.auth import authenticate, login, logout

# LANDING AFTER LOGIN

# def landingview(request):
#     return render(request, 'landingpage.html')

# LOGIN AND LOGOUT

def loginview(request):
    return render(request, 'loginpage.html')

def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    user = authenticate(username = user, password = passw)
    if user:
        login(request, user)
        context = {'name': user}
        return render(request, 'landingpage.html', context)
    else:
        return render(request, 'loginerror.html')

def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')

# Product views
def productlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        productlist = Product.objects.all()
        supplierlist = Supplier.objects.all()
        storelist = Store.objects.all()
        context = {'products': productlist, 'suppliers': supplierlist, 'stores': storelist}
        return render(request, 'productlist.html', context)

def addproduct(request):
    a = request.POST['productname']
    b = request.POST['packagesize']
    c = request.POST['unitprice']
    d = request.POST['unitsinstock']
    e = request.POST['supplier']
    f = request.POST['store']

    Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, store = Store.objects.get(id = f), supplier = Supplier.objects.get(id = e)).save()
    return redirect(request.META['HTTP_REFERER'])

def confirmdeleteproduct(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return render (request,"confirmdelprod.html",context)


def deleteproduct(request, id):
    Product.objects.get(id = id).delete()
    return redirect(productlistview)

def edit_product_get(request, id):
        product = Product.objects.get(id = id)
        context = {'product': product}
        return render (request,"edit_product.html",context)


def edit_product_post(request, id):
        item = Product.objects.get(id = id)
        item.unitprice = request.POST['unitprice']
        item.unitsinstock = request.POST['unitsinstock']
        item.save()
        return redirect(productlistview)

def products_filtered(request, id):
    productlist = Product.objects.all()
    filteredproducts = productlist.filter(supplier = id)
    context = {'products': filteredproducts}
    return render (request,"productlist.html",context)

def products_by_store(request, id):
    products = Product.objects.filter(store_id=id)
    suppliers = Supplier.objects.all()
    stores = Store.objects.all()
    store = get_object_or_404(Store, pk=id)
    return render(request, "productlist.html", {
        "products": products,
        "suppliers": suppliers,
        "stores": stores,
        "filtered_by": f"Store: {store.storename}"
    })




# Supplier views
def supplierlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplierlist = Supplier.objects.all()
        context = {'suppliers': supplierlist}
        return render(request, 'supplierlist.html', context)

def addsupplier(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])

def confirmdeletesupplier(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render (request,"confirmdelsupp.html",context)


def deletesupplier(request, id):
    Supplier.objects.get(id = id).delete()
    return redirect(supplierlistview)

def edit_supplier_get(request, id):
        supplier = Supplier.objects.get(id = id)
        context = {'supplier': supplier}
        return render (request,"edit_supplier.html",context)


def edit_supplier_post(request, id):
        item = Supplier.objects.get(id = id)
        item.contactname = request.POST['contact name']
        item.address = request.POST['address']
        item.phone = request.POST['phone']
        item.email = request.POST['email']
        item.country = request.POST['country']
        item.save()
        return redirect(supplierlistview)

def searchsuppliers(request):
    search = request.POST['search']
    filtered = Supplier.objects.filter(companyname__icontains=search)
    context = {'suppliers': filtered}
    return render (request,"supplierlist.html",context)


# EMPLOYEES 

def employeeslistview(request):
    employeelist = Employee.objects.all()
    storelist = Store.objects.all()
    context = {'employees': employeelist, 'stores': storelist}
    return render(request, 'employeeslist.html', context)

def addemployee(request):
    a = request.POST['firstname']
    b = request.POST['lastname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    Employee(firstname = a, lastname = b, address = c, phone = d, email = e).save()
    return redirect(request.META['HTTP_REFERER'])

def confirmdeleteempolyee(request, id):
    employee = Employee.objects.get(id = id)
    context = {'employee': employee}
    return render (request,"confirmdelemploy.html",context)

def deleteemployee(request, id):
    Employee.objects.get(id = id).delete()
    return redirect(employeeslistview)

def edit_employee_get(request, id):
        employee = Employee.objects.get(id = id)
        context = {'employee': employee}
        return render (request,"edit_employee.html",context)


def edit_employee_post(request, id):
        item = Employee.objects.get(id = id)
        item.address = request.POST['address']
        item.phone = request.POST['phone']
        item.email = request.POST['email']
        item.save()
        return redirect(employeeslistview)


# STORES

def storeslistview(request):
    storelist = Store.objects.all()
    employeelist = Employee.objects.all()
    productlist = Product.objects.all()
    context = {'stores': storelist, 'employees': employeelist, 'products': productlist}
    return render(request, 'storeslist.html', context)

def addstore(request):
    a = request.POST['storename']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Store(storename = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])

def confirmdeletestore(request, id):
    store = Store.objects.get(id = id)
    context = {'store': store}
    return render (request,"confirmdelstore.html",context)

def deletestore(request, id):
    Store.objects.get(id = id).delete()
    return redirect(storeslistview)

def edit_store_get(request, id):
        store = Store.objects.get(id = id)
        context = {'store': store}
        return render (request,"edit_store.html",context)


def edit_store_post(request, id):
        item = Store.objects.get(id = id)
        item.contactname = request.POST['contactname']
        item.address = request.POST['address']
        item.phone = request.POST['phone']
        item.email = request.POST['email']
        item.country = request.POST['country']
        item.save()
        return redirect(storeslistview)