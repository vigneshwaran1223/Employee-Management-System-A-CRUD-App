from django.db import models

# Create your models here.
class RegisterForm(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    designation = models.CharField(max_length=100)
    salary = models.BigIntegerField()
    email = models.EmailField()
    mobile = models.BigIntegerField()

class Meta:
    db_table = 'employee_details'    