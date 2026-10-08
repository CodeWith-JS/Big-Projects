# 🚀 CareerPilot AI — AI-Powered Career Advisor

> An intelligent Machine Learning-based career recommendation system that analyzes a user's skills and strengths to recommend suitable career paths.

**AICTE | IBM SkillsBuild Machine Learning & Applied AI Internship Program 2026**

---

## 📌 Project Overview

**CareerPilot AI** is a Machine Learning-based career advisory application designed to help students and beginners identify suitable technology career paths based on their skills, abilities, interests, and strengths.

The system uses a **Random Forest Classification model** trained on a synthetic career-profile dataset containing multiple skill-related features across different technology careers.

Users can rate their abilities across different areas, and CareerPilot AI analyzes their profile to generate:

- 🎯 Recommended career
- 📊 AI match score
- 🏆 Top career matches
- 📚 Recommended skills
- 📈 Career probability visualization
- 🚀 Suggested learning roadmap

---

## 🎯 Problem Statement

Students and beginners often struggle to identify which technology career is most suitable for their skills and interests.

There are many possible career paths such as:

- Artificial Intelligence
- Machine Learning
- Data Science
- Web Development
- Cloud Computing
- Cybersecurity
- DevOps
- UI/UX Design

CareerPilot AI attempts to solve this problem by using Machine Learning to analyze a user's skill profile and recommend suitable career options.

---

## 💡 Proposed Solution

CareerPilot AI collects a user's skill ratings and processes them through a trained Machine Learning model.

The system follows this process:

```text
User Skill Assessment
        ↓
Feature Preparation
        ↓
Machine Learning Model
        ↓
Career Prediction
        ↓
Career Probability Analysis
        ↓
Top Career Recommendations
        ↓
Skill Recommendations
        ↓
Learning Roadmap
```

---

## ✨ Features

### 🎯 Career Recommendation

Predicts the career that best matches the user's skill profile.

### 📊 AI Match Score

Provides a probability-based match score for the recommended career.

### 🏆 Top Career Matches

Displays multiple career options ranked according to their predicted probability.

### 🧠 Skill Assessment

Users can rate their ability from 0–100 across 15 different areas.

### 📚 Skill Recommendations

Suggests important skills associated with the recommended career.

### 📈 Career Visualization

Displays the top career matches using an interactive chart.

### 🚀 Learning Roadmap

Provides a simple roadmap for improving skills and preparing for a career.

### 🎨 Interactive UI

Built using Streamlit with a modern dark-themed interface.

---

# 🧠 Machine Learning

## Algorithm

CareerPilot AI uses:

> **Random Forest Classifier**

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees to improve prediction performance and reduce overfitting compared with a single decision tree.

---

## 📊 Dataset

The project uses a **synthetically generated dataset** created specifically for the prototype.

### Dataset statistics

| Property | Value |
|---|---:|
| Total profiles | 360 |
| Career categories | 12 |
| Features | 15 |
| Training samples | 270 |
| Testing samples | 90 |

### Career Categories

1. AI Engineer
2. Machine Learning Engineer
3. Data Scientist
4. Data Analyst
5. Web Developer
6. Frontend Developer
7. Backend Developer
8. Full Stack Developer
9. Cloud Engineer
10. Cybersecurity Analyst
11. DevOps Engineer
12. UI/UX Designer

---

## 🔢 Machine Learning Features

The model uses 15 skill-related features:

```text
Programming
Statistics
Mathematics
AI / Machine Learning
Databases
Frontend Development
Backend Development
Networking
Cloud Computing
Cybersecurity
UI / UX Design
DevOps
Communication
Creativity
Problem Solving
```

Each feature represents the user's ability level on a scale from **0 to 100**.

The application converts these values into a normalized 0–1 range before sending them to the Machine Learning model.

---

# 📈 Model Evaluation

The dataset is divided into:

```text
75% → Training
25% → Testing
```

The test set contains:

```text
90 profiles
```

### Model Result

> **Test Accuracy: 97.78%**

Additional evaluation:

| Metric | Score |
|---|---:|
| Accuracy | 97.78% |
| Macro F1 | 0.98 |
| Weighted F1 | 0.98 |

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Classification Report

---

## ⚠️ Dataset Limitation

The current dataset is **synthetic** and was generated for demonstrating the Machine Learning pipeline.

Therefore, the 97.78% accuracy should **not** be interpreted as real-world career prediction accuracy.

A production version of CareerPilot AI should use a larger, validated dataset collected from reliable career, education, skills, and employment sources.

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │       USER          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Skill Assessment UI │
                    │     Streamlit       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Feature Processing  │
                    │   Normalization     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Random Forest     │
                    │    Classifier       │
                    └──────────┬──────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │ Career Probability      │
                  │ Analysis                 │
                  └────────────┬────────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
        Recommended       Top Career       Skill & Learning
          Career            Matches            Roadmap
```

---

# 🛠️ Technology Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Random Forest
- Pandas
- NumPy

### Web Application

- Streamlit

### Model Storage

- Joblib

### Development

- VS Code
- Python
- Git / GitHub

---

# 📁 Project Structure

```text
CareerPilot-AI/
│
├── data/
│   └── careers.csv
│
├── model/
│   └── career_model.pkl
│
├── generate_dataset.py
├── train_model.py
├── app.py
├── requirements.txt
├── README.md
│
└── docs/
    └── project documentation
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project:

```bash
cd CareerPilot-AI
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install pandas numpy scikit-learn streamlit joblib
```

---

# ▶️ Running the Project

## Step 1 — Generate Dataset

```bash
python generate_dataset.py
```

This creates:

```text
data/careers.csv
```

---

## Step 2 — Train the Model

```bash
python train_model.py
```

This creates:

```text
model/career_model.pkl
```

---

## Step 3 — Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

Usually:

```text
http://localhost:8501
```

---

# 🖥️ Application Workflow

### Step 1

Enter your:

- Education
- Experience level
- Primary career interest

### Step 2

Rate your skills from:

```text
0 → Beginner
100 → Advanced
```

### Step 3

Click:

```text
🚀 Analyze My Career
```

### Step 4

CareerPilot AI generates:

```text
🎯 Recommended Career

📊 AI Match Score

🏆 Top Career Matches

📚 Recommended Skills

📈 Career Match Chart

🚀 Learning Roadmap
```

---

# 🔮 Future Scope

The project can be expanded significantly in future versions.

### 🤖 Advanced AI

- NLP-based resume analysis
- Large Language Model integration
- Personalized AI career chatbot
- Resume-to-career matching

### 📄 Resume Analysis

Users could upload their resume and CareerPilot AI could extract:

- Skills
- Education
- Experience
- Projects
- Certifications

and automatically generate career recommendations.

### 🌐 Real-World Data

Future versions could use validated data from:

- Job postings
- Career databases
- Skill frameworks
- Education platforms
- Industry reports

### 🎓 Personalized Learning

The system could recommend:

- Courses
- Certifications
- Projects
- Books
- Learning resources

based on the user's skill gaps.

### 💼 Job Recommendations

Future versions could match users with relevant job roles based on:

- Skills
- Experience
- Location
- Career preference

---

# ⚠️ Limitations

Current limitations include:

1. The dataset is synthetic.
2. The model currently uses skill-profile features only.
3. Real-world career decisions involve many factors beyond technical skills.
4. The system does not guarantee employment outcomes.
5. The current prototype does not analyze resumes automatically.

---

# 🔐 Ethical Considerations

Career recommendations can influence important personal decisions.

Therefore, CareerPilot AI should be treated as a **decision-support tool**, not as an authoritative career decision-maker.

The system should avoid making recommendations based on sensitive personal characteristics.

Future versions should also be evaluated for:

- Dataset bias
- Model bias
- Fairness
- Explainability
- Privacy

---

# 📌 Project Objectives

The main objectives of CareerPilot AI are:

1. Develop a Machine Learning-based career recommendation system.
2. Analyze user skill profiles.
3. Predict suitable technology career paths.
4. Provide multiple career recommendations.
5. Identify relevant skills for selected careers.
6. Provide a basic learning roadmap.
7. Demonstrate the application of Machine Learning in career guidance.

---

# 🎓 Internship Information

**Program:**

AICTE | IBM SkillsBuild Machine Learning & Applied AI Internship Program 2026

**Project:**

CareerPilot AI — AI-Powered Career Advisor

**Domain:**

Machine Learning & Applied AI

---

# 👨‍💻 Author

**Juned Shaikh**

Developed as part of the:

**AICTE | IBM SkillsBuild Machine Learning & Applied AI Internship Program 2026**

---

# ⭐ Conclusion

CareerPilot AI demonstrates how Machine Learning can be applied to career guidance by analyzing skill profiles and predicting suitable career paths.

The project combines:

```text
Python
+
Machine Learning
+
Random Forest
+
Data Processing
+
Streamlit
+
Interactive Visualization
```

The current prototype achieves a **97.78% test accuracy on its synthetic evaluation dataset** and provides an interactive platform for exploring career recommendations.

> 🚀 CareerPilot AI — Helping you find the career path that fits your skills.