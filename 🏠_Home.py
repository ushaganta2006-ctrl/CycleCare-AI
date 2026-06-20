import streamlit as st

st.set_page_config(
    page_title="CycleCare AI",
    page_icon="🌸",
    layout="wide"
)

# ================= CSS =================

st.markdown("""
<style>

/* Main Background */

.stApp{background:linear-gradient(90deg,#FFF8F2 0%,#FFF5F8 40%,#FFE7EF 100%);}

/* Sidebar */

[data-testid="stSidebar"]
{background:linear-gradient(180deg,#FFF4E7 0%,#FFE8EE 100%);border-right:2px solid #FFC8D7;}

[data-testid="stSidebar"] 
*{color:#3C3042 !important;}

/* Hero Section */

.main-title{text-align:center;font-size:90px;font-weight:900;color:#230B2C;margin-bottom:0px;}

.sub-title{text-align:center;font-size:42px;font-weight:700;background: linear-gradient(90deg,#C65AA0,#FF5F96);           
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
margin-bottom:30px;
}

.description{text-align:center;font-size:24px;color:#4B5563;padding-left:120px;padding-right:120px;margin-bottom:50px;}

/* Cards */

.feature-card{background:white;
padding:35px;
border-radius:30px;
text-align:center;
box-shadow:0px 8px 25px rgba(0,0,0,0.08);
min-height:320px;
transition:0.3s;
}

.feature-card:hover{
transform:translateY(-6px);
}

.feature-icon{
font-size:55px;
}

.feature-title{
font-size:28px;
font-weight:700;
margin-top:15px;
}

.feature-text{
font-size:18px;
color:#555;
}

/* Quote Card */

.quote-card{
background:white;
padding:30px;
border-radius:25px;
box-shadow:0px 8px 25px rgba(0,0,0,0.08);
margin-top:40px;
text-align:center;
font-size:24px;
color:#555;
font-style:italic;
}

/* Hide Footer */

footer{
visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================

st.sidebar.markdown(
"""
<div style="
text-align:center;
font-size:16px;
color:#C75A8A;
font-style:italic;
padding:10px;
">
"Every cycle tells a story.<br>
Understand yours with confidence 🌸"
</div>
""",
unsafe_allow_html=True
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)

st.sidebar.image("assets/woman.png",use_container_width=True)

# ================= HERO =================

st.markdown("""
<div class='main-title'>
🌸 CycleCare AI
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='sub-title'>
Personalized Women's Health Companion
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='description'>
Your all-in-one AI companion to track periods,
analyze reports, monitor nutrition, and improve
women's health naturally and intelligently.
</div>
""", unsafe_allow_html=True)

# ================= FEATURES =================

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='feature-card'>
        <div class='feature-icon'>📅</div>
        <div class='feature-title' style='color:#F25592'>
        Period Tracking
        </div>
        <br>
        <div class='feature-text'>
        Track cycles, symptoms and predict upcoming periods.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='feature-card'>
        <div class='feature-icon'>📄</div>
        <div class='feature-title' style='color:#A44AE5'>
        Report Analysis
        </div>
        <br>
        <div class='feature-text'>
        Upload CBC, Iron, Thyroid and USG reports for AI insights.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='feature-card'>
        <div class='feature-icon'>🍎</div>
        <div class='feature-title' style='color:#F28C18'>
        Routine Tracking
        </div>
        <br>
        <div class='feature-text'>
        Analyze meals and receive PCOS-friendly recommendations.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='feature-card'>
        <div class='feature-icon'>📊</div>
        <div class='feature-title' style='color:#FF4C95'>
        Health Dashboard
        </div>
        <br>
        <div class='feature-text'>
        Visualize your wellness journey and overall progress.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= QUOTE =================

st.markdown("""
<div class='quote-card'>
💜 "Take care of your body. It's the only place you have to live."
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.success("""
🌸 Welcome to CycleCare AI

Track your cycle • Analyze reports • Monitor nutrition • Build healthier habits
""")