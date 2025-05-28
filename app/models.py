from django.db import models

class Supplier(models.Model):
    companyname = models.CharField(max_length = 50, default="firma")
    contactname = models.CharField(max_length = 50, default="firma")
    address = models.CharField(max_length = 100, default="firma")
    phone = models.CharField(max_length = 20, default="firma")
    email = models.CharField(max_length = 50, default="firma")
    country = models.CharField(max_length = 50, default="firma")
    # ao:n voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa paremmin,
    # mutta se ei ole välttämätöntä alussa
    def __str__(self):
        return f"{self.companyname} from {self.country}"



class Product(models.Model):
    productname = models.CharField(max_length = 20, default = "laku")
    packagesize = models.CharField(max_length = 20, default = 3)
    unitprice = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)
    unitsinstock = models.IntegerField(default = 3)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    # ao:n voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa hienommin,
    # mutta se ei ole välttämätöntä alussa
    def __str__(self):
        return f"{self.productname} produced by {self.supplier.companyname}"

class Employee(models.Model):
    firstname = models.CharField(max_length = 50, default="Teppo")
    lastname = models.CharField(max_length = 50, default="Testaaja")
    address = models.CharField(max_length = 100, default="katu")
    phone = models.CharField(max_length = 20, default="123")
    email = models.CharField(max_length = 50, default="sposti")
    # store = models.ForeignKey(Store, on_delete=models.CASCADE)
    # ao:n voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa paremmin,
    # mutta se ei ole välttämätöntä alussa
    def __str__(self):
        return f"{self.firstname}"

class Store(models.Model):
    storename = models.CharField(max_length = 50, default="Kauppa")
    contactname = models.CharField(max_length = 50, default="Heikki")
    address = models.CharField(max_length = 100, default="katukatu")
    phone = models.CharField(max_length = 20, default="1234")
    email = models.CharField(max_length = 50, default="sahkoposti")
    country = models.CharField(max_length = 50, default="Finland")
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # ao:n voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa paremmin,
    # mutta se ei ole välttämätöntä alussa
    def __str__(self):
        return f"{self.storename} from {self.country}"
