# logic.py
import spacy
import re

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

def extract_entities(message):
    doc = nlp(message)
    
    # Initialize an empty dictionary to store extracted entities
    entities = {
        'medication': None,
        'frequency': None,
        'appointment_time': None,
    }

    # Debugging: Print the message being processed
    print(f"Processing message: {message}")

    # Extract medication information (simple regex or predefined list)
    medications = ["lisinopril", "metformin", "amoxicillin"]  # Add more medications as needed
    for token in doc:
        print(f"Token: {token.text}")  # Debugging: Print each token
        if token.text.lower() in medications:
            entities['medication'] = token.text
            print(f"Found medication: {entities['medication']}")  # Debugging: Confirm found medication

    # Extract frequency (simple regex for pattern like 'twice a day', 'once a week')
    frequency_pattern = re.compile(r'\b(?:once|twice|three times|four times|daily|weekly)\b(?:\s*a\s*day|\s*a\s*week)?', re.IGNORECASE)
    frequency_match = frequency_pattern.search(message)
    if frequency_match:
        entities['frequency'] = frequency_match.group()
        print(f"Found frequency: {entities['frequency']}")  # Debugging: Confirm found frequency

    # Extract appointment time (simple example, could be more complex)
    for ent in doc.ents:
        if ent.label_ == "TIME" or ent.label_ == "DATE":
            entities['appointment_time'] = ent.text
            print(f"Found appointment time: {entities['appointment_time']}")  # Debugging: Confirm found appointment time

    print(f"Extracted entities: {entities}")  # Debugging: Print extracted entities

    return entities

   
# Process message and extract relevant entities
def process_message(message):
    print(f"Received message: {message}")  # Debugging: Print the received message
    entities = extract_entities(message)  # Extract entities

    if entities['medication']:
        response = f"I see that you're taking {entities['medication']}."
        if entities['frequency']:
            response += f" You're taking it {entities['frequency']}."
        return response

    elif "appointment" in message.lower():
        if entities['appointment_time']:
            return f"Your preferred appointment time is {entities['appointment_time']}."
        return "I will convey your request to Dr. Smith."

    else:
        return "I'm sorry, I can only help with health-related inquiries."
