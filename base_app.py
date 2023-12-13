"""

    Simple Streamlit webserver application for serving developed classification
	models.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import joblib, os

# Data dependencies
import pandas as pd

# Vectorizer
news_vectorizer = open("resources/tfidfvect.pkl", "rb")
tweet_cv = joblib.load(news_vectorizer)  # loading your vectorizer from the pkl file

# Load your raw data
raw = pd.read_csv("resources/train.csv")

# The main function where we will build the actual app
def main():
    """Tweet Classifier App with Streamlit """

    # Creates a main title and subheader on your page -
    # these are static across all pages
    st.title("Happy Plastic PTY")
    st.subheader("Climate change tweet classification")

    # Creating text box for user input
    tweet_text = st.text_area("Enter Text", "Type Here")

    # Model selection
    model_option = st.selectbox("Choose a Model", ["Logistic Regression", "Linear SVM", "KNN"])

    if st.button("Classify"):
        # Transforming user input with vectorizer
        vect_text = tweet_cv.transform([tweet_text]).toarray()

        # Load the selected model based on user choice
        if model_option == "Logistic Regression":
            predictor = joblib.load(open(os.path.join("resources/Logistic_regression.pkl"), "rb"))
        elif model_option == "Linear SVM":
            predictor = joblib.load(open(os.path.join("resources/linear_svm_model.pkl"), "rb"))
        elif model_option == "KNN":
            predictor = joblib.load(open(os.path.join("resources/knn_model.pkl"), "rb"))

        prediction = predictor.predict(vect_text)

        # When the model has successfully run, will print prediction
        # You can use a dictionary or similar structure to make this output
        # more human interpretable.
        st.success("Text Categorized as: {}".format(prediction))

    # Displaying information on the home page
    st.info("General Information")
    # You can read a markdown file from supporting resources folder
    st.markdown("Some information here")

    st.subheader("Raw Twitter data and label")
    if st.checkbox('Show raw data'):  # data is hidden if the box is unchecked
        st.write(raw[['sentiment', 'message']])  # will write the df to the page

# Required to let Streamlit instantiate our web app.
if __name__ == '__main__':
    main()




