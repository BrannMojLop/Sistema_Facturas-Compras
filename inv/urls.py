from django.urls import path
from .views import CategoryView, CategoryNew

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories_list'),
    path('categories/new', CategoryNew.as_view(), name='category_new')
]
