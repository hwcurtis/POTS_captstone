import pandas as pd

data = {
    "Category": [
        "Summary",
        "Diagnosis Criteria",
        "Common Symptoms",
        "Functional Impact",
        "History",
        "Classifications",
        "Demographics",
        "Known Causes",
        "Treatment",
        "Prognosis"
    ],
    "Information": [
        "Postural Orthostatic Tachycardia Syndrome (POTS) is a form of dysautonomia...",
        "Heart rate increase of 30 bpm or more (40 bpm in children) within 10 minutes of standing...",
        "Fatigue, headaches, lightheadedness, heart palpitations...",
        "25% disabled; often misdiagnosed as anxiety...",
        "Coined in 1993 by Mayo Clinic; formerly known as DaCosta's Syndrome, etc.",
        "Primary/Secondary POTS, Neuropathic, Hypovolemic, Hyperadrenergic...",
        "Most common in women aged 15-50; affects 500k-1M Americans...",
        "Autoimmune disease, infections, genetic disorders, trauma, etc.",
        "Fluids, salt, compression stockings, meds like Fludrocortisone...",
        "Varies by patient; some recover in 2-5 years, others see lifelong symptoms..."
    ]
}

df = pd.DataFrame(data)
print(df)

# Save the DataFrame to a CSV file
df.to_csv("pots_dataset.csv", index=False)
