import streamlit as st
from datetime import timedelta

from utils.gemini_period_analyzer import analyze_period

st.title("📅 Period Tracker")

st.write(
    "Track your cycle and receive AI-powered health insights."
)

# -------------------------
# INPUTS
# -------------------------

last_period_date = st.date_input(
    "Last Period Date"
)

cycle_length = st.number_input(
    "Average Cycle Length (Days)",
    min_value=20,
    max_value=90,
    value=45
)

symptoms = st.multiselect(
    "Select Symptoms",
    [
        "Irregular Periods",
        "Missed Periods",
        "Acne",
        "Weight Gain",
        "Hair Fall",
        "Facial Hair Growth",
        "Mood Swings",
        "Fatigue",
        "Heavy Bleeding",
        "Pelvic Pain",
        "Cravings"
    ]
)

# -------------------------
# ANALYZE
# -------------------------

if st.button("🌸 Analyze My Cycle"):

    next_period = (
        last_period_date +
        timedelta(days=cycle_length)
    )

    st.session_state["next_period"] = str(next_period)
    st.session_state["cycle_length"] = cycle_length
    st.session_state["symptoms"] = symptoms

    st.success(
        f"📅 Estimated Next Period: {next_period}"
    )

    with st.spinner(
        "Analyzing symptoms..."
    ):

        result = analyze_period(
            cycle_length,
            symptoms
        )

    st.session_state["period_ai_response"] = result

    st.markdown("### 🌸 AI Health Insights")

    st.markdown(result)