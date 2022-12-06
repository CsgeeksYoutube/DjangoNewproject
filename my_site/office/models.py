from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinLengthValidator(0),MaxLengthValidator(100)])
    bp= models.IntegerField(default=80,validators=[MinLengthValidator(80),MaxLengthValidator(120)])
    
    def __str__(self):
        return f"{self.first_name}, {self.last_name} is {self.age} year old"
