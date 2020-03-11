from django.urls import path
from . import views

urlpatterns = [
    path('persons-list/', views.persons_list, name='persons_list'),
    path('persons-create/', views.persons_create, name='persons_create'),
    path('persons-update/<int:id>', views.persons_update, name='persons_update'),
    path('persons-delete/<int:id>', views.persons_delete, name='persons_delete'),

    path('users-list/', views.users_list, name='users_list'),
    path('users-create/', views.users_create, name='users_create'),
    path('users-update/<int:id>/', views.users_update, name='users_update'),
    path('users-delete/<int:id>', views.users_delete, name='users_delete'),
]