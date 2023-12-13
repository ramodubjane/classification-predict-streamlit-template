import streamlit as st

def faq_page():
    st.title("Happy Plastic Pty - Frequently Asked Questions (FAQ)")

    st.header("General Questions")

    st.subheader("Q: What is the Happy Plastic Pty app?")
    st.write("A: The Happy Plastic Pty app is designed to [describe the main purpose or features of the app].")

    st.subheader("Q: How can I download the app?")
    st.write("A: You can download the Happy Plastic Pty app from [App Store/Google Play/other platforms].")

    st.subheader("Q: Is the app free to use?")
    st.write("A: Yes, the Happy Plastic Pty app is free to download and use.")

    st.header("Account and Security")

    st.subheader("Q: How do I create an account?")
    st.write("A: To create an account, [provide instructions on the account creation process].")

    st.subheader("Q: How can I reset my password?")
    st.write("A: You can reset your password by [explain the password reset process].")

    st.header("Technical Support")

    st.subheader("Q: I'm experiencing technical issues with the app. What should I do?")
    st.write("A: If you're facing technical issues, please [provide guidance on troubleshooting or contacting support].")

    st.header("Submit a Question")

    st.write("If you have a question that is not addressed in the FAQ, feel free to submit it using the form below.")

    new_question = st.text_area("Your Question:")
    submit_button = st.button("Submit Question")

    if submit_button:
        # You can customize this part to handle the submission of new questions (e.g., store in a database, send an email, etc.)
        st.success(f"Thank you for your question! We will get back to you as soon as possible.")

if __name__ == "__main__":
    st.set_page_config(
        page_title="Happy Plastic Pty - FAQ",
        page_icon="❓",
        layout="wide"
    )

    # Display the FAQ page
    faq_page()
