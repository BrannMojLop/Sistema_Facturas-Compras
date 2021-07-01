from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Category
from .forms import CategoryForm

# Create your views here.


class CategoryView(LoginRequiredMixin, generic.ListView):
    model = Category
    template_name = 'inv/categories_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'


class CategoryNew(LoginRequiredMixin, generic.CreateView):
    model = Category
    template_name = "inv/category_form.html"
    context_object_name = "obj"
    form_class = CategoryForm
    success_url = reverse_lazy("inv:categories_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.user_create = self.request.user
        return super().form_valid(form)


class CategoryEdit(LoginRequiredMixin, generic.UpdateView):
    model = Category
    template_name = "inv/category_form.html"
    context_object_name = "obj"
    form_class = CategoryForm
    success_url = reverse_lazy("inv:categories_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.user_update = self.request.user.id
        return super().form_valid(form)
