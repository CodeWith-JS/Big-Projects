import streamlit as st
import pandas as pd
import joblib
import textwrap


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(99, 102, 241, 0.12),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(139, 92, 246, 0.10),
                transparent 30%
            ),
            #0b1020;
        color: #f8fafc;
    }


    /* Main content */
    .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* Header */
    .hero {
        padding: 2rem;
        border-radius: 24px;
        margin-bottom: 2rem;

        background:
            linear-gradient(
                135deg,
                rgba(30, 41, 59, 0.95),
                rgba(15, 23, 42, 0.95)
            );

        border: 1px solid rgba(148, 163, 184, 0.15);

        box-shadow:
            0 20px 60px rgba(0, 0, 0, 0.35);
    }


    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.3rem;
    }


    .hero-gradient {
        background:
            linear-gradient(
                90deg,
                #8b5cf6,
                #6366f1
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }


    .hero-subtitle {
        color: #94a3b8;
        font-size: 1.1rem;
    }


    /* Section titles */
    .section-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }


    /* Cards */
    .info-card {
        background: rgba(15, 23, 42, 0.75);

        border:
            1px solid
            rgba(148, 163, 184, 0.12);

        border-radius: 18px;

        padding: 1.4rem;

        margin-bottom: 1rem;

        box-shadow:
            0 10px 30px rgba(0, 0, 0, 0.18);
    }


    .career-card {
        background:
            linear-gradient(
                145deg,
                rgba(30, 41, 59, 0.95),
                rgba(15, 23, 42, 0.95)
            );

        border-radius: 22px;

        padding: 1.8rem;

        border:
            1px solid
            rgba(139, 92, 246, 0.25);

        box-shadow:
            0 15px 40px rgba(0, 0, 0, 0.25);

        margin: 1rem 0 2rem 0;
    }


    .career-name {
        font-size: 2rem;
        font-weight: 800;
    }


    .career-description {
        color: #94a3b8;
        line-height: 1.7;
    }


    /* Metric styling */
    [data-testid="stMetric"] {
        background: rgba(15, 23, 42, 0.7);

        border:
            1px solid
            rgba(148, 163, 184, 0.12);

        padding: 1rem;

        border-radius: 16px;
    }


    /* Buttons */
    .stButton > button {
        border-radius: 14px;

        font-weight: 700;

        min-height: 3rem;

        border: none;

        background:
            linear-gradient(
                90deg,
                #7c3aed,
                #4f46e5
            );

        color: white;

        transition: 0.2s;
    }


    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 10px 30px rgba(99, 102, 241, 0.35);
    }


    /* Sliders */
    .stSlider {
        padding-bottom: 0.5rem;
    }


    /* Sidebar */
    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #0f172a,
                #111827
            );

        border-right:
            1px solid
            rgba(148, 163, 184, 0.12);
    }


    /* Footer */
    .footer {
        text-align: center;

        color: #64748b;

        padding: 2rem 0 1rem 0;

        font-size: 0.9rem;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("model/career_model.pkl")


model = load_model()


# ============================================================
# CAREER INFORMATION
# ============================================================

career_info = {

    "AI Engineer": {
        "skills": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow / PyTorch",
            "Generative AI"
        ],
        "description":
            "AI Engineers design and integrate intelligent systems "
            "using artificial intelligence and machine learning."
    },

    "Machine Learning Engineer": {
        "skills": [
            "Python",
            "Machine Learning",
            "Scikit-learn",
            "Deep Learning",
            "Statistics"
        ],
        "description":
            "Machine Learning Engineers build, train and deploy "
            "machine learning models."
    },

    "Data Scientist": {
        "skills": [
            "Python",
            "SQL",
            "Statistics",
            "Machine Learning",
            "Data Visualization"
        ],
        "description":
            "Data Scientists use statistics, programming and machine "
            "learning to discover insights from data."
    },

    "Data Analyst": {
        "skills": [
            "SQL",
            "Python",
            "Excel",
            "Statistics",
            "Data Visualization"
        ],
        "description":
            "Data Analysts transform data into useful insights "
            "for decision-making."
    },

    "Web Developer": {
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "Backend Development",
            "Databases"
        ],
        "description":
            "Web Developers create and maintain modern websites "
            "and web applications."
    },

    "Frontend Developer": {
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "UI Design"
        ],
        "description":
            "Frontend Developers build the visual and interactive "
            "parts of web applications."
    },

    "Backend Developer": {
        "skills": [
            "Python / Node.js",
            "APIs",
            "Databases",
            "Authentication",
            "Server Development"
        ],
        "description":
            "Backend Developers build APIs, databases and "
            "server-side application logic."
    },

    "Full Stack Developer": {
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js",
            "Databases"
        ],
        "description":
            "Full Stack Developers work across both frontend "
            "and backend development."
    },

    "Cloud Engineer": {
        "skills": [
            "AWS / Azure",
            "Cloud Computing",
            "Linux",
            "Networking",
            "Docker"
        ],
        "description":
            "Cloud Engineers design and maintain cloud infrastructure "
            "and services."
    },

    "Cybersecurity Analyst": {
        "skills": [
            "Network Security",
            "Cybersecurity",
            "Linux",
            "Threat Analysis",
            "Ethical Hacking"
        ],
        "description":
            "Cybersecurity Analysts identify threats and protect "
            "systems and networks."
    },

    "DevOps Engineer": {
        "skills": [
            "Linux",
            "Docker",
            "CI/CD",
            "Cloud Computing",
            "Git"
        ],
        "description":
            "DevOps Engineers automate development, testing and "
            "deployment workflows."
    },

    "UI UX Designer": {
        "skills": [
            "UI Design",
            "UX Research",
            "Figma",
            "Wireframing",
            "Prototyping"
        ],
        "description":
            "UI/UX Designers create intuitive and visually appealing "
            "digital experiences."
    }
}


# ============================================================
# HERO
# ============================================================
st.html(
"""
<div class="hero">

<div class="hero-title">
🚀 <span class="hero-gradient">CareerPilot AI</span>
</div>

<div class="hero-subtitle">
AI-Powered Career Advisor • Machine Learning Based
</div>

<br>

<div style="color:#cbd5e1; line-height:1.7;">
Discover career paths that match your skills,
strengths and interests — powered by Machine Learning.
</div>

</div>
"""
)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🚀 CareerPilot AI")

    st.write(
        "Your intelligent career guidance assistant."
    )

    st.divider()

    st.markdown("### 🧠 AI Model")

    st.write("Algorithm: Random Forest")

    st.write("Careers: 12")

    st.write("Features: 15")

    st.write("Training Profiles: 270")

    st.divider()

    st.markdown("### 📊 Model Performance")

    st.metric(
        "Test Accuracy",
        "97.78%"
    )

    st.divider()

    st.caption(
        "AICTE × IBM SkillsBuild\n"
        "Machine Learning & Applied AI Internship 2026"
    )


# ============================================================
# PROFILE
# ============================================================

st.markdown(
    '<div class="section-title">👤 Your Career Profile</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


with col1:

    education = st.selectbox(
        "🎓 Education",
        [
            "BCA",
            "B.Tech",
            "B.Sc",
            "MCA",
            "M.Tech",
            "Other"
        ]
    )


with col2:

    experience = st.selectbox(
        "💼 Experience",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )


with col3:

    interest = st.selectbox(
        "💡 Primary Interest",
        [
            "Artificial Intelligence",
            "Data Science",
            "Web Development",
            "Cloud Computing",
            "Cybersecurity",
            "DevOps",
            "UI/UX Design"
        ]
    )


# ============================================================
# SKILLS
# ============================================================

st.markdown(
    '<div class="section-title">🧠 Skill Assessment</div>',
    unsafe_allow_html=True
)

st.caption(
    "Rate your current ability from 0 to 100."
)


feature_labels = {

    "Programming": "💻 Programming",

    "Statistics": "📊 Statistics",

    "Mathematics": "➗ Mathematics",

    "AI_ML": "🤖 AI / Machine Learning",

    "Databases": "🗄️ Databases",

    "Frontend": "🌐 Frontend Development",

    "Backend": "⚙️ Backend Development",

    "Networking": "📡 Networking",

    "Cloud": "☁️ Cloud Computing",

    "Cybersecurity": "🔐 Cybersecurity",

    "UI_UX": "🎨 UI / UX Design",

    "DevOps": "🔄 DevOps",

    "Communication": "🗣️ Communication",

    "Creativity": "💡 Creativity",

    "Problem_Solving": "🧩 Problem Solving"
}


features = {}

feature_list = list(
    feature_labels.keys()
)


for i in range(
    0,
    len(feature_list),
    3
):

    cols = st.columns(3)

    for j, col in enumerate(cols):

        index = i + j

        if index >= len(feature_list):
            break

        feature = feature_list[index]

        with col:

            features[feature] = st.slider(
                feature_labels[feature],
                min_value=0,
                max_value=100,
                value=50,
                step=5,
                key=f"skill_{feature}"
            )


st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# ANALYZE
# ============================================================

if st.button(
    "🚀 Analyze My Career",
    type="primary",
    use_container_width=True
):

    # --------------------------------------------------------
    # Prepare Input
    # --------------------------------------------------------

    model_input = {

        feature:
            features[feature] / 100

        for feature in feature_list
    }


    input_data = pd.DataFrame(
        [model_input]
    )


    # --------------------------------------------------------
    # Prediction
    # --------------------------------------------------------

    prediction = model.predict(
        input_data
    )[0]


    probabilities = model.predict_proba(
        input_data
    )[0]


    classes = model.classes_


    probability_df = pd.DataFrame({

        "Career": classes,

        "Probability": probabilities

    })


    probability_df = probability_df.sort_values(
        "Probability",
        ascending=False
    )


    match_score = round(
        probability_df.iloc[0]["Probability"] * 100,
        2
    )


    # ========================================================
    # RESULT
    # ========================================================

    st.markdown(
        "<br><hr>",
        unsafe_allow_html=True
    )


    st.markdown(
        '<div class="section-title">🎯 Career Analysis</div>',
        unsafe_allow_html=True
    )


    st.html(
f"""
<div class="career-card">

<div style="color:#94a3b8;">
BEST CAREER MATCH
</div>

<div class="career-name">
{prediction}
</div>

<br>

<div class="career-description">
{career_info.get(prediction, {}).get("description", "Career information unavailable.")}
</div>

</div>
"""
)


    result_col1, result_col2, result_col3 = st.columns(3)


    with result_col1:

        st.metric(
            "🎯 Recommended Career",
            prediction
        )


    with result_col2:

        st.metric(
            "📊 AI Match Score",
            f"{match_score}%"
        )


    with result_col3:

        st.metric(
            "🏆 Career Options",
            "12"
        )


    # ========================================================
    # TOP MATCHES
    # ========================================================

    st.markdown(
        '<div class="section-title">🏆 Top Career Matches</div>',
        unsafe_allow_html=True
    )


    top_matches = probability_df.head(
        5
    ).copy()


    top_matches["Probability"] = (
        top_matches["Probability"] * 100
    ).round(2)


    top_matches = top_matches.rename(
        columns={
            "Probability":
                "Match Score (%)"
        }
    )


    st.dataframe(
        top_matches,
        use_container_width=True,
        hide_index=True
    )


    # ========================================================
    # CHART
    # ========================================================

    st.markdown(
        '<div class="section-title">📊 Career Match Analysis</div>',
        unsafe_allow_html=True
    )


    chart_data = top_matches.set_index(
        "Career"
    )


    st.bar_chart(
        chart_data[
            "Match Score (%)"
        ]
    )


    # ========================================================
    # RECOMMENDED SKILLS
    # ========================================================

    st.markdown(
        '<div class="section-title">📚 Recommended Skills</div>',
        unsafe_allow_html=True
    )


    recommended_skills = career_info.get(
        prediction,
        {}
    ).get(
        "skills",
        []
    )


    skill_cols = st.columns(3)


    for index, skill in enumerate(
        recommended_skills
    ):

        with skill_cols[
            index % 3
        ]:

            st.markdown(f"""
<div class="info-card">
🔹 <b>{skill}</b>
</div>
""",
unsafe_allow_html=True
)

    # ========================================================
    # LEARNING ROADMAP
    # ========================================================

    st.markdown(
        '<div class="section-title">🚀 Suggested Learning Roadmap</div>',
        unsafe_allow_html=True
    )


    roadmap = [

        "Strengthen your existing skills",

        "Learn the missing technical skills",

        "Build 2–3 practical projects",

        "Create a strong GitHub portfolio",

        "Complete relevant certifications",

        "Apply for internships and entry-level jobs"

    ]


    for index, step in enumerate(
        roadmap,
        start=1
    ):

        st.markdown(
f"""
<div class="info-card">
<b>{index}</b> &nbsp; {step}
</div>
""",
unsafe_allow_html=True
)


    # ========================================================
    # DISCLAIMER
    # ========================================================

    st.info(
        "💡 CareerPilot AI provides career guidance "
        "based on a machine-learning model. "
        "It should be used as a decision-support tool "
        "rather than a definitive career decision."
    )


# ============================================================
# FOOTER
# ============================================================
st.markdown("""
<div class="footer">
CareerPilot AI<br>
AICTE × IBM SkillsBuild<br>
Machine Learning & Applied AI Internship 2026
</div>
""", unsafe_allow_html=True)