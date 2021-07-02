from django.urls import path
from .views import CategoryNew, CategoryEdit, CategoryView, CategoryDelete, SubCategoryView, SubCategoryNew, SubCategoryEdit, SubCategoryDelete, MarcaView, MarcaEdit, MarcaNew, marca_inactivar, UMView, UMNew, UMEdit, um_inactivar, ProductosView, ProductoNew

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories_list'),
    path('categories/new', CategoryNew.as_view(), name='category_new'),
    path('categories/edit/<int:pk>', CategoryEdit.as_view(), name='category_edit'),
    path('categories/delete/<int:pk>',
         CategoryDelete.as_view(), name='category_del'),

    path('subcategories/', SubCategoryView.as_view(), name='subcategories_list'),
    path('subcategories/new', SubCategoryNew.as_view(), name='subcategory_new'),
    path('subcategories/edit/<int:pk>',
         SubCategoryEdit.as_view(), name='subcategory_edit'),
    path('subcategories/delete/<int:pk>',
         SubCategoryDelete.as_view(), name='subcategory_del'),

    path('marcas/', MarcaView.as_view(), name='marcas_list'),
    path('marca/new', MarcaNew.as_view(), name='marca_new'),
    path('marca/edit/<int:pk>',
         MarcaEdit.as_view(), name='marca_edit'),
    path('marca/inactivar/<int:id>',
         marca_inactivar, name='marca_inactivar'),


    path('um/', UMView.as_view(), name='um_list'),
    path('um/new', UMNew.as_view(), name='um_new'),
    path('um/edit/<int:pk>',
         UMEdit.as_view(), name='um_edit'),
    path('um/inactivar/<int:id>',
         um_inactivar, name='um_inactivar'),

    path('productos/', ProductosView.as_view(), name='productos_list'),
    path('producto/new', ProductoNew.as_view(), name='producto_new'),
]
