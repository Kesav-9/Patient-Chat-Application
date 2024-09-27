# patient_chat/admin.py
from django.contrib import admin # type: ignore
from .models import Patient

admin.site.register(Patient)
