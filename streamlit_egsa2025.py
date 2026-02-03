import streamlit as st
import pandas as pd
import altair as alt
import time

# ==========================
# PAGE SETUP
# ==========================
st.set_page_config(page_title="EGSA2025 PLC", layout="wide")

# ==========================
# FILE LINKS (RAW GitHub)
# ==========================
LOGO_URL = "https://raw.githubusercontent.com/Walfaanaa/EGSA/main/EGSA.png"

# ✅ Your GitHub MP3 (RAW link)
AUDIO_URL = "https://raw.githubusercontent.com/Walfaanaa/EGSA/main/page_1.mp3"


# ==========================
# SIDEBAR WITH ANIMATED LOGO
# ==========================
st.sidebar.markdown(
    f"""
    <div style="text-align:center; padding-top:10px;">
        <img src="{LOGO_URL}" width="120"
        style="
            border-radius: 50%;
            animation: spinGlow 4s linear infinite;
            box-shadow: 0px 0px 15px rgba(34,197,94,0.8);
        ">
        <h2 style="color:#16a34a; margin-top:10px;">EGSA2025</h2>
    </div>

    <style>
    @keyframes spinGlow {{
        0%   {{ transform: rotate(0deg) scale(1);   filter: brightness(1); }}
        50%  {{ transform: rotate(180deg) scale(1.08); filter: brightness(1.3); }}
        100% {{ transform: rotate(360deg) scale(1); filter: brightness(1); }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar menu
page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "Financial Strategy",
        "Leadership Handbook",
        "Strategic Action Plan",
        "Member Benefits",
        "How It Works",
        "Join EGSA2025"
    ]
)


# ==========================
# CENTERED ANIMATED LOGO
# ==========================
def display_centered_animated_logo(width=250):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            f"""
            <div style="text-align:center;">
                <img src="{LOGO_URL}" width="{width}"
                style="
                    border-radius: 20px;
                    animation: bounceZoom 2.5s ease-in-out infinite;
                    box-shadow: 0px 0px 25px rgba(217,70,239,0.7);
                ">
            </div>

            <style>
            @keyframes bounceZoom {{
                0%   {{ transform: translateY(0px) scale(1); }}
                25%  {{ transform: translateY(-10px) scale(1.03); }}
                50%  {{ transform: translateY(0px) scale(1.06); }}
                75%  {{ transform: translateY(-10px) scale(1.03); }}
                100% {{ transform: translateY(0px) scale(1); }}
            }}
            </style>
            """,
            unsafe_allow_html=True
        )


# ==========================
# INTRO TEXT PART BY PART
# ==========================
def egsa_intro_text_part_by_part(speed=2.5):
    lines = [
        "🎉 Welcome to EGSA2025!",
        "🌍 Economic Growth Solution Association",
        "💰 We build savings, loans, and investment opportunities for members.",
        "🤝 Together we grow stronger through unity and trust.",
        "📈 EGSA2025 is a digital cooperative for sustainable economic success.",
        "✅ Thank you for being part of EGSA2025!"
    ]

    placeholder = st.empty()

    for line in lines:
        placeholder.markdown(
            f"""
            <div style="
                text-align:center;
                font-size:38px;
                font-weight:bold;
                font-family:Arial;
                color:#16a34a;
                animation: fadeIn 1s ease-in-out;
                padding:18px;
            ">
                {line}
            </div>

            <style>
            @keyframes fadeIn {{
                0%   {{opacity:0; transform:translateY(10px);}}
                100% {{opacity:1; transform:translateY(0px);}}
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        time.sleep(speed)


# ==========================
# GLOBAL INTRO (SHOW ON ALL PAGES)
# ==========================
def show_global_intro():
    st.markdown(
        "<h2 style='text-align:center; color:#2563eb;'>🎬 EGSA2025 Intro</h2>",
        unsafe_allow_html=True
    )

    speed = st.slider("⏱️ Text Speed (seconds per line)", 1.0, 5.0, 2.5, 0.5)

    # ✅ One button: Audio + Text
    if st.button("▶️ Start Intro (Audio + Text)"):
        st.audio(AUDIO_URL, format="audio/mp3")
        egsa_intro_text_part_by_part(speed=speed)

    st.markdown("---")


# ==========================
# SHOW LOGO + INTRO ON ALL PAGES
# ==========================
display_centered_animated_logo(width=240)
show_global_intro()


# ==========================
# PAGES
# ==========================
if page == "Home":
    st.markdown(
        """
        <h1 style="
            text-align: center;
            font-family: Arial, sans-serif;
            font-size: 50px;
            animation: colorChange 10s infinite;
        ">
            Welcome to EGSA2025
        </h1>

        <style>
        @keyframes colorChange {
            0% { color: #16a34a; }
            25% { color: #2563eb; }
            50% { color: #f59e0b; }
            75% { color: #d946ef; }
            100% { color: #16a34a; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )


elif page == "Financial Strategy":
    st.title("📘 Financial Strategy")
    st.write("""
- Monthly Contribution  
- Quarterly Contribution  
- Service Charge Collected  
- Uqub Pick Sold  
- Grain Buy and Sell Profit
""")


elif page == "Leadership Handbook":
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


elif page == "Strategic Action Plan":
    st.title("📄 EGSA Internal Strategic Action Plan (2025–2027)")

    st.markdown("**Prepared by:** Founder & Executive Director  \n**Location:** Sheger City  \n**Date:** October 31, 2025")

    with st.expander("Executive Summary"):
        st.write(
            """The Economic Growth Solution Association (EGSA) is a member-based organization 
dedicated to promoting sustainable economic empowerment through savings, loans, 
and community-driven investments. This internal strategic action plan outlines a 
roadmap for growth and digital transformation between 2025 and 2027."""
        )

    with st.expander("Vision"):
        st.write(
            """To be a model cooperative using digital innovation and community capital 
to build sustainable economic independence for members."""
        )

    with st.expander("Mission"):
        st.write(
            """To empower members economically through savings mobilization, investment in local opportunities, 
digital solutions, and continuous capacity building."""
        )

    with st.expander("Core Values"):
        st.write(
            """- **Integrity** – ensuring transparency and accountability in all operations.
- **Innovation** – embracing digital and financial technologies for growth.
- **Teamwork** – collective action and shared ownership among members.
- **Empowerment** – enhancing skills and opportunities for economic advancement.
- **Sustainability** – promoting long-term social and financial resilience."""
        )

    with st.expander("Strategic Objectives (2025–2027)"):
        st.write(
            """1. Build a fully digital cooperative management system for EGSA operations.
2. Diversify investments into profitable and low-risk local enterprises.
3. Strengthen member skills and entrepreneurship through training and mentorship.
4. Establish EGSA as a trusted brand recognized for transparency and innovation.
5. Expand partnerships with local government, financial institutions, and development partners."""
        )

    with st.expander("Implementation Framework"):
        st.write(
            """The implementation will be phased over three years to ensure sustainable rollout and impact.

**Phase 1 (0–6 months):** Digitalization & Branding – EGSA App launched, digital member registration, improved transparency.
**Phase 2 (6–12 months):** Financial Expansion – Micro-investment fund established, 40% growth in member assets.
**Phase 3 (Year 2):** Skill & Investment Growth – Business training center operational, active partnerships with SMEs.
**Phase 4 (Year 3):** Scaling & Replication – Regional expansion, stronger brand recognition, external investment attraction."""
        )

    with st.expander("Unique Strategy: Digital Cooperative Capitalization (DCC)"):
        st.write(
            """EGSA introduces the 'Digital Cooperative Capitalization' model, where each member contributes 
not only financially but also through participation data, training engagement, and transaction activity. 
This creates a Digital Capital Index (DCI) that measures each member’s economic contribution and reliability. 
The DCI can be used internally to guide loan access and externally to attract partnerships and funding."""
        )

    with st.expander("Monitoring and Evaluation"):
        st.write(
            """EGSA will track performance through quarterly reviews, annual reports, and a centralized digital dashboard. 
Key indicators include member growth, capital increase, investment return rates, and training participation."""
        )

    with st.expander("Conclusion"):
        st.write(
            """This internal strategic action plan provides EGSA with a clear roadmap for achieving economic growth, 
digital transformation, and sustainable community impact. Effective implementation will require 
commitment, transparency, and continuous innovation across all levels of the association."""
        )


elif page == "Member Benefits":
    st.title("🤝 Member Benefits")
    st.write("""
EGSA members enjoy the following benefits:

- **Savings & Loans Access** – Participate in digital savings programs and access low-interest loans.
- **Investment Opportunities** – Join community-based investment projects and profit-sharing schemes.
- **Skill Development** – Receive training in entrepreneurship, agriculture, finance, and digital tools.
- **Networking & Collaboration** – Connect with like-minded members and local development partners.
- **Financial Inclusion** – Benefit from Uqub and other community-based financial innovations.
- **Social Impact Participation** – Contribute to projects in education, health, housing, and agriculture.
""")


elif page == "How It Works":
    st.title("⚙️ How It Works")
    st.write("""
EGSA operates through a simple, member-driven process:

1. **Join EGSA** – Become a registered member via digital registration.
2. **Contribute Savings** – Participate in monthly, quarterly, and Uqub contributions.
3. **Access Services** – Use savings for loans, micro-investments, or community projects.
4. **Participate in Training** – Enhance your skills through workshops, mentorship, and digital courses.
5. **Engage in Community Projects** – Invest in local development initiatives like housing, agriculture, or education.
6. **Track Impact** – Members can monitor their contributions and participation through the EGSA digital dashboard.
7. **Grow Together** – Collective action and shared responsibility ensure sustainable growth and benefits for all members.
""")


elif page == "Join EGSA2025":
    st.title("📩 Join EGSA2025")
    st.write("""
You can join EGSA2025 or contact us via:  

**Phone:** +251912861288  
**Email:** walfanamegersa3@gmail.com
""")
