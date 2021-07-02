from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Category, SubCategory, Marca, UnidadMedida, Producto
from .forms import CategoryForm, SubCategoryForm, MarcaForm, UMForm, ProductoForm

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


class CategoryDelete(LoginRequiredMixin, generic.DeleteView):
    model = Category
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:categories_list')


class SubCategoryView(LoginRequiredMixin, generic.ListView):
    model = SubCategory
    template_name = 'inv/subcategories_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'


class SubCategoryNew(LoginRequiredMixin, generic.CreateView):
    model = SubCategory
    template_name = "inv/subcategory_form.html"
    context_object_name = "obj"
    form_class = SubCategoryForm
    success_url = reverse_lazy("inv:subcategories_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.user_create = self.request.user
        return super().form_valid(form)


class SubCategoryEdit(LoginRequiredMixin, generic.UpdateView):
    model = SubCategory
    template_name = "inv/subcategory_form.html"
    context_object_name = "obj"
    form_class = SubCategoryForm
    success_url = reverse_lazy("inv:subcategories_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.user_update = self.request.user.id
        return super().form_valid(form)


class SubCategoryDelete(LoginRequiredMixin, generic.DeleteView):
    model = SubCategory
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:subcategories_list')


class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = 'inv/marcas_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'


class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marcas_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.user_create = self.request.user
        return super().form_valid(form)


class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marcas_list")
    login_url = "base:login"


def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'inv/catalogos_del.html'

    if not marca:
        return redirect('inv:marcas_list')

    if request.method == 'GET':
        contexto = {'obj': marca}

    if request.method == 'POST':
        marca.status = False
        marca.save()
        return redirect('inv:marcas_list')

    return render(request, template_name, contexto)


class UMView(LoginRequiredMixin, generic.ListView):
    model = UnidadMedida
    template_name = 'inv/um_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'


class UMNew(LoginRequiredMixin, generic.CreateView):
    model = UnidadMedida
    template_name = "inv/um_form.html"
    context_object_name = "obj"
    form_class = UMForm
    success_url = reverse_lazy("inv:um_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.user_create = self.request.user
        return super().form_valid(form)


class UMEdit(LoginRequiredMixin, generic.UpdateView):
    model = UnidadMedida
    template_name = "inv/um_form.html"
    context_object_name = "obj"
    form_class = UMForm
    success_url = reverse_lazy("inv:um_list")
    login_url = "base:login"


def um_inactivar(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'inv/catalogos_del.html'

    if not um:
        return redirect('inv:um_list')

    if request.method == 'GET':
        contexto = {'obj': um}

    if request.method == 'POST':
        um.status = False
        um.save()
        return redirect('inv:um_list')

    return render(request, template_name, contexto)


class ProductosView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = 'inv/productos_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'


class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:productos_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.user_create = self.request.user
        return super().form_valid(form)
