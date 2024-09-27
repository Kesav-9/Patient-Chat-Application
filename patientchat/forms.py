# patient_chat/forms.py
from django import forms # type: ignore
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 
                  'medical_condition', 'medication_regimen', 'last_appointment', 
                  'next_appointment', 'doctor_name']
