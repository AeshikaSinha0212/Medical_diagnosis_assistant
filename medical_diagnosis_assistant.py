from patients_data import patients

def diagnose(symptoms):
    symptoms = [s.lower() for s in symptoms]
    if all(s in symptoms for s in ['fever', 'headache', 'joint pain', 'skin rash']):
        return 'Dengue', 'High', 'Please visit a hospital immediately for a blood test and hydration treatment.'
    elif all(s in symptoms for s in ['cough', 'fever', 'shortness of breath']):
        return 'COVID-19', 'High', 'Isolate yourself and get an RT-PCR test done as soon as possible.'
    elif all(s in symptoms for s in ['sore throat', 'runny nose', 'sneezing']):
        return 'Common Cold', 'Low', 'Stay hydrated and rest. Take paracetamol if required.'
    elif all(s in symptoms for s in ['vomiting', 'diarrhea', 'abdominal pain']):
        return 'Food Poisoning', 'Moderate', 'Take ORS and light food. Consult doctor if symptoms persist.'
    elif all(s in symptoms for s in ['itchy eyes', 'sneezing', 'runny nose']):
        return 'Allergy', 'Low', 'Avoid allergens. Antihistamines may help.'
    else:
        return 'Unknown', 'Uncertain', 'Please consult a doctor for further diagnosis.'

for patient in patients:
    name = patient['name']
    age = patient['age']
    symptoms = patient['symptoms']
    illness, risk, advice = diagnose(symptoms)

    print(f"\n👤 Patient: {name} ({age} yrs)")
    print(f"🩺 Symptoms: {', '.join(symptoms)}")
    print(f"📘 Possible Illness: {illness}")
    print(f"⚠️ Risk Level: {risk}")
    print(f"💡 Advice: {advice}")
