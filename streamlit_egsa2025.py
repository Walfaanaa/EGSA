import streamlit as st
import pandas as pd
import altair as alt

# ==========================
# PAGE SETUP
# ==========================
st.set_page_config(page_title="EGSA2025 PLC", layout="wide")

# ==========================
# SIDEBAR NAVIGATION (English + Amharic)
# ==========================
st.sidebar.title("EGSA2025")

pages = {
    "🏠 Home / መነሻ": "home",
    "📘 Financial Strategy / የገንዘብ ዘዴ": "finance",
    "🔑 Leadership Handbook / የአመራር መመሪያ": "leadership",
    "🤝 Member Benefits / የአባላት ጥቅሞች": "benefits",
    "⚙️ How It Works / እንዴት እንደሚሰራ": "how",
    "📩 Join EGSA2025 / አባል ይሁኑ": "join",
}

page_selection = st.sidebar.radio("Navigate / አስመራ", list(pages.keys()))
page = pages[page_selection]

# ==========================
# HOME
# ==========================
if page == "home":
    # --- Centered Logo ---
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(
            "https://github.com/Walfaanaa/EGSA/blob/main/EGSA.png?raw=true",
            use_container_width=True
        )

    # --- Centered Title ---
    st.markdown(
        "<h1 style='text-align: center;'>Welcome to <b>EGSA2025 PLC</b> / እንኳን ወደ EGSA2025 PLC በደህና መጡ</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<h4 style='text-align: center;'>Empowering the New Generation of Investors / የአዲሱን ትውልድ የባለጌነት ኃይል ማድረግ</h4>",
        unsafe_allow_html=True
    )
    st.markdown("---")

    # --- Introduction Section ---
    st.markdown(
        '<span style="color:blue; font-weight:bold; font-size:22px;">INTRODUCTION / መግቢያ</span>',
        unsafe_allow_html=True
    )
    st.write("""
    EGSA2025 is built by members who take initiative, lead with integrity, and focus on effort rather than immediate results.
    የEGSA2025 ማህበር በተለያዩ አባላት ተመሠረተ፣ በትክክለኛነት መሪነት ያደርጉ እና ትጋትን በፊት ያደርጉ እንጂ በአስቸኳይ ውጤት ላይ አያደርጉ።
    """)

# ==========================
# FINANCIAL STRATEGY
# ==========================
elif page == "finance":
    st.header("📘 EGSA Financial Strategy / የገንዘብ ዘዴ")
    st.markdown("""
    EGSA follows a **system-driven financial model** / EGSA የስርዓት የተመሠረተ የገንዘብ ሞዴል ይከተላል:
    - **80% Investment / 80% እንቅስቃሴ** → Growth & wealth creation / እድገት እና ገንዘብ ፍጠር
    - **20% Savings / 20% ቁጠባ** → Security & stability / ደህንነት እና ጸናት
    - **0% Waste / 0% ቀርቶ አይጠፋ** → Discipline & accountability / ትክክለኛ ስራና ሀላፊነት
    """)

# ==========================
# LEADERSHIP HANDBOOK
# ==========================
elif page == "leadership":
    st.title("🔑 Leadership Handbook / የአመራር መመሪያ")
    with st.expander("Chapter 1: Initiative Is Leadership / ምዕራፍ 1: እንቅስቃሴ መሪነት ነው"):
        st.write("Leadership begins with action, not permission. / መሪነት በተግባር ይጀምራል፣ በፈቃድ ሳይኖረው።")

    with st.expander("Chapter 2: Responsibility Without Authority / ምዕራፍ 2: ሀላፊነት በሥልጣን ሳይኖረው"):
        st.write("Ownership is a mindset, not a title. / ሀላፊነት አሳብ ነው፣ ስም አይደለም።")

# ==========================
# MEMBER BENEFITS
# ==========================
elif page == "benefits":
    st.header("🤝 Member Benefits / የአባላት ጥቅሞች")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("🤝 Community / ማህበረሰብ")
        st.write("Strong, trusted membership / በትክክለኛነት የተሰጠ አባላት")
    with col2:
        st.subheader("💰 Fair Loans / የፍትህ ብድር")
        st.write("Access flexible and fair financing / የተለዋዋጭና ፍትህ ያለው ዕድል")
    with col3:
        st.subheader("📈 Shared Growth / ተጋላጭ እድገት")
        st.write("Benefit as EGSA grows / EGSA እየነደገ ጥቅም ማግኘት")

# ==========================
# HOW IT WORKS
# ==========================
elif page == "how":
    st.header("⚙️ How It Works / እንዴት እንደሚሰራ")
    st.markdown("""
    1. Members contribute regularly / አባላት በመደበኛ ሁኔታ ይስጡ
    2. Funds are invested systematically / ገንዘብ በስርዓት ይገባል
    3. Members access loans / አባላት ብድር ይወሰዳሉ
    4. Benefits are shared fairly / ጥቅሞች በፍትህ ይከፋፈላሉ
    """)

# ==========================
# JOIN EGSA2025
# ==========================
elif page == "join":
    st.header("📩 Join EGSA2025 / አባል ይሁኑ")
    st.markdown("""
    📞 **Phone / ስልክ:** +251 912 861 288  
    📧 **Email / ኢሜይል:** walfanamegersa3@gmail.com
    """)
    if st.button("Join Now / አባል ይሁኑ አሁን"):
        st.success("Thank you! We will contact you soon. / አመሰግናለን! በቅርቡ እናገናኝላችኋለን።")

# ==========================
# FOOTER MESSAGE (display on all pages)
# ==========================
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color: gray;'>EGSA2025 PLC – Empowering the new generation / ኢግሳ2025 ፒኤልሲ – አዲሱን ትውልድ ኃይል ማድረግ</p>",
    unsafe_allow_html=True
)
