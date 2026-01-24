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
st.sidebar.title("EGSA2025")
page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home / መነሻ",
        "📘 Financial Strategy / የገንዘብ ዘዴ",
        "🔑 Leadership Handbook / የአመራር መመሪያ",
        "🤝 Member Benefits / የአባላት ጥቅሞች",
        "⚙️ How It Works / እንዴት እንደሚሰራ",
        "📩 Join EGSA2025 / አባል ይሁኑ",
    ],
)

# ==========================
# HOME
# ==========================
if page == "🏠 Home / መነሻ":

    # --- Centered Logo ---
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(
            "https://github.com/Walfaanaa/EGSA/blob/main/EGSA.png?raw=true",
            use_container_width=True
        )

    # --- Centered Title ---
    st.markdown(
        "<h1 style='text-align: center;'>Welcome to <b>EGSA2025 PLC</b> / እንኳን ወደ <b>EGSA2025 PLC</b> በደህና መጡ</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<h4 style='text-align: center;'>Empowering the New Generation of Investors / አዲሱን ትውልድ የተጠናቀቀ በኢንቨስትመንት ኃይል ማበረታታት</h4>",
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
    ኢግሳ2025 በአባላት የተመሠረተ ነው፣ እነሱም የራሳቸውን ተግባር የሚመራ እና በቅንነት የሚመራ ሲሆን፣ ውጤት የሚያመጣውን በተገቢ ኃይል ላይ ያቀናሉ።  

    This handbook is a guide to empower every member to contribute meaningfully, inspire others, and grow personally and collectively.  
    ይህ መመሪያ እያንዳንዱን አባል በሚገባ ለመስጠት፣ ሌሎችን ለማነሳት እና ለግል እና ለቡድን እድገት የሚያግዝ መርምሮ ነው።
    """)

    st.markdown("---")

    # --- Mission & Vision Section ---
    st.markdown(
        '<span style="color:green; font-weight:bold; font-size:22px;">OUR MISSION & VISION / ተልዕኮና ራዕይ</span>',
        unsafe_allow_html=True
    )
    st.markdown("""
    **Our Mission / ተልዕኮ:**  
    - Provide accessible and fair opportunities for our members / ለአባላት ቀላል እና እኩል እድሎች ማቅረብ  
    - Foster a strong, engaged financial community / ጠንካራ የገንዘብ ማህበር ማበረታታት  
    - Build sustainable growth and value for everyone involved / ለሁሉም ተገቢ እድገትና እሴት ማቋቋም  

    **Our Vision / ራዕይ:**  
    To be the leading platform for financial empowerment among the new generation / በአዲሱ ትውልድ የገንዘብ ኃይል ማበረታታት የሚያስችል ዋና መድረክ መሆን
    """)

    st.markdown("---")

    # --- Main Banner Image (Centered) ---
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image(
            "https://github.com/Walfaanaa/EGSA/blob/main/EGSA%20Logo.png?raw=true",
            use_container_width=True
        )

    st.markdown("""
    **EGSA2025 PLC** is a member-based organization built on trust, discipline,
    and long-term financial growth. / ኢግሳ2025 PLC በአባላት ተመሠረት የተደረገ ተቋም ሲሆን፣ በታማኝነት፣ በትክክለኛነትና በረጅም ጊዜ የገንዘብ እድገት የተመሠረተ ነው።

    We believe / እኛ እንደምናመን:

    - **Systems matter more than emotions / ስርዓቶች ከስሜቶች ይሻላሉ**
    - **Effort matters more than outcomes / ጥረት ከውጤት ይሻላል**
    """)

    st.markdown("---")

    # --- Footer Message ---
    st.markdown(
        "<p style='text-align:center; color:gray;'>© 2026 EGSA2025 PLC | እያንዳንዱ አባል ይኑር ፣ ለተግባርና ለአንድነት ተሳትፎ ይሁን</p>",
        unsafe_allow_html=True
    )
