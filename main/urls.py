from django.urls import path
from . import views

urlpatterns = [
    # front
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('news', views. news, name='news'),
    # dashboard
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/region/create', views.create_region, name='create_region'),
    path('dashboard/region/list', views.regions, name='regions'),
    path('dashboard/region/update/<int:id>/', views.region_update, name='region_update'),
    path('dashboard/region/delete/<int:id>/', views.region_delete, name='region_delete'),
    path('dashboard/category/create', views.create_category, name='create_category'),
    path('dashboard/category/list', views.categories, name='categories'),
    path('dashboard/category/update/<int:id>/', views.category_update, name='category_update'),
    path('dashboard/category/delete/<int:id>/', views.category_delete, name='category_delete'),
    path('dashboard/items/create', views.create_item, name='create_item'),
    path('dashboard/items/list', views.items, name='items'),
    path('dashboard/items/update/<int:id>/', views.update_item, name='update_item'),
    path('dashboard/items/delete/<int:id>/', views.delete_item, name='delete_item'),
    path('dashboard/form/list1/<int:id>/', views.forms, name='list1'),
    path('dashboard/form/list2/<int:id>/', views.forms2, name='list2'),
    path('dashboard/form/about/<int:id>/', views.about, name='about'),
    ]
