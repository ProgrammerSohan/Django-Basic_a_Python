from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.first_name, self.last_name
      # return f"{self.first_name} {self.last_name} {self.photo} { self.designation} {self.email_address} {self.phone_number} {self.created_at} {self.updated_at}"
      # return f"{self.first_name} {self.last_name} | Photo: {self.photo.url} | Designation: {self.designation} | Email: {self.email_address} | Phone: {self.phone_number} | Created: {self.created_at} | Updated: {self.updated_at}"