from rest_framework import generics
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.core.paginator import Paginator
from .models import Employee
from .serializers import EmployeeSerializer
from .forms import EmployeeForm


# API Views for Employee: List/Create and Retrieve/Update/Delete
class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# HTML View: List employees with optional search and pagination
def employee_list_html(request):
    query = request.GET.get('q')
    employees = Employee.objects.all()
    if query:
        employees = employees.filter(name__icontains=query) | employees.filter(position__icontains=query)

    paginator = Paginator(employees, 10)  # Show 10 employees per page
    page_number = request.GET.get('page')
    employees = paginator.get_page(page_number)

    return render(request, 'employees/employee_list.html', {'employees': employees, 'query': query})


# HTML View: Create new employee
def employee_create_html(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee-list-html')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_create.html', {'form': form})


# HTML View: Edit existing employee
def employee_edit_html(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee-list-html')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_edit.html', {'form': form, 'employee': employee})


# HTML View: Delete employee confirmation and action
def employee_delete_html(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee-list-html')
    return render(request, 'employees/employee_delete.html', {'employee': employee})


# HTML View: Search employee by employee ID
def employee_search_html(request):
    eid = request.GET.get('eid')
    employee = Employee.objects.filter(eid=eid).first() if eid else None
    return render(request, 'employees/employee_search.html', {'employee': employee, 'eid': eid})


# HTML View: Update employee salary
def employee_salary_update_html(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    class SalaryForm(forms.ModelForm):
        class Meta:
            model = Employee
            fields = ['salary']

    if request.method == 'POST':
        form = SalaryForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee-list-html')
    else:
        form = SalaryForm(instance=employee)

    return render(request, 'employees/employee_salary.html', {'form': form, 'employee': employee})
