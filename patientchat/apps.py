import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(message):
    doc = nlp(message)
    entities = {}
    for ent in doc.ents:
        if ent.label_ in ["DATE", "TIME"]:
            entities['appointment_time'] = ent.text
        elif ent.label_ == "DRUG":
            entities['medication'] = ent.text
        # Add more entity types as needed
    return entities
