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
EGSA2025 PLC is a modern member-based platform that brings together individuals to 
**grow together, access loans, and benefit from shared opportunities**.  

**Our Mission:**  
- Provide accessible and fair opportunities for our members.  
- Foster a strong, engaged financial community.  
- Build sustainable growth and value for everyone involved.  

**Our Vision:**  
To be the leading platform for financial empowerment among the new generation.
""")

# -------------------------------
# EGSA Financial Strategy & Investment Principle
# -------------------------------
st.header("📘 EGSA Financial Strategy & Investment Principle")
st.markdown("""
The principle guiding financially successful institutions is the use of structured systems 
rather than emotional or spontaneous decision-making. In alignment with this philosophy,  
EGSA has adopted a system-driven approach as the foundation for its present and future operations.  
Building a strong internal financial system is therefore considered the most effective strategy 
for ensuring long-term organizational growth and stability.

A central component of this system is the investment-focused financial principle. Sustainable 
wealth is generated not merely through saving but through **strategic investment**. Savings 
provide security, whereas investments drive expansion and long-term value creation.

Following this ideology, EGSA implements a disciplined financial allocation structure:

- **80% of funds allocated to investment**, ensuring that the majority of resources 
  generate continuous growth and future income.  
- **20% reserved for savings and emergency needs**, protecting the organization from 
  unexpected financial challenges.  
- **0% allocated to waste or non-productive expenses**, ensuring complete efficiency 
  and accountability.

Through consistent application of this system, EGSA positions itself as a forward-looking, 
investment-oriented organization committed to strengthening its financial capacity, 
expanding wealth, and securing sustainable benefits for all members.
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
# Incentive Program
# -------------------------------
st.header("🌟 Incentive Program for Member Recruitment")
st.markdown("""
EGSA encourages active engagement and growth among its members. To promote meaningful participation, 
any member who successfully recruits more than one new member shall be eligible for the following benefits:

**1. Preferential Loan Terms:**  
Access loans at reduced interest rates.

**2. Performance-Based Rewards:**  
Receive an annual reward for contributing to organizational growth.

**3. Official Recognition:**  
Receive a certificate of recognition for expanding the membership base.

This initiative fosters a culture of participation, contribution, and appreciation.
""")

# -------------------------------
# How EGSA Works
# -------------------------------
st.header("How EGSA2025 Works")
st.markdown("""
1. Members contribute regularly to the community pool.  
2. Members may request loans based on their participation and contributions.  
3. EGSA generates growth opportunities and shares benefits with its members.  
4. Occasional additional contributions help accelerate community growth.  
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
