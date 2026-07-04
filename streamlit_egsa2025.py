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

# ✅ YOUR VOICE FILE (UPDATED)
AUDIO_URL = "https://raw.githubusercontent.com/Walfaanaa/EGSA/main/vioce.mp3"


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
# GLOBAL INTRO
# ==========================
def show_global_intro():
    st.markdown(
        "<h2 style='text-align:center; color:#2563eb;'>🎬 EGSA2025 Intro</h2>",
        unsafe_allow_html=True
    )

    speed = st.slider("⏱️ Text Speed (seconds per line)", 1.0, 5.0, 2.5, 0.5)

    # ✅ AUDIO + TEXT
    if st.button("▶️ Start Intro (Audio + Text)"):
        st.audio(AUDIO_URL)  # plays your vioce.mp3
        egsa_intro_text_part_by_part(speed=speed)

    st.markdown("---")


# ==========================
# SHOW GLOBAL COMPONENTS
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
            font-family: Arial;
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
- Interest from loan
""")


elif page == "Leadership Handbook":
    st.title("🔑 Leadership Handbook")

    with st.expander("Chapter 1"):
        st.write("Leadership begins with action, not permission.")

    with st.expander("Chapter 2"):
        st.write("Ownership is a mindset, not a title.")

    with st.expander("Chapter 3"):
        data = pd.DataFrame({
            "Action": ["Small", "Consistent", "Collective"],
            "Impact": [1, 4, 8]
        })

        chart = alt.Chart(data).mark_bar().encode(
            x="Action",
            y="Impact"
        )

        st.altair_chart(chart, use_container_width=True)


elif page == "Strategic Action Plan":
    st.title("📄 Strategic Action Plan")
    st.write("Full EGSA strategic roadmap 2025–2027")


elif page == "Member Benefits":
    st.title("🤝 Member Benefits")
    st.write("""
- Savings & Loans  
- Investment Opportunities  
- Skill Development  
- Networking  
- Financial Inclusion  
""")


elif page == "How It Works":
    st.title("⚙️ How It Works")
    st.write("""
1. Join EGSA  
2. Save Money  
3. Access Loans  
4. Invest  
5. Grow Together  
""")


elif page == "Join EGSA2025":
    st.title("📩 Join EGSA2025")
    st.write("""
Phone: +251912861288  
Email: walfanamegersa3@gmail.com
""")
