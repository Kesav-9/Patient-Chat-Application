# patient_chat/models.py
from django.db import models # type: ignore

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    medical_condition = models.CharField(max_length=255)
    medication_regimen = models.TextField()
    last_appointment = models.DateTimeField(null=True, blank=True)  # Allow null values
    next_appointment = models.DateTimeField()
    doctor_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
