from django.shortcuts import render
from .models import Employee, Customer, Part, Order, Order_Part_Quantity
from .forms import EmployeeForm, CustomerForm, PartForm, OrderForm, OrderPartQuantityForm 
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
	customers = Customer.objects.all()
	employees = Employee.objects.all()
	orders = Order.objects.all()
	context = {'employees':employees, 'customers':customers, 'orders':orders}
	return render(request, 'app/index.html', context)


def newcustomer(request):
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			usr = form.save(commit=False)
			usr.save()
			return HttpResponseRedirect('/')
	elif request.method == 'GET':
			studentform = CustomerForm()
			context = {'form': studentform}
			return render(request, 'app/customer.html', context)
	return HttpResponseRedirect('/')


def customer_edit(request, cid):
	if request.method == 'POST':
		form = CustomerForm(request.POST, instance=Customer.objects.get(pk=cid))
		if form.is_valid():
			usr = form.save(commit=False)
			usr.save()
			return HttpResponseRedirect('/')
	elif request.method == 'GET':
			studentform = CustomerForm(instance=Customer.objects.get(pk=cid))
			context = {'form': studentform}
			return render(request, 'app/customer.html', context)
	return HttpResponseRedirect('/')


def customer_delete(request, cid):
	Customer.objects.get(pk=cid).delete()
	return render(request, 'app/delete.html')


def newemployee(request):
	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			usr = form.save(commit=False)
			usr.save()
			return HttpResponseRedirect('/')
	elif request.method == 'GET':
			studentform = EmployeeForm()
			context = {'form': studentform}
			return render(request, 'app/employee.html', context)
	return HttpResponseRedirect('/')

def employee_edit(request, eid):
	if request.method == 'POST':
		form = EmployeeForm(request.POST, instance=Employee.objects.get(pk=eid))
		if form.is_valid():
			usr = form.save(commit=False)
			usr.save()
			return HttpResponseRedirect('/')
	elif request.method == 'GET':
			studentform = EmployeeForm(instance=Employee.objects.get(pk=eid))
			context = {'form': studentform}
			return render(request, 'app/employee.html', context)
	return HttpResponseRedirect('/')

def employee_delete(request, eid):
	Employee.objects.get(pk=eid).delete()
	return render(request, 'app/delete.html')


def neworder(request):
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			usr = form.save(commit=False)
			usr.save()
			return HttpResponseRedirect('/')
	elif request.method == 'GET':
			studentform = OrderForm()
			context = {'form': studentform}
			return render(request, 'app/order.html', context)
	return HttpResponseRedirect('/')

def order_edit(request, oid):	
	if request.method == 'POST':
		form = OrderForm(request.POST, instance=Order.objects.get(pk=oid))
		if form.is_valid():
			usr = form.save(commit=False)
			usr.save()
			return HttpResponseRedirect('/')
	elif request.method == 'GET':
			studentform = OrderForm(instance=Order.objects.get(pk=oid))
			context = {'form': studentform}
			return render(request, 'app/order.html', context)
	return HttpResponseRedirect('/')

def order_delete(request, oid):
	Order.objects.get(pk=oid).delete()
	return render(request, 'app/delete.html')


def query(request):
	return render(request, 'app/query.html')
