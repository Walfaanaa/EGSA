# -------------------------------
# 📦 Import Libraries
# -------------------------------
import streamlit as st
import pandas as pd
import os# -------------------------------
# 📦 Import Libraries
# -------------------------------
import streamlit as st
import pandas as pd
import os
from io import BytesIO
from datetime import datetime, timedelta

# -------------------------------
# 1️⃣ Page Setup
# -------------------------------
st.set_page_config(page_title="🏦 Loan Management System", layout="wide")
st.title("🏦 Loan Management System")

# -------------------------------
# 2️⃣ Storage Path
# -------------------------------
folder = r"C:\Users\User\Desktop\Request"
os.makedirs(folder, exist_ok=True)
file_path = os.path.join(folder, "loan_records.xlsx")

# Load existing data or create new
if os.path.exists(file_path):
    df = pd.read_excel(file_path)
else:
    df = pd.DataFrame(columns=[
        "Loan ID", "Full Name", "Mobile Number", "Address",
        "Loan Amount", "Duration (months)", "Interest Rate (%)",
        "Monthly Payment", "Total Payment", "Start Date", "End Date"
    ])

# -------------------------------
# 3️⃣ Interest Rate Determination
# -------------------------------
def determine_interest_rate(months):
    if months <= 3:
        return 20
    elif months <= 6:
        return 25
    elif months <= 9:
        return 30
    elif months <= 12:
        return 35
    elif months <= 36:
        return 40
    elif months <= 60:
        return 45
    else:
        return 45

# -------------------------------
# 4️⃣ Input Section (Live Calculation)
# -------------------------------
st.subheader("📋 Enter Loan Details")

col1, col2 = st.columns(2)
with col1:
    loan_id = st.text_input("Loan ID")
    full_name = st.text_input("Full Name")
    mobile = st.text_input("Mobile Number")
    address = st.text_area("Address", height=70)

with col2:
    loan_amount = st.number_input("Loan Amount", min_value=0.0, step=100.0)
    duration = st.number_input("Duration (months)", min_value=1, step=1)
    start_date = st.date_input("Start Date", datetime.today())

# Auto-calc End Date
if duration > 0:
    end_date = start_date + timedelta(days=duration * 30)
else:
    end_date = start_date

# Calculate interest + payments
interest_rate = determine_interest_rate(duration)
monthly_rate = interest_rate / 100 / 12

if loan_amount > 0 and duration > 0:
    monthly_payment = (
        loan_amount * monthly_rate * (1 + monthly_rate) ** duration
    ) / ((1 + monthly_rate) ** duration - 1)
    total_payment = monthly_payment * duration
else:
    monthly_payment, total_payment = 0.0, 0.0

st.write(f"💰 **Interest Rate:** {interest_rate}%")
st.write(f"📆 **Monthly Payment:** {monthly_payment:.2f}")
st.write(f"💵 **Total Payment:** {total_payment:.2f}")
st.write(f"📅 **Loan End Date:** {end_date}")

# -------------------------------
# 5️⃣ Save / Update Button
# -------------------------------
if st.button("💾 Save / Update Record"):
    if not loan_id:
        st.error("⚠️ Loan ID is required!")
    else:
        record = {
            "Loan ID": loan_id,
            "Full Name": full_name,
            "Mobile Number": mobile,
            "Address": address,
            "Loan Amount": loan_amount,
            "Duration (months)": duration,
            "Interest Rate (%)": interest_rate,
            "Monthly Payment": round(monthly_payment, 2),
            "Total Payment": round(total_payment, 2),
            "Start Date": start_date,
            "End Date": end_date
        }

        # Update or insert
        if not df.empty and loan_id in df["Loan ID"].values:
            df.loc[df["Loan ID"] == loan_id] = record
        else:
            df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)

        df.to_excel(file_path, index=False)
        st.success(f"✅ Record saved successfully to {file_path}!")

# -------------------------------
# 6️⃣ Show Table
# -------------------------------
st.subheader("📊 Loan Records")
st.dataframe(df, use_container_width=True)

# -------------------------------
# 7️⃣ Record Deletion
# -------------------------------
st.divider()
st.subheader("🗑️ Manage Records")

delete_id = st.text_input("Enter Loan ID to Delete")
if st.button("Delete Record"):
    if delete_id and delete_id in df["Loan ID"].values:
        df = df[df["Loan ID"] != delete_id]
        df.to_excel(file_path, index=False)
        st.success(f"🗑️ Record with Loan ID '{delete_id}' deleted.")
    else:
        st.error("⚠️ Loan ID not found!")

# -------------------------------
# 8️⃣ 🔄 Refresh / Clear All Data
# -------------------------------
if st.button("🔄 Refresh / Clear ALL Records"):
    df = pd.DataFrame(columns=df.columns)
    df.to_excel(file_path, index=False)
    st.success("🧹 All loan data cleared successfully!")

# -------------------------------
# 9️⃣ Export Option
# -------------------------------
buffer = BytesIO()
df.to_excel(buffer, index=False)
buffer.seek(0)

st.download_button(
    label="⬇️ Download Records as Excel",
    data=buffer,
    file_name="loan_records.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

from io import BytesIO

# -------------------------------
# 1️⃣ Page Setup
# -------------------------------
st.set_page_config(page_title="🏦 Loan Management System", layout="wide")
st.title("🏦 Loan Management System")

# -------------------------------
# 2️⃣ Storage Path
# -------------------------------
folder = r"C:\Users\User\Desktop\Request"
os.makedirs(folder, exist_ok=True)
file_path = os.path.join(folder, "loan_records.xlsx")

# Load existing data
if os.path.exists(file_path):
    df = pd.read_excel(file_path)
else:
    df = pd.DataFrame(columns=[
        "Loan ID", "Full Name", "Mobile Number", "Address",
        "Loan Amount", "Duration (months)", "Interest Rate (%)",
        "Monthly Payment", "Total Payment"
    ])

# -------------------------------
# 3️⃣ Interest Rate Determination
# -------------------------------
def determine_interest_rate(months):
    if months <= 3:
        return 20
    elif months <= 6:
        return 25
    elif months <= 9:
        return 30
    elif months <= 12:
        return 35
    elif months <= 36:
        return 40
    elif months <= 60:
        return 45
    else:
        return 45

# -------------------------------
# 4️⃣ Input Section (Live Calculation)
# -------------------------------
st.subheader("📋 Enter Loan Details")

col1, col2 = st.columns(2)
with col1:
    loan_id = st.text_input("Loan ID")
    full_name = st.text_input("Full Name")
    mobile = st.text_input("Mobile Number")
    address = st.text_area("Address", height=70)
with col2:
    loan_amount = st.number_input("Loan Amount", min_value=0.0, step=100.0)
    duration = st.number_input("Duration (months)", min_value=1, step=1)
    
# Calculate interest and payments dynamically
interest_rate = determine_interest_rate(duration)
monthly_rate = interest_rate / 100 / 12
if loan_amount > 0 and duration > 0:
    monthly_payment = (
        loan_amount * monthly_rate * (1 + monthly_rate) ** duration
    ) / ((1 + monthly_rate) ** duration - 1)
    total_payment = monthly_payment * duration
else:
    monthly_payment, total_payment = 0.0, 0.0

st.write(f"💰 **Interest Rate:** {interest_rate}%")
st.write(f"📆 **Monthly Payment:** {monthly_payment:.2f}")
st.write(f"💵 **Total Payment:** {total_payment:.2f}")

# -------------------------------
# 5️⃣ Save / Update Button
# -------------------------------
if st.button("💾 Save / Update Record"):
    if not loan_id:
        st.error("⚠️ Loan ID is required!")
    else:
        record = {
            "Loan ID": loan_id,
            "Full Name": full_name,
            "Mobile Number": mobile,
            "Address": address,
            "Loan Amount": loan_amount,
            "Duration (months)": duration,
            "Interest Rate (%)": interest_rate,
            "Monthly Payment": round(monthly_payment, 2),
            "Total Payment": round(total_payment, 2)
        }

        # Update existing record or append new
        if not df.empty and loan_id in df["Loan ID"].values:
            df.loc[df["Loan ID"] == loan_id] = record
        else:
            df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)

        df.to_excel(file_path, index=False)
        st.success(f"✅ Record saved successfully to {file_path}!")

# -------------------------------
# 6️⃣ Show Table
# -------------------------------
st.subheader("📊 Loan Records")
st.dataframe(df, use_container_width=True)

# -------------------------------
# 7️⃣ Record Deletion
# -------------------------------
st.divider()
st.subheader("🗑️ Manage Records")

delete_id = st.text_input("Enter Loan ID to Delete")
if st.button("Delete Record"):
    if delete_id and delete_id in df["Loan ID"].values:
        df = df[df["Loan ID"] != delete_id]
        df.to_excel(file_path, index=False)
        st.success(f"🗑️ Record with Loan ID '{delete_id}' deleted.")
    else:
        st.error("⚠️ Loan ID not found!")

# -------------------------------
# 8️⃣ Export Option
# -------------------------------
buffer = BytesIO()
df.to_excel(buffer, index=False)
buffer.seek(0)

st.download_button(
    label="⬇️ Download Records as Excel",
    data=buffer,
    file_name="loan_records.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)


