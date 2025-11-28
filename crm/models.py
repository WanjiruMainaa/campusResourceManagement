from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#department - organizing courses and lectureres
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

#course - linked to a department
class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.code} - {self.name}"
    
    class Meta:
        ordering = ['code']

#Lecturer - associated to department
class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']



#resourse - managing campus resource

class Resource(models.Model):
    RESOURSCE_TYPE_CHOICES = [
        ('room', 'Room'),
        ('laptop', 'Laptop'),
        ('projector', 'Projector'),
        ('lab_equipment', 'Lab_equipment'),
    ]

    name = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=20, choices=RESOURSCE_TYPE_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=50, default="Available")

    def __str__(self):
        return f"{self.name} ({self.get_resource_type_display()})"
    
    class Meta:
        ordering = ['name']


#booking - resource reservation requests
class Booking(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)
    date_needed = models.DateField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        status = "Approved" if self.approved else "Pending"
        return f"{self.resource.name} - {self.booked_by.username} ({status})"
    
    class Meta:
        ordering = ['-date_booked']

#Activities - student extra-cal activities (later)
