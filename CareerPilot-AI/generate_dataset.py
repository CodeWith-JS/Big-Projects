import pandas as pd
import random

random.seed(42)


# ============================================================
# Career Profiles
# ============================================================

career_profiles = {

    "Data Scientist": {
        "Programming": 0.9,
        "Statistics": 0.95,
        "Mathematics": 0.9,
        "AI_ML": 0.9,
        "Databases": 0.8,
        "Frontend": 0.1,
        "Backend": 0.4,
        "Networking": 0.1,
        "Cloud": 0.4,
        "Cybersecurity": 0.1,
        "UI_UX": 0.1,
        "DevOps": 0.1,
        "Communication": 0.7,
        "Creativity": 0.6,
        "Problem_Solving": 0.9
    },

    "Machine Learning Engineer": {
        "Programming": 0.95,
        "Statistics": 0.8,
        "Mathematics": 0.85,
        "AI_ML": 1.0,
        "Databases": 0.6,
        "Frontend": 0.1,
        "Backend": 0.6,
        "Networking": 0.2,
        "Cloud": 0.7,
        "Cybersecurity": 0.1,
        "UI_UX": 0.1,
        "DevOps": 0.5,
        "Communication": 0.6,
        "Creativity": 0.7,
        "Problem_Solving": 0.95
    },

    "AI Engineer": {
        "Programming": 0.95,
        "Statistics": 0.7,
        "Mathematics": 0.8,
        "AI_ML": 1.0,
        "Databases": 0.5,
        "Frontend": 0.2,
        "Backend": 0.7,
        "Networking": 0.2,
        "Cloud": 0.7,
        "Cybersecurity": 0.1,
        "UI_UX": 0.2,
        "DevOps": 0.4,
        "Communication": 0.6,
        "Creativity": 0.8,
        "Problem_Solving": 0.95
    },

    "Data Analyst": {
        "Programming": 0.6,
        "Statistics": 0.9,
        "Mathematics": 0.7,
        "AI_ML": 0.3,
        "Databases": 0.9,
        "Frontend": 0.1,
        "Backend": 0.2,
        "Networking": 0.1,
        "Cloud": 0.2,
        "Cybersecurity": 0.1,
        "UI_UX": 0.2,
        "DevOps": 0.1,
        "Communication": 0.85,
        "Creativity": 0.6,
        "Problem_Solving": 0.8
    },

    "Web Developer": {
        "Programming": 0.85,
        "Statistics": 0.2,
        "Mathematics": 0.3,
        "AI_ML": 0.1,
        "Databases": 0.7,
        "Frontend": 0.8,
        "Backend": 0.7,
        "Networking": 0.4,
        "Cloud": 0.3,
        "Cybersecurity": 0.2,
        "UI_UX": 0.5,
        "DevOps": 0.3,
        "Communication": 0.6,
        "Creativity": 0.8,
        "Problem_Solving": 0.85
    },

    "Full Stack Developer": {
        "Programming": 0.95,
        "Statistics": 0.2,
        "Mathematics": 0.3,
        "AI_ML": 0.1,
        "Databases": 0.85,
        "Frontend": 0.9,
        "Backend": 0.9,
        "Networking": 0.5,
        "Cloud": 0.5,
        "Cybersecurity": 0.3,
        "UI_UX": 0.5,
        "DevOps": 0.5,
        "Communication": 0.7,
        "Creativity": 0.8,
        "Problem_Solving": 0.95
    },

    "Cloud Engineer": {
        "Programming": 0.75,
        "Statistics": 0.2,
        "Mathematics": 0.3,
        "AI_ML": 0.1,
        "Databases": 0.5,
        "Frontend": 0.1,
        "Backend": 0.5,
        "Networking": 0.9,
        "Cloud": 1.0,
        "Cybersecurity": 0.6,
        "UI_UX": 0.1,
        "DevOps": 0.8,
        "Communication": 0.6,
        "Creativity": 0.4,
        "Problem_Solving": 0.9
    },

    "Cybersecurity Analyst": {
        "Programming": 0.6,
        "Statistics": 0.3,
        "Mathematics": 0.4,
        "AI_ML": 0.1,
        "Databases": 0.4,
        "Frontend": 0.1,
        "Backend": 0.3,
        "Networking": 0.95,
        "Cloud": 0.6,
        "Cybersecurity": 1.0,
        "UI_UX": 0.1,
        "DevOps": 0.3,
        "Communication": 0.7,
        "Creativity": 0.5,
        "Problem_Solving": 0.95
    },

    "DevOps Engineer": {
        "Programming": 0.8,
        "Statistics": 0.2,
        "Mathematics": 0.3,
        "AI_ML": 0.1,
        "Databases": 0.6,
        "Frontend": 0.1,
        "Backend": 0.6,
        "Networking": 0.8,
        "Cloud": 0.9,
        "Cybersecurity": 0.5,
        "UI_UX": 0.1,
        "DevOps": 1.0,
        "Communication": 0.7,
        "Creativity": 0.5,
        "Problem_Solving": 0.9
    },

    "Frontend Developer": {
        "Programming": 0.8,
        "Statistics": 0.1,
        "Mathematics": 0.2,
        "AI_ML": 0.1,
        "Databases": 0.3,
        "Frontend": 1.0,
        "Backend": 0.2,
        "Networking": 0.2,
        "Cloud": 0.2,
        "Cybersecurity": 0.1,
        "UI_UX": 0.9,
        "DevOps": 0.1,
        "Communication": 0.7,
        "Creativity": 0.95,
        "Problem_Solving": 0.8
    },

    "Backend Developer": {
        "Programming": 0.95,
        "Statistics": 0.2,
        "Mathematics": 0.3,
        "AI_ML": 0.1,
        "Databases": 0.95,
        "Frontend": 0.2,
        "Backend": 1.0,
        "Networking": 0.6,
        "Cloud": 0.5,
        "Cybersecurity": 0.3,
        "UI_UX": 0.1,
        "DevOps": 0.4,
        "Communication": 0.6,
        "Creativity": 0.5,
        "Problem_Solving": 0.95
    },

    "UI UX Designer": {
        "Programming": 0.2,
        "Statistics": 0.3,
        "Mathematics": 0.1,
        "AI_ML": 0.1,
        "Databases": 0.1,
        "Frontend": 0.5,
        "Backend": 0.1,
        "Networking": 0.1,
        "Cloud": 0.1,
        "Cybersecurity": 0.1,
        "UI_UX": 1.0,
        "DevOps": 0.1,
        "Communication": 0.9,
        "Creativity": 1.0,
        "Problem_Solving": 0.8
    }
}


# ============================================================
# Generate Dataset
# ============================================================

rows = []

feature_names = list(
    next(iter(career_profiles.values())).keys()
)


for career, profile in career_profiles.items():

    # 30 samples for every career
    for _ in range(30):

        sample = {}

        for feature in feature_names:

            base_value = profile[feature]

            # Add realistic variation
            variation = random.gauss(0, 0.12)

            value = base_value + variation

            # Keep values between 0 and 1
            value = max(0, min(1, value))

            sample[feature] = round(value, 2)

        sample["Career"] = career

        rows.append(sample)


# ============================================================
# Create DataFrame
# ============================================================

df = pd.DataFrame(rows)

df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)


# ============================================================
# Save Dataset
# ============================================================

df.to_csv(
    "data/careers.csv",
    index=False
)


# ============================================================
# Output
# ============================================================

print("============================================")
print("🎉 CareerPilot AI Dataset Generated")
print("============================================")

print(f"📊 Total records: {len(df)}")

print(
    f"🎯 Career categories: {df['Career'].nunique()}"
)

print(
    f"🧠 Features: {len(feature_names)}"
)

print("\nCareer distribution:")

print(
    df["Career"].value_counts()
)

print("\nFeatures:")

print(
    ", ".join(feature_names)
)

print("\n📁 Saved to: data/careers.csv")