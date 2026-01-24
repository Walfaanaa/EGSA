import streamlit as st
import pandas as pd
import altair as alt

# ==========================
# Page Setup
# ==========================
st.set_page_config(page_title="EGSA2025 PLC", layout="wide")

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

    col_logo, col_title = st.columns([1, 6])

    with col_logo:
        st.image(
            "https://github.com/Walfaanaa/EGSA/blob/main/EGSA.png?raw=true",
            width=90
        )

    with col_title:
        st.markdown("## Welcome to **EGSA2025 PLC**")
        st.subheader("Empowering the New Generation of Investors")

    st.image(
        "https://github.com/Walfaanaa/EGSA/blob/main/EGSA%20Logo.png?raw=true",
        width=500
    )

    st.markdown("""
    **EGSA2025 PLC** is a member-based organization built on trust, discipline,
    and long-term financial growth.

    We believe **systems matter more than emotions**
    and **effort matters more than outcomes**.
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

        st.altair_chart(
            alt.Chart(data)
            .mark_bar()
            .encode(x="Action", y="Impact"),
            use_container_width=True
        )

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
    st.markdown("""
    1. Members contribute regularly  
    2. Funds are invested systematically  
    3. Members access loans  
    4. Benefits are shared fairly
    """)

# ==========================
# JOIN
# ==========================
elif page == "📩 Join EGSA2025":
    st.header("Become a Member")

    st.markdown("""
    📞 **Phone:** +251912861288  
    📧 **Email:** walfanamegersa3@gmail.com
    """)

    if st.button("Join Now"):
        st.success("Thank you! We will contact you soon.")
