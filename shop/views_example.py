from .models import Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    initial = {'name': 'Enter name'}


class ProductUpdate(UpdateView):
    model = Product
    fields = ['available']


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


