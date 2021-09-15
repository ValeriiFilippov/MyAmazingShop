from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import MyUserCreateForm


class RegisterFormView(FormView):
    form_class = MyUserCreateForm
    success_url = 'login/'

    template_name = 'accounts/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)

