from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.
def customer_home(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_home.html', {'customers':customers})


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer/details_view.html'
    context_object_name = 'customer'


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer/create.html'

    form_class = CustomerForm


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = '/customer/'
    template_name = 'customer/customer-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_home')
        else:
            error = 'Incorect input'

    form = CustomerForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'customer/create.html', data)