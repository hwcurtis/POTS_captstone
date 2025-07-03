import pandas as pd

# Creating a structured summary of POTS from the provided content
data = {
    "Category": [
        "Definition",
        "Diagnostic Criteria",
        "Diagnostic Methods",
        "Common Symptoms",
        "Symptom Severity",
        "Misdiagnosis Risk",
        "History",
        "Subtypes",
        "Demographics",
        "Estimated Prevalence",
        "Causes (Partial List)",
        "Common Treatments",
        "Medications Used",
        "Prognosis"
    ],
    "Details": [
        "POTS is a form of dysautonomia characterized by excessive tachycardia upon standing.",
        "≥30 bpm HR increase in adults; ≥40 bpm in children within 10 minutes of standing or HR >120 bpm.",
        "Tilt Table Test or bedside HR/BP measurements at 2, 5, and 10 minutes post-standing.",
        "Fatigue, headaches, palpitations, dizziness, syncope, chest pain, GI issues, etc.",
        "Varies from mild to disabling; ~25% are unable to work due to severity.",
        "Often misdiagnosed as anxiety or panic disorder, though not more prevalent in POTS patients.",
        "Term 'POTS' coined in 1993; historically known by other names like DaCosta’s Syndrome.",
        "Includes Hypovolemic, Neuropathic (Partial Dysautonomia), Hyperadrenergic; often overlapping.",
        "Mostly affects women aged 15–50; ~75–80% of cases are female.",
        "Estimated 500,000 to 1,000,000 Americans affected.",
        "Includes autoimmune diseases, Ehlers-Danlos, Chiari malformation, infections, trauma, vitamin deficiencies, etc.",
        "Increased fluids/salt, compression garments, exercise, elevated bed head, dietary & lifestyle changes.",
        "Fludrocortisone, Beta Blockers, Midodrine, SSRIs/SNRIs, Pyridostigmine, Erythropoietin, Octreotide, etc.",
        "No cure; ~50% post-viral cases recover in 2–5 years; 60% improve over time with treatment."
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("POTS_summary.csv", index=False)
