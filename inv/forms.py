from django import forms
from .models import Category, SubCategory, Marca, UnidadMedida, Producto


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['description', 'status']
        labels = {'description': 'Descripciòn de la Categoria',
                  'status': 'Estatus'}
        widgets = {'description': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class SubCategoryForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.filter(status=True).order_by('description')
    )

    class Meta:
        model = SubCategory
        fields = ['category', 'description', 'status']
        labels = {'description': 'Sub-Categoria',
                  'status': 'Estatus'}
        widgets = {'description': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['category'].empty_label = "Selecione Categoria"


class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = ['description', 'status']
        labels = {'description': 'Marca',
                  'status': 'Estatus'}
        widgets = {'description': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class UMForm(forms.ModelForm):

    class Meta:
        model = UnidadMedida
        fields = ['description', 'status']
        labels = {'description': 'Unidad de Medida',
                  'status': 'Estatus'}
        widgets = {'description': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['codigo', 'codigo_barras', 'descripcion', 'status', 'precio', 'existencia', 'ultima_compra',
                  'marca', 'subcategoria', 'unidad_medida']
        widgets = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True
