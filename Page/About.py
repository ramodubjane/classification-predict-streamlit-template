import streamlit as st
import os

def about_page():
    st.title("About Happy Plastic Pty App 🌍")

    # Dynamic loading of the logo using an absolute path
    script_directory = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(script_directory, "logo.png")
    
    st.image(logo_path, caption="Happy Plastic Pty Logo", use_column_width=True)

    st.write(
        "Happy Plastics Pty – a plastic bag manufacturing company – has recruited our team of experts to analyze Twitter data "
        "with the goal of understanding how people perceive climate change. Many companies, including Happy Plastics Pty, are "
        "dedicated to lessening environmental impact and offering environmentally friendly products. They want to gauge public "
        "sentiment on climate change to inform their market research efforts and understand how their products may be received."
    )

    st.header("Project Objectives:")
    st.write(
        "The primary objective of this project is to determine how people perceive climate change and whether they believe it "
        "poses a real threat. Achieving an accurate and robust solution to this task provides companies with access to a broad "
        "base of consumer sentiment, spanning multiple demographic and geographic categories. This, in turn, enhances insights and "
        "informs future marketing strategies."
    )

    st.header("Why Twitter Data?")
    st.write(
        "Twitter serves as a rich source of real-time data, reflecting a diverse range of opinions and sentiments. Analyzing Twitter "
        "data allows us to capture a snapshot of public discourse on climate change, providing valuable insights for our analysis."
    )

    st.header("Collaboration with Happy Plastics Pty:")
    st.write(
        "Happy Plastics Pty, being environmentally conscious, recognizes the importance of understanding public attitudes towards climate "
        "change. By collaborating with our team of experts, they aim to leverage data-driven insights to enhance their environmental "
        "initiatives and product/service offerings."
    )

    st.header("Machine Learning Classification Sprint:")
    st.write(
        "To achieve our objectives, we are embarking on a Classification Sprint. The task involves creating a Machine Learning model "
        "capable of classifying whether a person believes in climate change based on their Twitter data. This model will contribute "
        "to a comprehensive analysis of public sentiment, enabling informed decision-making for companies like Happy Plastics Pty."
    )

if __name__ == "__main__":
    st.set_page_config(
        page_title="Happy Plastic Pty - About",
        page_icon="🌍",
        layout="wide"
    )

    # Display the About page
    about_page()


