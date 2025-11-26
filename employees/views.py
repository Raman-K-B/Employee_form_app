from rest_framework import generics
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Employee
from .serializers import EmployeeSerializer
from .forms import EmployeeForm


class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


def employee_list_html(request):
    query = request.GET.get('q')
    employees = Employee.objects.all()
    if query:
        employees = employees.filter(name__icontains=query) | employees.filter(position__icontains=query)

    from django.core.paginator import Paginator
    paginator = Paginator(employees, 10)
    page_number = request.GET.get('page')
    employees = paginator.get_page(page_number)
    return render(request, 'employees/employee_list.html', {'employees': employees, 'query': query})


def employee_create_html(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee-list-html')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_create.html', {'form': form})


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


def employee_delete_html(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee-list-html')
    return render(request, 'employees/employee_delete.html', {'employee': employee})


def employee_search_html(request):
    eid = request.GET.get('eid')
    employee = None
    if eid:
        employee = Employee.objects.filter(eid=eid).first()
    return render(request, 'employees/employee_search.html', {'employee': employee, 'eid': eid})


# New salary update view
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
