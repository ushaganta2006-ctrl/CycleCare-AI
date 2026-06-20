import streamlit as st
import pandas as pd
from PIL import Image

from utils.gemini_food_analyzer import analyze_food_image

st.title("🏃 Routine Tracker")

st.subheader("Daily Wellness")

col1, col2 = st.columns(2)

with col1:

    sleep = st.slider(
        "😴 Sleep Hours",
        0,
        12,
        7
    )

    water = st.number_input(
        "💧 Water Intake (L)",
        min_value=0.0,
        value=2.0
    )

with col2:

    stress = st.slider(
        "😌 Stress Level",
        1,
        10,
        5
    )

    exercise = st.selectbox(
        "🏋 Exercise",
        [
            "None",
            "Walking",
            "Yoga",
            "Gym",
            "Running"
        ]
    )

st.divider()

st.subheader("📷 Food Plate Analysis")

uploaded_image = st.file_uploader(
    "Upload Meal Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image:

    image = Image.open(uploaded_image)

    st.image(
        image,
        caption="Uploaded Food Plate",
        use_container_width=True
    )

    if st.button("🔍 Analyze Food Plate"):

        with st.spinner("Analyzing meal..."):

            result = analyze_food_image(image)

        st.success("Analysis Complete")

        st.divider()

        st.subheader("🍽 Food Items Identified")

        food_df = pd.DataFrame(
            result["food_items"]
        )

        st.dataframe(food_df,use_container_width=True)

        st.divider()

        st.subheader("📊 Total Nutrition")

        nutrition = result["total_nutrition"]

        c1, c2, c3, c4, c5 = st.columns(5)

        c1.metric("Calories",nutrition.get("calories", 0))

        c2.metric("Protein",f"{nutrition.get('protein', 0)} g")

        c3.metric("Carbs",f"{nutrition.get('carbs', 0)} g")

        c4.metric("Fat",f"{nutrition.get('fat', 0)} g")

        c5.metric("Fiber",f"{nutrition.get('fiber', 0)} g")

        st.divider()

        score = result["pcos_score"]

        st.subheader("💜 PCOS Suitability")

        st.progress(score / 100)

        st.metric("PCOS Score",f"{score}/100")

        st.write(f"Assessment: **{result['assessment']}**")

        st.divider()

        st.subheader("⚠ Warnings")

        if result["warnings"]:

            for warning in result["warnings"]:
                st.warning(warning)

        else:
            st.success("No major concerns detected.")

        st.divider()

        st.subheader("🌸 Nutrients Missing")

        if result["missing_nutrients"]:

            for nutrient in result["missing_nutrients"]:
                st.error(nutrient)

        else:
            st.success("No major nutrient gaps detected.")
            
        st.divider()

        st.subheader("✅ Recommendations")

        for rec in result["recommendations"]:
            st.info(rec)