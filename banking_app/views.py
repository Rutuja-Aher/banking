from django.shortcuts import render
from db.models import Customer
from django.template import loader
from django.http import HttpResponse


def home(request):
    return render(request, 'banking/index.html')

def allCustomers(request):
    customers = Customer.objects.all().values()
    template = loader.get_template('banking/allCustomers.html')
    context = {
        "customers":customers
    }
    return HttpResponse(template.render(context,request))

def customer(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    template = loader.get_template('banking/customer.html')
    context = {
        "customer": customer
    }
    return HttpResponse(template.render(context,request))

def transfer(request):
    if request.method == 'POST':
        # Takes data from Form
        from_account_name = request.POST.get('from_account')
        to_account_name = request.POST.get('to_account')
        amount = int(request.POST.get('amount'))

        # Takes data from Customer table
        from_account = Customer.objects.get(name=from_account_name)
        to_account = Customer.objects.get(name=to_account_name)

        # Checks if the from account has sufficient balance or not
        if(from_account.balance < amount):
            print("error: Not enough money to transfer")
        else:
            # If the from account has the balance then
            # reduce the amount from from_account
            # and add it to the to_account
            from_account.balance -= amount
            to_account.balance += amount

            # Lastly save new balance to the Customer table
            from_account.save()
            to_account.save()
            print("successfully transfer")
        
    customers = Customer.objects.all()  
    customer_names = [customer.name for customer in customers]

    context = {
        "customer_names": customer_names
    }
    
    return render(request, 'banking/transfer.html', context)