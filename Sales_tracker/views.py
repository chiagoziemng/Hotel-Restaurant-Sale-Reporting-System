from django.shortcuts import render
from django.http import HttpResponse

def add_sale(request):
    if request.method == 'POST':
        # TODO: process sale data and save to database
        return HttpResponse('Sale added successfully')
    else:
        # TODO: display form to add new sale
        return render(request, 'add_sale.html')

def view_sales(request):
    # TODO: retrieve sales data from database and display in a table
    return render(request, 'view_sales.html')

def manage_inventory(request):
    # TODO: retrieve inventory data from database and display in a table
    return render(request, 'manage_inventory.html')

def manage_staff(request):
    # TODO: retrieve staff data from database and display in a table
    return render(request, 'manage_staff.html')

