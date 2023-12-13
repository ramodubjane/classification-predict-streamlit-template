# Streamlit dependencies
import streamlit as st
import joblib
import os

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
    st.title("Team_JM_4")
    st.subheader("Climate Change ")

    st.info("Make predictions on climate change sentiment")

    # Creating a text box for user input
    tweet_text = st.text_area("Enter Text", "Type Here")

    if st.button("Classify"):
        # Transforming user input with vectorizer
        vect_text = tweet_cv.transform([tweet_text]).toarray()
        # Load your .pkl file with the model of your choice + make predictions
        # Try loading in multiple models to give the user a choice
        predictor = joblib.load(open(os.path.join("resources/LinearSVC_model.pkl"), "rb"))
        prediction = predictor.predict(vect_text)

        # When the model has successfully run, it will print the prediction
        # You can use a dictionary or a similar structure to make this output
        # more human interpretable.
        st.success("Text Categorized as: {}".format(prediction))

    st.info("General Information")
    # You can read a markdown file from the supporting resources folder
    st.markdown("Some information here")

    st.subheader("Raw Twitter data and label")
    if st.checkbox('Show raw data'):  # data is hidden if the box is unchecked
        st.write(raw[['sentiment', 'message']])  # will write the df to the page

    # Display a bar graph showing sentiment distribution in the raw data
    st.subheader("Sentiment Distribution")
    sentiment_counts = raw['sentiment'].value_counts()
    st.bar_chart(sentiment_counts)

# Required to let Streamlit instantiate our web app.
if __name__ == '__main__':
    main()
