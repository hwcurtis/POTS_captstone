
import pandas as pd

data = {
    "Orthostatic": {
        "Light-headedness or dizziness": 77.6,
        "Pre-syncope": 60.5,
        "Weakness": 50,
        "Palpitations": 75,
        "Tremulousness": 37.5,
        "Shortness of breath": 27.6,
        "Chest pain": 24.3,
        "Loss of sweating": 5.3,
        "Hyperhidrosis": 9.2
    },
    "Non-orthostatic": {
        "Bloating": 23.7,
        "Nausea": 38.8,
        "Vomiting": 8.6,
        "Abdominal pain": 15.1,
        "Constipation": 15.1,
        "Diarrhoea": 17.8,
        "Bladder dysfunction": 9.2,
        "Pupillary dysfunction": 3.3
    },
    "Generalized": {
        "Fatigue": 48,
        "Sleep disturbance": 31.6,
        "Migraine headache": 27.6,
        "Myofascial pain": 15.8,
        "Neuropathic pain": 2
    }
}


print(data["Orthostatic"]["Palpitations"])  # Output: 75

for category, symptoms in data.items():
    print(f"\n{category} symptoms:")
    for symptom, prevalence in symptoms.items():
        print(f"  - {symptom}: {prevalence}%")

# Convert the nested dictionary to a DataFrame
df = pd.DataFrame.from_dict(data, orient='index').transpose()

# Print all symptoms and their frequencies by category
for category in df.columns:
    print(f"\n{category}:")
    for symptom, freq in df[category].dropna().items():
        print(f"  {symptom}: {freq}%")
