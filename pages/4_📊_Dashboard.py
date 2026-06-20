import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------

st.markdown("""
<style>

.stApp{
background: linear-gradient(
90deg,
#FFF8F2 0%,
#FFF5F8 40%,
#FFE7EF 100%
);
}

.metric-card{
background:white;
padding:25px;
border-radius:20px;
text-align:center;
box-shadow:0 6px 15px rgba(0,0,0,0.08);
}

.summary-card{
background:white;
padding:30px;
border-radius:25px;
box-shadow:0 6px 15px rgba(0,0,0,0.08);
}

.title{
font-size:50px;
font-weight:800;
color:#2C0B36;
text-align:center;
}

.subtitle{
font-size:22px;
color:#D45D9E;
text-align:center;
margin-bottom:30px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# FETCH DATA
# -------------------------

next_period = st.session_state.get(
    "next_period",
    "No Data"
)

cycle_length = st.session_state.get(
    "cycle_length",
    0
)

nutrition_score = st.session_state.get(
    "nutrition_score",
    0
)

report_status = st.session_state.get(
    "report_status",
    "No Reports"
)

symptoms = st.session_state.get(
    "symptoms",
    []
)

# -------------------------
# WELLNESS SCORE
# -------------------------

score = 100

if cycle_length > 45:
    score -= 15

if nutrition_score < 70:
    score -= 10

if report_status != "Normal":
    score -= 20

score = max(score, 0)

# -------------------------
# AI SUMMARY
# -------------------------

summary = ""

if cycle_length > 45:

    summary = """
🌸 Your cycle appears slightly irregular.

Continue a high-protein diet,
regular exercise and stress management.

Consider hormonal testing if symptoms persist.
"""

elif len(symptoms) > 2:

    summary = """
🌸 Symptoms are being monitored.

Focus on sleep, hydration and
balanced meals.

Keep tracking your cycle regularly.
"""

else:

    summary = """
🌸 Good Going!

Your current health indicators
look stable.

Keep maintaining your healthy routine.
"""

# -------------------------
# HERO
# -------------------------

st.markdown("""
<div class='title'>
🌸 CycleCare Dashboard
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle'>
Your Personalized Women's Health Snapshot
</div>
""", unsafe_allow_html=True)

# -------------------------
# AI SUMMARY CARD
# -------------------------

st.markdown(
f"""
<div class='summary-card'>
<h2>🌷 AI Health Summary</h2>

<p style='font-size:18px;'>

{summary}

</p>
</div>
""",
unsafe_allow_html=True
)

st.write("")

# -------------------------
# TOP METRICS
# -------------------------

col1,col2,col3,col4 = st.columns(4)

with col1:

    st.metric(
        "📅 Next Period",
        next_period
    )

with col2:

    st.metric(
        "🌸 Cycle Length",
        f"{cycle_length} Days"
    )

with col3:

    st.metric(
        "🍎 Nutrition Score",
        f"{nutrition_score}/100"
    )

with col4:

    st.metric(
        "🩺 Reports",
        report_status
    )

st.write("")

# -------------------------
# WELLNESS SCORE
# -------------------------

st.subheader("🌸 PCOS Wellness Score")

st.progress(score/100)

st.markdown(
f"""
### 💜 {score}/100
"""
)

# -------------------------
# SYMPTOMS
# -------------------------

st.subheader("🩺 Recent Symptoms")

if symptoms:

    for symptom in symptoms:

        st.write(f"• {symptom}")

else:

    st.success("No symptoms recorded")

# -------------------------
# CYCLE TREND CHART
# -------------------------

st.subheader("📈 Cycle Trend")

cycle_history = st.session_state.get(
    "cycle_history",
    [45,48,52,50,46]
)

df = pd.DataFrame({

    "Cycle": list(
        range(
            1,
            len(cycle_history)+1
        )
    ),

    "Days": cycle_history
})

fig = px.line(
    df,
    x="Cycle",
    y="Days",
    markers=True
)

fig.update_layout(
    height=400,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------
# MOTIVATION CARD
# -------------------------

if score >= 80:

    quote = """
🌸 You're doing great.

Healthy habits build a healthier future.
"""

elif score >= 60:

    quote = """
💜 Small daily improvements
lead to lasting results.
"""

else:

    quote = """
🌷 One step at a time.

Your health journey matters.
"""

st.info(quote)