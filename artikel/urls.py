from django.urls import path
from artikel.views import *

urlpatterns = [
    path('artikel/list', artikel_list, name="artikel_list"),
    path('artikel/tambah', artikel_tambah, name="artikel_tambah"),
    path('artikel/update/<int:id_artikel>', artikel_update, name="artikel_update"),
    path('artikel/delete/<int:id_artikel>', artikel_delete, name="artikel_delete"),

    # operator #
    path('operator/kategori/list', admin_kategori_list, name="admin_kategori_list"),
    path('operator/kategori/tambah', admin_kategori_tambah, name="admin_kategori_tambah"),
    path('operator/kategori/update/<int:id_kategori>', admin_kategori_update, name="admin_kategori_update"),
    path('operator/kategori/delete/<int:id_kategori>', admin_kategori_delete, name="admin_kategori_delete"),

    path('operator/artikel/list', admin_artikel_list, name="admin_artikel_list"),
    path('operator/artikel/tambah', admin_artikel_tambah, name="admin_artikel_tambah"),
    path('operator/artikel/update/<int:id_artikel>', admin_artikel_update, name="admin_artikel_update"),
    path('operator/artikel/delete/<int:id_artikel>', admin_artikel_delete, name="admin_artikel_delete"),

    path('operator/management-list/list', admin_management_user_list, name="admin_management_user_list"),
    path('operator/management-edit/edit<int:user_id>', admin_management_user_edit, name="admin_management_user_edit"),
]