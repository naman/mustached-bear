from django.db import models

# Create your models here.
class Employee(models.Model):
        employee_no = models.IntgerField(primary_key=True)
        fname = models.CharField(max_length=50)
        lname = models.CharField(max_length = 50)
        zip = models.IntegerField(max_length=6, null = True)

class Customer(models.Model):
    customer_no = models.IntgerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length = 50)
    zip = models.IntegerField(max_length=6, null = True)

class Part(models.Model):
    part_no = models.IntgerField(primary_key=True)
    pname = models.CharField(max_length = 20)
    price = models.IntgerField(max_length=4)
    max_quantity = models.IntegerField(max_length=4) #This is the stock quantity for every part

class Order(models.Model):
    order_no = models.IntgerField(primary_key = True)
    employee = models.ForeignKey(Employee)
    customer = models.ForeignKey(Customer)
    recv_date = models.DateTimeField()
    ship_date = models.DateTimeField()

class Order_Part_Quantity(models.Model):
    order_no = models.ForeignKey(Order)
    part_quantity = models.IntgerField()
    part_no = models.ForeignKey(Part)
