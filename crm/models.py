from django.db import models

# Create your models here.

#department - organizing courses and lectureres
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        return True
    







#course - linked to a department

#Lecturer - associated to department

#resourse - managing campus resources

#Activities - student extra-cal activities

#booking - resource reservation requests