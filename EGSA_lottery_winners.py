# -------------------------------
# 🎟️ EGSA Uqub Lottery App
# -------------------------------

import streamlit as st
import pandas as pd
import random
from io import BytesIO
from datetime import datetime

# -------------------------------
# Page Setup
# -------------------------------
st.set_page_config(page_title="🎟️ EGSA Uqub Lottery", layout="wide")
st.title("🎟️ EGSA Uqub Lottery App (Random & Transparent)")

# -------------------------------
# 1️⃣ Load Members Data (GitHub or Upload)
# -------------------------------
use_github = st.checkbox("🔗 Load data from GitHub", value=True)

if use_github:
    GITHUB_FILE_URL = "https://github.com/Walfaanaa/EGSA/raw/refs/heads/main/EGSA_uqub_members.xlsx"
    try:
        df = pd.read_excel(GITHUB_FILE_URL, engine='openpyxl')
        st.success("✅ Members data loaded successfully from GitHub!")
    except Exception as e:
        st.error(f"❌ Error loading file from GitHub: {e}")
        st.stop()
else:
    members_file = st.file_uploader("📂 Upload members file (CSV/XLSX)", type=["csv", "xlsx"])
    if members_file:
        if members_file.name.endswith(".csv"):
            df = pd.read_csv(members_file)
        else:
            df = pd.read_excel(members_file, engine='openpyxl')
        st.success("✅ Members data loaded successfully from upload.")
    else:
        st.stop()

# Ensure phone numbers are strings and index is 1-based
df['Phone_no'] = df['Phone_no'].astype(str)
df.index = range(1, len(df) + 1)

st.dataframe(df)

# -------------------------------
# 2️⃣ Number of Winners
# -------------------------------
num_winners = st.number_input(
    "How many winners to pick?", 
    min_value=1, max_value=len(df), value=1
)

# -------------------------------
# 3️⃣ Pick Random Winner(s)
# -------------------------------
if st.button("🎯 Pick Random Winner(s)"):
    random.seed()  # Different result each click
    winner = df.sample(n=num_winners, random_state=None)
    
    # Draw timestamp
    draw_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    st.success(f"🎉 Winner(s) Picked Randomly! ⏰ Draw Time: {draw_time}")
    st.dataframe(winner)

    # -------------------------------
    # 4️⃣ Save Winners for Download
    # -------------------------------
    output_winners = BytesIO()
    winner.to_excel(output_winners, index=False, engine='openpyxl')
    st.download_button(
        label="💾 Download Winners Excel",
        data=output_winners.getvalue(),
        file_name=f"EGSA_uqub_winners_{draw_time.replace(':','-')}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # -------------------------------
    # 5️⃣ Update Remaining Members
    # -------------------------------
    remaining = df[~df['Phone_no'].isin(winner['Phone_no'])]
    output_remaining = BytesIO()
    remaining.to_excel(output_remaining, index=False, engine='openpyxl')
    st.download_button(
        label="💾 Download Remaining Members Excel",
        data=output_remaining.getvalue(),
        file_name=f"EGSA_uqub_remaining_{draw_time.replace(':','-')}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    st.info("✅ Transparency: Full member list is visible above.")
