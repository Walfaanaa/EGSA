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
# SIDEBAR WITH LOGO
# ==========================
st.sidebar.image(
    "https://github.com/Walfaanaa/EGSA/raw/main/EGSA.png",
    width=120
)
st.sidebar.title("EGSA2025")

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
# CENTERED LOGO FUNCTION
# ==========================
def display_centered_logo(width=150):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(
            "https://github.com/Walfaanaa/EGSA/raw/main/EGSA.png",
            width=width
        )

# ==========================
# PAGES
# ==========================

# ---------- HOME ----------
if page == "Home":
    display_centered_logo()
    st.title("🏠 Welcome to EGSA2025")
    st.write("Home Page Content Here")

# ---------- FINANCIAL STRATEGY ----------
elif page == "Financial Strategy":
    display_centered_logo()
    st.title("📘 Financial Strategy")

    st.write(
        "EGSA2025 tracks key financial activities to ensure transparency, growth, and member empowerment. "
        "The main financial indicators include:"
    )

    # Display highlighted points without values
    st.markdown("### Key Financial Metrics")
    st.markdown("- **Monthly Contributions** – Amount each member contributes every month.")
    st.markdown("- **Quarterly Contributions** – Aggregated contributions for each quarter.")
    st.markdown("- **Service Charges Collected** – Fees collected for services provided by EGSA.")
    st.markdown("- **Uqub Pick Sold** – Income from rotating savings groups or uqub activities.")
    st.markdown("- **Grain Buy and Sell Profit** – Earnings from trading grain or agricultural products.")

    st.write(
        "Tracking these indicators helps EGSA plan finances, reward members, and make informed investment decisions."
    )

# ---------- LEADERSHIP HANDBOOK ----------
elif page == "Leadership Handbook":
    display_centered_logo()
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
elif page == "Strategic Action Plan":
    display_centered_logo()
    st.title("📄 EGSA Internal Strategic Action Plan (2025–2027)")

    # Expanders for content as before...

# ---------- MEMBER BENEFITS ----------
elif page == "Member Benefits":
    display_centered_logo()
    st.title("🤝 Member Benefits")
    st.write("Member Benefits Content Here")

# ---------- HOW IT WORKS ----------
elif page == "How It Works":
    display_centered_logo()
    st.title("⚙️ How It Works")
    st.write("How It Works Content Here")

# ---------- JOIN EGSA2025 ----------
elif page == "Join EGSA2025":
    display_centered_logo()
    st.title("📩 Join EGSA2025")
    st.write("Join EGSA2025 Content Here")
