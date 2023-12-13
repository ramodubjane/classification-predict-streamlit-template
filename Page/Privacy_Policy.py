import streamlit as st

def privacy_policy_page():
    st.title("Happy Plastic Pty - Privacy Policy")

    st.write("At Happy Plastic Pty, we are committed to protecting your privacy and ensuring the security of your personal information. This Privacy Policy outlines how we collect, use, disclose, and safeguard your information. By using our services, you agree to the terms of this policy.")

    st.header("1. Collection of Personal Information")
    st.write("We may collect personal information from you when you interact with our website, products, or services. This information may include, but is not limited to, your name, email address, phone number, and other details relevant to the services we provide.")

    st.header("2. Use of Personal Information")
    st.write("We use the collected information to provide and improve our products and services. Your personal information may be used for communication, marketing, and other business-related purposes. We respect your privacy and will not sell or share your information with third parties without your consent.")

    st.header("3. Protection of Personal Information (POPI Act)")
    st.write("Happy Plastic Pty complies with the Protection of Personal Information Act (POPIA) in South Africa. This legislation governs the processing of personal information and sets guidelines for responsible and secure data handling. We are committed to ensuring the confidentiality, integrity, and availability of your personal information.")

    st.header("4. Security Measures")
    st.write("We implement reasonable security measures to protect your personal information from unauthorized access, disclosure, alteration, and destruction. Our employees are trained on data protection practices, and we regularly review and update our security protocols.")

    st.header("5. Your Rights")
    st.write("As a user, you have the right to access, correct, or delete your personal information. You may also request information about how your data is being used. To exercise these rights, please contact us through the provided contact details below.")

    st.header("6. Contact Information")
    st.write("If you have any questions, concerns, or requests regarding our privacy policy or the handling of your personal information, please contact us at:")

    st.subheader("Happy Plastic Pty")
    st.write("Email: privacy@happyplasticpty.com")
    st.write("Phone: +123 456 7890")
    st.write("Address: 123 Plastic Avenue, Cityville, PL 54321, Country")

if __name__ == "__main__":
    st.set_page_config(
        page_title="Happy Plastic Pty - Privacy Policy",
        page_icon="🔐",
        layout="wide"
    )

    # Display the privacy policy page
    privacy_policy_page()
