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
        "🏠 Home",
        "📘 Financial Strategy",
        "🔑 Leadership Handbook",
        "🤝 Member Benefits",
        "⚙️ How It Works",
        "📩 Join EGSA2025",
    ],
)

# ==========================
# HOME
# ==========================
if page == "🏠 Home":

    # --- Centered Logo ---
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(
            "https://github.com/Walfaanaa/EGSA/blob/main/EGSA.png?raw=true",
            use_container_width=True
        )

    # --- Centered Title ---
    st.markdown(
        "<h1 style='text-align: center;'>Welcome to <b>EGSA2025 PLC</b></h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<h4 style='text-align: center;'>Empowering the New Generation of Investors</h4>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    # --- Introduction Section ---
    st.markdown(
        '<span style="color:blue; font-weight:bold; font-size:22px;">INTRODUCTION</span>',
        unsafe_allow_html=True
    )
    st.write("""
    EGSA2025 is built by members who take initiative, lead with integrity, and focus on effort rather than immediate results. 
    This handbook is a guide to empower every member to contribute meaningfully, inspire others, and grow personally and collectively.
    """)

    st.markdown("---")

    # --- Mission & Vision Section ---
    st.markdown(
        '<span style="color:green; font-weight:bold; font-size:22px;">OUR MISSION & VISION</span>',
        unsafe_allow_html=True
    )
    st.markdown("""
    **Our Mission:**  
    - Provide accessible and fair opportunities for our members.  
    - Foster a strong, engaged financial community.  
    - Build sustainable growth and value for everyone involved.  

    **Our Vision:**  
    To be the leading platform for financial empowerment among the new generation.
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
    and long-term financial growth.

    We believe:

    - **Systems matter more than emotions**
    - **Effort matters more than outcomes**
    """)

# ==========================
# FINANCIAL STRATEGY
# ==========================
elif page == "📘 Financial Strategy":
    st.header("📘 EGSA Financial Strategy")

    st.markdown("""
    EGSA follows a **system-driven financial model**:

    - **80% Investment** → Growth & wealth creation  
    - **20% Savings** → Security & stability  
    - **0% Waste** → Discipline & accountability
    """)

# ==========================
# LEADERSHIP HANDBOOK
# ==========================
elif page == "🔑 Leadership Handbook":
    st.title("🔑 Be the Key, But the Solution Doesn’t Matter")

    with st.expander("Chapter 1: Initiative Is Leadership"):
        st.write("Leadership begins with action, not permission.")

    with st.expander("Chapter 2: Responsibility Without Authority"):
        st.write("Ownership is a mindset, not a title.")

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

    # --- New Chapters 4, 5, 6 ---
    with st.expander("🔑 Chapter 4: Every Member Is a Key"):
        st.write("Every role, no matter how small, matters. Identify how we can contribute uniquely to EGSA2025 and act consistently.")

    with st.expander("🔑 Chapter 5: Collective Keys"):
        st.write("Multiple keys working together open doors to bigger achievements. Collaboration amplifies impact and strengthens the organization.")

    with st.expander("🔑 Chapter 6: Measuring What Matters"):
        st.write("Impact is not only in numbers. Contributions, learning, trust, initiative, and collaboration are essential metrics for growth.")

# ==========================
# MEMBER BENEFITS
# ==========================
elif page == "🤝 Member Benefits":
    st.header("Why Join EGSA2025?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🤝 Community")
        st.write("Strong, trusted membership")

    with col2:
        st.subheader("💰 Fair Loans")
        st.write("Access flexible and fair financing")

    with col3:
        st.subheader("📈 Shared Growth")
        st.write("Benefit as EGSA grows")

# ==========================
# HOW IT WORKS
# ==========================
elif page == "⚙️ How It Works":
    st.header("⚙️ How EGSA2025 Works")

    st.markdown("""
    1. Members contribute regularly  
    2. Funds are invested systematically  
    3. Members access loans  
    4. Benefits are shared fairly
    """)

# ==========================
# JOIN EGSA2025
# ==========================
elif page == "📩 Join EGSA2025":
    st.header("Become a Member")

    st.markdown("""
    📞 **Phone:** +251 912 861 288  
    📧 **Email:** walfanamegersa3@gmail.com
    """)

    if st.button("Join Now"):
        st.success("Thank you! We will contact you soon.")
