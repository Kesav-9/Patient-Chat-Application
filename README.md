# AI Health Chatbot

This is a Django-based AI chatbot that assists patients with health-related inquiries, including rescheduling appointments, discussing medication, and providing general health advice. The bot responds only to health-related topics and filters out unrelated or sensitive queries. Additionally, the chatbot can extract key entities such as appointment times and medication details and handle them accordingly.

## Features
- Responds to health-related queries (medication, appointments, general health).
- Filters out non-health-related topics.
- Handles patient requests for appointment rescheduling.
- Extracts key entities like medication and appointment time from conversations.
- Displays action messages related to appointment changes.

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, JavaScript (Fetch API)
- **Natural Language Processing (NLP):** spaCy for entity extraction (medication, appointment time)
- **Database:** SQLite (default Django setup)
- **Other Libraries:** 
  - `spaCy` (for entity extraction)
  - `re` (Python's regex module for basic pattern matching)

## Prerequisites

Make sure you have the following installed on your machine:
- Python 3.x
- Django 4.x (or the latest stable version)
- spaCy NLP library
- pip (Python package manager)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-health-chatbot.git
cd ai-health-chatbot

Commands
pip install -r requirements.txt
pip install django spacy
python -m spacy download en_core_web_sm
python manage.py migrate
python manage.py runserver

