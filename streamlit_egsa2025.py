# streamlit_egsa2025_ad.py
# EGSA2025 PLC - Streamlit Advertisement / Information Page

import streamlit as st

# -------------------------------
# Page Setup
# -------------------------------
st.set_page_config(page_title="EGSA2025 PLC", layout="wide")
st.title("🌟 Welcome to EGSA2025 PLC")
st.subheader("Empowering the New Generation of Investors")

# -------------------------------
# Hero Image / Banner (Using EGSA Logo)
# -------------------------------
st.markdown(
    """
    <div style="text-align:center;">
        <img src="https://github.com/Walfaanaa/EGSA/blob/main/EGSA%20Logo.png?raw=true" width="600">
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# About EGSA2025
# -------------------------------
st.header("About EGSA2025")
st.markdown("""
EGSA2025 PLC is a modern member-based platform that brings together individuals to **grow together, access loans, and benefit from shared opportunities**.  

**Our Mission:**  
- Provide accessible and fair opportunities for our members.  
- Foster a strong, engaged financial community.  
- Build sustainable growth and value for everyone involved.  

**Our Vision:**  
To be the leading platform for financial empowerment among the new generation.
""")

# -------------------------------
# Member Benefits
# -------------------------------
st.header("Why Join EGSA2025?")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://via.placeholder.com/100.png?text=Membership", width=100)
    st.subheader("Exclusive Membership")
    st.write("Join a growing community of active and engaged members.")

with col2:
    st.image("https://via.placeholder.com/100.png?text=Loan", width=100)
    st.subheader("Access to Loans")
    st.write("Members can access fair and flexible loans from our pooled resources.")

with col3:
    st.image("https://via.placeholder.com/100.png?text=Growth", width=100)
    st.subheader("Shared Benefits")
    st.write("Enjoy bonuses and opportunities as the company grows.")

# -------------------------------
# How EGSA Works
# -------------------------------
st.header("How EGSA2025 Works")
st.markdown("""
1. Members contribute regularly to the community pool.  
2. Members can request loans based on their participation.  
3. EGSA generates growth opportunities and shares benefits with its members.  
4. Occasional additional contributions help the community grow even faster.  
""")

# -------------------------------
# Testimonials
# -------------------------------
st.header("What Our Members Say")
st.markdown("""
> "Joining EGSA2025 has allowed me to access loans quickly and grow my savings!" – *Member A*  
> "I love being part of a community that truly benefits everyone." – *Member B*  
> "Transparent, fair, and empowering. EGSA2025 is the future!" – *Member C*
""")

# -------------------------------
# Call to Action
# -------------------------------
st.header("Become a Member Today!")
st.markdown("""
📞 **Phone:** +251912861288  
📧 **Email:** walfanamegersa3@gmail.com  

Reach out to get more information and join our growing community!
""")

if st.button("📩 Contact Us / Join Now"):
    st.success("Thank you for your interest! Please contact us via phone or email to join EGSA2025.")
