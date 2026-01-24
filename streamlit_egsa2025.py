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
# PAGES
# ==========================
if page == "🏠 Home":
    st.title("🏠 Welcome to EGSA2025")
    st.write("Home Page Content Here")

elif page == "🔑 Leadership Handbook":
    st.title("🔑 Be the Key, But the Solution Doesn’t Matter")

    with st.expander("Chapter 1: Initiative Is Leadership"):
        st.write("Leadership begins with action, not permission.")
        st.write("አመራር ከፈቃድ አይጀምርም፤ ከእርምጃ ይጀምራል።")

    with st.expander("Chapter 2: Responsibility Without Authority"):
        st.write("Ownership is a mindset, not a title.")
        st.write("ባለቤትነት ስም አይደለም፤ አእምሮ ነው።")

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
        st.write("Even small consistent actions can create major impact.")
        st.write("ትንሽ የቀጥታ እርምጃዎች ትልቅ ተፅዕኖ ማፍጠር ይችላሉ።")

    with st.expander("Chapter 4: Every Member Is a Key"):
        st.write("Every role, no matter how small, matters. Identify how we can contribute uniquely to EGSA2025 and act consistently.")
        st.write("እያንዳንዱ አባል ቁልፍ ነው። ስለ EGSA2025 በልዩ መንገድ እንዴት እንረዳ እና ትክክለኛ እንሆን ማወቅ አለብን።")

    with st.expander("Chapter 5: Collective Keys"):
        st.write("Multiple keys working together open doors to bigger achievements. Collaboration amplifies impact and strengthens the organization.")
        st.write("ብዙ ቁልፎች በመስራት ወደ ትልቅ ስኬቶች በማንፀባረቅ ማደርግ ይቻላል። መተባበር ተፅዕኖን ያጨምራል እና ድርጅቱን ያጠናክራል።")

    with st.expander("Chapter 6: Measuring What Matters"):
        st.write("Impact is not only in numbers. Contributions, learning, trust, initiative, and collaboration are essential metrics for growth.")
        st.write("ተፅዕኖ ቁጥር ብቻ አይደለም። እርምጃዎች፣ ትምህርት፣ እምነት፣ ተነሳሽነት፣ እና መተባበር ለእድገት አስፈላጊ መለኪያዎች ናቸው።")
