from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from patientchat.chatbot.logic import process_message  # Correct import path
from django.views import View

@csrf_exempt
@csrf_exempt
def chat_view(request, patient_id=None):
    """
    Chat view:
    If a patient ID is provided, show the specific patient's chat.
    If no patient ID is provided, fetch all patients and display options.
    """
    if request.method == 'POST':
        # Handling chat messages
        data = json.loads(request.body)
        user_message = data.get('message')

        if patient_id:  # If a specific patient is selected
            response = process_message(user_message)  # Process the user's message
            return JsonResponse({'response': response})  # Return the AI response as JSON

        # If patient_id is not provided
        return JsonResponse({'error': 'Patient ID required for chat.'}, status=400)

    # Handle GET requests
    if patient_id:
        # Retrieve specific patient by ID
        patient = get_object_or_404(Patient, id=patient_id)
        return render(request, 'chat.html', {'patient': patient})

    # Fetch all patients and list them if no specific patient is selected
    patients = Patient.objects.all()
    return render(request, 'chat.html', {'patients': patients})

    

def process_message(message):
    """
    A simple bot response logic based on message content.
    Extend this logic as needed for more complex conversations.
    """
    if "medication" in message.lower():
        return "Please tell me more about your medication."
    elif "appointment" in message.lower():
        return "I will convey your request to Dr. Smith."
    else:
        return "I'm sorry, I can only help with health-related inquiries."
    
def ai_bot_response(message):
    # Simple AI bot logic for demo purposes
    keywords = {
        "appointment": "I will convey your request to Dr.",
        "medication": "Please let me know what changes you want for your medication.",
        "diet": "For dietary advice, please consult Dr.",
    }

    for keyword, response in keywords.items():
        if keyword in message.lower():
            return response
    return "I'm sorry, I can only answer health-related questions."

def is_health_related(message):
    health_keywords = [
        "health", "doctor", "medication", "diet", "condition", "exercise",
        "appointment", "treatment", "lifestyle", "reschedule", "symptoms"
    ]
    
    message_lower = message.lower()
    
    if any(keyword in message_lower for keyword in health_keywords):
        return True
    return False

def add_patient(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        doctor_name = request.POST.get('doctor_name')
        next_appointment = request.POST.get('next_appointment')
        date_of_birth = request.POST.get('date_of_birth')
        last_appointment = request.POST.get('last_appointment')

        # Ensure all required fields are provided
        if first_name and last_name and doctor_name and next_appointment and date_of_birth:
            # Create and save the patient instance
            Patient.objects.create(
                first_name=first_name,
                last_name=last_name,
                doctor_name=doctor_name,
                next_appointment=next_appointment,
                date_of_birth=date_of_birth,
                last_appointment=last_appointment
            )
            return redirect('chat')  # Redirect to chat page
        else:
            return HttpResponse("All fields are required.")

    return render(request, 'add_patient.html')  # Render the patient form template
class ChatView(View):
    def post(self, request, *args, **kwargs):
        message = request.POST.get('message')  # Adjust to match your form data
        if not message:
            return JsonResponse({"error": "No message provided"}, status=400)

        response = process_message(message)
        return JsonResponse({"response": response})