import streamlit as st
import pandas as pd
from PIL import Image

from utils.gemini_reports_analyzer import analyze_report

st.title("📄 Reports Analyzer")

st.markdown("""
### Upload Reports

Supported Reports:

- CBC Report
- Iron Profile
- Thyroid Profile
- Vitamin D
- Vitamin B12
- Hormonal Reports
- USG Whole Abdomen
""")

uploaded_file = st.file_uploader("Upload Report Image",type=["png", "jpg", "jpeg"])

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image,caption="Uploaded Report",use_container_width=True)

    if st.button("🔍 Analyze Report"):

        with st.spinner("Analyzing Report..."):

            result = analyze_report(image)

        if "error" in result:

            st.error(result["error"])
            st.stop()

        st.success("Analysis Complete")

        st.divider()

        st.subheader("👩 Patient Information")

        patient = result["patient_information"]

        col1, col2, col3 = st.columns(3)

        with col1:st.metric("Name",patient["name"])

        with col2:st.metric("Age",patient["age"])

        with col3:st.metric("Gender",patient["gender"])

        st.divider()

        st.subheader("🌸 Overall Health Score")

        score = result["health_score"]

        st.progress(score / 100)

        st.metric("Health Score",f"{score}/100")

        st.divider()

        st.subheader("📋 Reports Analysis")

        for report in result["reports_analysis"]:

            with st.expander(report["report_type"]):

                findings = report["findings"]

                if findings:

                    df = pd.DataFrame(findings)

                    st.dataframe(df,use_container_width=True)

                abnormalities = report.get("abnormalities",[])

                if abnormalities:

                    st.subheader("⚠ Abnormalities")

                    for abnormality in abnormalities:

                        st.warning(abnormality)

                else:

                    st.success("No abnormalities detected.")

        st.divider()

        st.subheader("🩺 Summary")

        st.info(result["summary"])

        st.divider()

        st.subheader("💜 PCOS Relevance")

        st.info(result["pcos_relevance"])

        st.divider()

        st.subheader("✅ Recommendations")

        for recommendation in result["recommendations"]:

            st.success(recommendation)