from django.http import HttpResponse
from django.shortcuts import render, redirect # To render HTML and redirect!
from datetime import datetime # To use for date_added field 
from models import Brand, Product # MUST import tables to use!

# Loads /products page
def index(request):
	brands = Brand.objects.all();
	products = Product.objects.all();
	context = {
		# "brands" will be the key called for in index.html to access all the brands we queried
		"brands": brands,
		# "products" will be the key called for in index.html to access all the products we queried
		"products": products,
	}
	return render(request, 'inventory/index.html', context)

# Adds new product
def add(request):
	# Because Brand is another table with relationship to Product, we must establish which brand first!
	b = Brand.objects.get(brand_name=request.POST['brand_name'])
	# request.POST['key'] fills in with whatever user input in form
	Product.objects.create(brand=b, name=request.POST['name'], price=request.POST['price'], date_added=datetime.now(), description=request.POST['description'])
	return redirect('/products')

# Deletes product
def delete(request, id):
	# Selects specific product with that ID which was passed from form
	p = Product.objects.get(id=id)
	p.delete()
	return redirect('/products')

# Loads /edit/id page
def edit(request, id):
	context = {
	# by setting up the specific Product selected, and all brands in advance, we can utilize this date in the edit.html
		"product": Product.objects.get(id=id),
		"brands": Brand.objects.all(),
	}
	return render(request, 'inventory/edit.html', context)

# Updates changes and redirects to /products
def update(request, id):
	# Again, because Product is separate table with relationship to Brand, we set up Brand first to access properly
	b = Brand.objects.get(brand_name=request.POST['brand_name'])
	p = Product.objects.get(id=id)
	p.brand = b
	p.name = request.POST['name']
	p.price = request.POST['price']
	p.description = request.POST['description']
	p.save()
	return redirect('/products')