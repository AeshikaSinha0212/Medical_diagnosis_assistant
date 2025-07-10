8# 🏥 Medical Diagnosis Assistant

This is a beginner-friendly Python project that mimics a basic healthcare assistant. It takes symptoms as input and provides possible illness prediction, risk level, and medical advice — all based on basic logic and real-world relevance.
---
## 📌 Features

- 📋 Analyze symptoms for multiple patients  
- 🩺 Detect common illnesses like Dengue, COVID-19, Cold, etc.  
- ⚠️ Displays health **risk level** and medical **advice**  
- 👩‍💻 Beginner-friendly and easy to customize  
- 🔁 Modular structure using separate patient data file  

---

## 📁 Project Structure
📦 medical-diagnosis-assistant/
├── medical_diagnosis_assistant.py   # 💉 Main logic to detect illness based on symptoms
├── patients_data.py                 # 👥 Contains multiple patient data and symptoms
├── README.md                        # 📘 Project documentation with badges & usage info
├── LICENSE                          # 📄 MIT License for open-source usage
└── __pycache__/                     # ⚙️ Auto-generated Python cache files (can be ignored)

## 📁 Files Included

- `medical_diagnosis_assistant.py` → Main program logic
- `patients_data.py` → List of patients with symptoms
- `README.md` → Documentation
- `LICENSE` → MIT License

## ▶️ How to Run

1. Make sure you have Python installed.
2. Save all files in the same folder.
3. Run the program:
```bash
python medical_diagnosis_assistant.py
```
## 💡 Sample Output
Here’s how the program displays diagnosis details for each patient based on their symptoms:
```
👤 Patient: Iris (29 yrs)
🩺 Symptoms: High Fever, Headache, Joint Pain, Skin Rash
📘 Possible Illness: Dengue
⚠️ Risk Level: High
💡 Advice: Please visit a hospital immediately for a blood test and hydration treatment.

...

## 🎯 Ideal For

- Beginners learning conditional logic
- Simple real-world problem simulation
