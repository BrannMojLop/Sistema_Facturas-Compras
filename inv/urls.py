from django.urls import path
from .views import CategoryEdit, CategoryView, CategoryEdit, CategoryNew

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories_list'),
    path('categories/new', CategoryNew.as_view(), name='category_new'),
    path('categories/edit/<int:pk>', CategoryEdit.as_view(), name='category_edit')
]
