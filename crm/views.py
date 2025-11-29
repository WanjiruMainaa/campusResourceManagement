from django.shortcuts import render, redirect
from .forms import DepartmentForm, CourseForm, LecturerForm, ResourceForm, BookingForm, CustomUserCreationForm
from .models import Department, Course, Lecturer, Resource, Booking
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'crm/home.html')

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "registration successfull please login")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request,'crm/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.GET('username')
        password = request.POST.GET('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request, "Welcome, {user.username}")
            return redirect('home')
        else:
            messages.error(request, "Invalid udername or password")
    return render(request,'crm/login.html')

# Department CRUD operations

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'crm/department_list.html',{'departments': departments})

def department_create(request):
    form = DepartmentForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Department created successfully")
        return redirect('department_list')
    return render(request,'crm/department_form.html', {'form': form})

def department_update(request, pk):
    department = Department.objects.get(id=pk)
    form = DepartmentForm(request.POST, instance=department)
    if form.is_valid():
        form.save()
        messages.success(request, "Department updated")
        return redirect('department_list')
    return render(request, 'crm/department_form.html', {'form': form})

def department_delete(request, pk):
    department = Department.objects.get(id=pk)
    if request.method == "POST":
        department.delete()
        messages.success(request, "Department deleted sucessfully")
        return redirect('department_list')
    return render(request, 'confirm_delete.html', {'object': department})

# Course CRUD operations

def course_list(request):
    courses = Course.objects.select_related('department').all()
    return render(request, 'crm/course_list.html', {'courses': courses})

def course_create(request):
    form = CourseForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Course added successfully")
        return redirect('course_list')
    return render(request,'crm/course_form.html', {'form': form})

def course_update(request, pk):
    course = Course.objects.get(id=pk)
    form = DepartmentForm(request.POST, instance=course)
    if form.is_valid():
        form.save()
        messages.success(request, "Course updated")
        return redirect('course_list')
    return render(request, 'crm/course_form.html', {'form': form})

def course_delete(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course deleted sucessfully")
        return redirect('course_list')
    return render(request, 'confirm_delete.html', {'object': course})

# Lecturer CRUD operations

def lecturer_list(request):
    lecturers = Lecturer.objects.select_related('department').all()
    return render(request, 'crm/lecturer_list.html', {'lecturers', lecturers})

def lecturer_create(request):
    form = LecturerForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Lecturer added successfully")
        return redirect('lecturer_list')
    return render(request,'crm/lecturer_form.html', {'form': form})

def lecturer_update(request, pk):
    lecturer = Lecturer.objects.get(id=pk)
    form = LecturerForm(request.POST, instance=lecturer)
    if form.is_valid():
        form.save()
        messages.success(request, "Lecturer updated")
        return redirect('lecturer_list')
    return render(request, 'crm/lecturer_form.html', {'form': form})

def lecturer_delete(request, pk):
    lecturer = Lecturer.objects.get(id=pk)
    if request.method == "POST":
        lecturer.delete()
        messages.success(request, "Lecturer removed sucessfully")
        return redirect('lecturer_list')
    return render(request, 'confirm_delete.html', {'object': lecturer})

# Resource CRUD operations

def resource_list(request):
    resources = Resource.objects.select_related('department').all()
    return render(request, 'crm/resource_list.html', {'resources', resources})

def resource_create(request):
    form = ResourceForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Resource created successfully")
        return redirect('resource_list')
    return render(request,'crm/resource_form.html', {'form': form})

def resource_update(request, pk):
    resource = Resource.objects.get(id=pk)
    form = ResourceForm(request.POST, instance=resource)
    if form.is_valid():
        form.save()
        messages.success(request, "Resource updated")
        return redirect('resource_list')
    return render(request, 'crm/resource_form.html', {'form': form})

def resource_delete(request, pk):
    resource = Resource.objects.get(id=pk)
    if request.method == "POST":
        resource.delete()
        messages.success(request, "Resource removed sucessfully")
        return redirect('resource_list')
    return render(request, 'confirm_delete.html', {'object': resource})

# Booking CRUD operations
def booking_list(request):
    bookings = Booking.objects.select_related('resource', 'booked_by').all()
    return render(request, 'crm/booking_list.html', {'bookings': bookings})

def booking_create(request):
    form = BookingForm(request.POST)
    if form.is_valid():
        booking = form.save(commit=False)
        booking.booked_by = request.user
        booking.save()
        messages.success(request, "Booking request received")
        return redirect('booking_list')
    return render(request,'crm/booking_form.html', {'form': form})

def booking_approve(request, pk):
    booking = Booking.objects.get(id=pk)
    booking.approved = True
    booking.save()
    messages.success(request, "Booking approved.")
    return redirect('booking_list')


def booking_delete(request, pk):
    booking = Booking.objects.get(id=pk)
    if request.method == "POST":
        booking.delete()
        messages.success(request, "Booking removed sucessfully")
        return redirect('booking_list')
    return render(request, 'confirm_delete.html', {'object': booking})