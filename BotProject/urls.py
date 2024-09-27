from django.urls import path
from patientchat.views import add_patient, chat_view
from django.contrib import admin


urlpatterns = [
    path('add_patient/', add_patient, name='add_patient'),  # Path to add patient
    path('chat/<int:patient_id>/', chat_view, name='chat_with_patient'),  # Chat view for specific patient
    path('chat/', chat_view, name='chat'),  # Chat view for all patients or without ID
    path('admin/', admin.site.urls),

]
