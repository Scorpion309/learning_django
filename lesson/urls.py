from django.contrib import admin
from django.urls import path
from . import views

app_name = 'lesson'

urlpatterns = [
    # path('', views.all_materials, name='all_materials'),
    path('', views.MaterialListView.as_view(), name='all_materials'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>',
         views.material_details, name='material_details'),
    path('<int:material_id>/share/', views.share_material,
         name='share_material'),
    path('create/', views.create_form, name='create_form'),
    path('login/', views.user_login, name='login'),
]