from django.urls import path
from .views import (
    EmployeeListCreate,
    EmployeeRetrieveUpdateDestroy,
    employee_list_html,
    employee_create_html,
    employee_edit_html,
    employee_delete_html,
    employee_search_html,
    employee_salary_update_html,
)

urlpatterns = [
    # API endpoints for Employee
    path('', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view(), name='employee-detail-update-delete'),

    # HTML page views for Employee management
    path('list/', employee_list_html, name='employee-list-html'),
    path('create/', employee_create_html, name='employee-create-html'),
    path('edit/<int:pk>/', employee_edit_html, name='employee-edit-html'),
    path('delete/<int:pk>/', employee_delete_html, name='employee-delete-html'),
    path('search/', employee_search_html, name='employee-search-html'),
    path('salary/<int:pk>/', employee_salary_update_html, name='employee-salary-update-html'),
]
