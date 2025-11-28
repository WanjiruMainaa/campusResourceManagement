from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Department, Lecturer, Course, Resource, Booking

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']
        widgets = { 
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'department', 'code']
        widgets = { 
            'department': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['name', 'department', 'email']
        widgets = { 
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'department', 'resource_type', 'status']
        widgets = { 
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'resource_type': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['resource', 'date_needed']
        widgets = { 
            'resource': forms.Select(attrs={'class': 'form-control'}),
            'date_needed': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, required= False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required= False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name' 'password1', 'password2']
        widgets = { 
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password1'].widget.attrs.update({'class': 'form-control'})
            self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    
