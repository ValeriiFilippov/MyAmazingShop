from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views.generic.edit import FormView
from .forms import MyUserCreateForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {'category': category,
               'categories': categories,
               'products': products}

    return render(request, 'shop/product/list.html', context=context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)

    cart_form = CartAddProductForm()
    context = {'product': product,
               'cart_product_form': cart_form}

    return render(request, 'shop/product/detail.html', context=context)


class RegisterFormView(FormView):
    form_class = MyUserCreateForm
    success_url = 'login/'

    template_name = 'shop/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)