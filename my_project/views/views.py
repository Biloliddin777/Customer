from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from my_project.models import Customer
from my_project.forms import CustomerModelForm


# Create your views here.


def project_management(request):
    return render(request, 'my_project/project-management.html')


def customers(request):
    search_query = request.GET.get('search', '')
    customers = Customer.objects.all()
    if search_query:
        customers = customers.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query)
        )

    context = {'customers': customers}
    return render(request, 'my_project/customers.html', context)


def customer_details(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    context = {'customer': customer}
    return render(request, 'my_project/customer-details.html', context)


def profile(request):
    return render(request, 'my_project/profile.html')


def profile_settings(request):
    return render(request, 'my_project/settings.html')


def add_customer(request):
    if request.method == 'POST':
        form = CustomerModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CustomerModelForm()

    context = {'form': form}
    return render(request, 'my_project/add-customer.html', context)


def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == 'POST':
        form = CustomerModelForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CustomerModelForm(instance=customer)

    context = {'form': form}
    return render(request, 'my_project/edit-customer.html', context)


def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == "POST":
        customer.delete()
        return redirect('customers')

    return render(request, 'my_project/delete-customer.html', {'customer': customer})
