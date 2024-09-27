# BotProject/urls.py
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from patientchat.views import add_patient, chat, chat_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', chat_view, name='chat_view'),  # API chat view
    path('add-patient/', add_patient, name='addpatient'),  # Adding patient view
]
