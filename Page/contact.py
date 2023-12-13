import streamlit as st

def contact_page():
    st.title("Happy Plastic Pty")

    st.write("Welcome to our contact page! We look forward to hearing from you with suggestions, ideas to improve our work, or any questions you may have. We can't wait to connect!")

    # Add form fields
    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    message = st.text_area("Your Message:")

    if st.button("Submit"):
        # You can customize this part to handle the form submission (e.g., send an email, store in a database, etc.)
        st.success(f"Thank you, {name}! Your message has been submitted.")

    st.header("Contact the Team")
    st.subheader("Team Leader and Project Manager")
    team_leader_project_manager = {
        "Dimakatso Selolo (Team Leader)": "paledi2nd@gmail.com",
        "Percy Makhakaba (Project Manager)": "percykgmakakaba@gmail.com"
    }

    for name, member_email in team_leader_project_manager.items():
        st.write(f"[{name}](mailto:{member_email})")

    st.subheader("Team Members")
    team_members = {
        "Asiphe Nkomo": "asiphenkomo91@gmail.com",
        "Choene Dikeledi": "cdcseema@gmail.com",
        "Lauryn Mamabolo": "mamabololesego94@gmail.com",
        "Ramodubjane Sete": "ramodubjanesete@gmail.com"
    }

    for name, member_email in team_members.items():
        st.write(f"[{name}](mailto:{member_email})")

    st.header("Company Contact Details")
    st.write("Email: info@happyplasticpty.com")
    st.write("Phone: +123 456 7890")

    st.header("Company Address")
    st.write("Happy Plastic Pty")
    st.write("123 Plastic Avenue")
    st.write("Cityville, PL 54321")
    st.write("South Africa")
    
if __name__ == "__main__":
    st.set_page_config(
        page_title="Happy Plastic Pty - Contact App",
        page_icon="✉️",
        layout="wide"
    )

    # Navigation sidebar
    page = st.sidebar.radio("Navigation", ["Home", "Contact"])

    if page == "Home":
        st.title("Welcome To Happy Plastic Team Contact Page ")
        st.write("Select 'Contact' in the sidebar to reach out to us.")
    elif page == "Contact":
        contact_page()



