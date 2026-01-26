import streamlit as st
import pandas as pd
import altair as alt

# ==========================
# PAGE SETUP
# ==========================
st.set_page_config(
    page_title="EGSA2025 PLC",
    layout="wide"
)

# ==========================
# SIDEBAR NAVIGATION
# ==========================
st.sidebar.image(
    "https://github.com/Walfaanaa/EGSA/raw/main/EGSA.png",
    width=120
)
st.sidebar.title("EGSA2025")
page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "📘 Financial Strategy",
        "🔑 Leadership Handbook",
        "📄 Strategic Action Plan",
        "🤝 Member Benefits",
        "⚙️ How It Works",
        "📩 Join EGSA2025",
    ],
)

# ==========================
# PAGES
# ==========================
# ---------- HOME ----------
if page == "🏠 Home":
    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        st.image(
            "https://github.com/Walfaanaa/EGSA/raw/main/EGSA.png",
            width=80
        )
    with col2:
        st.title("🏠 Welcome to EGSA2025")
    st.write("Home Page Content Here")

# ---------- LEADERSHIP HANDBOOK ----------
elif page == "🔑 Leadership Handbook":
    col1, col2 = st.columns([1, 6])
    with col1:
        st.image(
            "https://github.com/Walfaanaa/EGSA/raw/main/EGSA.png",
            width=80
        )
    with col2:
        st.title("🔑 Be the Key, But the Solution Doesn’t Matter")

    with st.expander("Chapter 1: Initiative Is Leadership"):
        st.write(
            "Leadership begins with action, not permission. "
            "አመራር ከፈቃድ አይጀምርም፤ ከእርምጃ ይጀምራል።"
        )

    with st.expander("Chapter 2: Responsibility Without Authority"):
        st.write(
            "Ownership is a mindset, not a title. "
            "ባለቤትነት ስም አይደለም፤ አእምሮ ነው።"
        )

    with st.expander("Chapter 3: Small Keys Open Big Doors"):
        data = pd.DataFrame({
            "Action": ["Small", "Consistent", "Collective"],
            "Impact": [1, 4, 8]
        })
        chart = (
            alt.Chart(data)
            .mark_bar()
            .encode(
                x="Action",
                y="Impact"
            )
        )
        st.altair_chart(chart, use_container_width=True)
        st.write(
            "Even small consistent actions can create major impact. "
            "ትንሽ የቀጥታ እርምጃዎች ትልቅ ተፅዕኖ ማፍጠር ይችላሉ።"
        )

    with st.expander("Chapter 4: Every Member Is a Key"):
        st.write(
            "Every role, no matter how small, matters. Identify how we can contribute uniquely to EGSA2025 and act consistently. "
            "እያንዳንዱ አባል ቁልፍ ነው። ስለ EGSA2025 በልዩ መንገድ እንዴት እንረዳ እና ትክክለኛ እንሆን ማወቅ አለብን።"
        )

    with st.expander("Chapter 5: Collective Keys"):
        st.write(
            "Multiple keys working together open doors to bigger achievements. Collaboration amplifies impact and strengthens the organization. "
            "ብዙ ቁልፎች በመስራት ወደ ትልቅ ስኬቶች በማንፀባረቅ ማደርግ ይቻላል። መተባበር ተፅዕኖን ያጨምራል እና ድርጅቱን ያጠናክራል።"
        )

    with st.expander("Chapter 6: Measuring What Matters"):
        st.write(
            "Impact is not only in numbers. Contributions, learning, trust, initiative, and collaboration are essential metrics for growth. "
            "ተፅዕኖ ቁጥር ብቻ አይደለም። እርምጃዎች፣ ትምህርት፣ እምነት፣ ተነሳሽነት፣ እና መተባበር ለእድገት አስፈላጊ መለኪያዎች ናቸው።"
        )

# ---------- STRATEGIC ACTION PLAN ----------
elif page == "📄 Strategic Action Plan":
    col1, col2 = st.columns([1, 6])
    with col1:
        st.image(
            "https://github.com/Walfaanaa/EGSA/raw/main/EGSA.png",
            width=80
        )
    with col2:
        st.title("📄 EGSA Internal Strategic Action Plan (2025–2027)")

    with st.expander("Executive Summary"):
        st.write(
            "The Economic Growth Solution Association (EGSA) is a member-based organization "
            "dedicated to promoting sustainable economic empowerment through savings, loans, "
            "and community-driven investments. EGSA aims to be a holistic solution hub for Ethiopia, "
            "addressing critical sectors such as education, health, transportation, agriculture, housing, "
            "and economic development, while empowering members economically. This strategic action plan "
            "outlines a roadmap for growth, digital transformation, and multi-sector community impact "
            "between 2025 and 2027."
        )

    with st.expander("Vision & Mission"):
        st.write(
            "**Vision:** To be a model cooperative using digital innovation and community capital "
            "to build sustainable economic independence for members, while serving as a national "
            "development solution hub addressing Ethiopia’s critical social and economic challenges.\n\n"
            "**Mission:** To empower members economically and socially through savings mobilization, "
            "investment in local opportunities, digital solutions, and continuous capacity building "
            "in key sectors like education, health, transport, agriculture, and housing."
        )

    with st.expander("Core Values"):
        st.write(
            "- Integrity: Ensuring transparency and accountability in all operations.\n"
            "- Innovation: Embracing digital and financial technologies for growth.\n"
            "- Teamwork: Collective action and shared ownership among members.\n"
            "- Empowerment: Enhancing skills and opportunities for economic advancement.\n"
            "- Sustainability: Promoting long-term social, economic, and environmental resilience."
        )

    with st.expander("Strategic Objectives (2025–2027)"):
        st.write(
            "1. Build a fully digital cooperative management system for EGSA operations.\n"
            "2. Diversify investments into profitable and low-risk local enterprises.\n"
            "3. Strengthen member skills and entrepreneurship through training and mentorship.\n"
            "4. Establish EGSA as a trusted brand recognized for transparency and innovation.\n"
            "5. Expand partnerships with local government, financial institutions, and development partners.\n"
            "6. Introduce modern community-based financial systems like Uqub to mobilize capital and foster inclusion.\n"
            "7. Address critical housing shortages by promoting affordable, sustainable housing solutions."
        )

    with st.expander("Implementation Framework"):
        st.write(
            "**Phase 1 (0–6 months):** Digitalization & Branding – EGSA App launched, digital member registration, improved transparency\n"
            "**Phase 2 (6–12 months):** Financial Expansion – Micro-investment fund established, 40% growth in member assets\n"
            "**Phase 3 (Year 2):** Skill & Investment Growth – Business training center operational, active partnerships with SMEs\n"
            "**Phase 4 (Year 3):** Scaling & Replication – Regional expansion, stronger brand recognition, external investment attraction"
        )

    with st.expander("Digital Cooperative Capitalization (DCC)"):
        st.write(
            "Each member contributes financially and via participation, training engagement, "
            "and transaction activity. This generates a Digital Capital Index (DCI) measuring each member's "
            "contribution and reliability, guiding loan access and attracting partnerships."
        )

    with st.expander("Community-Based Financial Innovation: Modern Uqub System"):
        st.write(
            "**Key Actions:**\n"
            "1. Digital Uqub Platform – digital rotating savings inside the EGSA app.\n"
            "2. Transparent Record Management – all uqub activities recorded digitally.\n"
            "3. Inclusive Expansion – allow community groups to form uqub under EGSA.\n"
            "4. Investment Integration – channel part of uqub savings into investment funds.\n"
            "5. Economic Empowerment – use uqub for microcredit, emergency funds, and social insurance."
        )

    with st.expander("Holistic Future Plan for Ethiopia"):
        st.write(
            "**Sectoral Development:**\n"
            "1. Education – scholarships, vocational training, youth entrepreneurship.\n"
            "2. Healthcare – community health campaigns, clinic support, micro-insurance.\n"
            "3. Transportation & Infrastructure – small transport services, community logistics, green mobility.\n"
            "4. Agriculture – microloans, cooperative hubs, climate-smart farming.\n"
            "5. Housing – affordable housing, microfinance, sustainable construction.\n"
            "6. Economic & Community Development – digital financial services, SME incubators, DCC for community projects.\n\n"
            "**Implementation Idea:**\n"
            "- 2025: Finance & Digital Uqub\n"
            "- 2026: Agriculture & Education\n"
            "- 2027: Health, Housing & Transport"
        )

    with st.expander("Monitoring and Evaluation"):
        st.write(
            "EGSA will track performance via quarterly reviews, annual reports, and a centralized digital dashboard. "
            "Key indicators include member growth, capital increase, investment returns, training participation, "
            "housing projects completed, and sectoral development impacts."
        )

    with st.expander("Conclusion"):
        st.write(
            "This strategic action plan provides EGSA with a roadmap for economic growth, digital transformation, "
            "and sustainable multi-sector community impact. By integrating modern financial tools, traditional uqub practices, "
            "and targeted sectoral interventions, EGSA is positioned to become a national solution hub addressing Ethiopia’s most critical challenges."
        )
