# Streamlit dependencies
import streamlit as st
import joblib
import os

# Data dependencies
import pandas as pd

# Load your raw data at the module level
raw = pd.read_csv("resources/train.csv")

# Load the KNN model at the module level
Knb = joblib.load(open(os.path.join("resources/KNN_model.pkl"), "rb"))

# Initialize tweet_text with a default value
tweet_text = "Type Here"

# The main function where we will build the actual app
def main():
    """Tweet Classifier App with Streamlit """

    # ... (same as your existing code)

    if st.button("Classify"):
        # Transforming user input with vectorizer
        vect_text = tweet_cv.transform([tweet_text]).toarray()
        # Make predictions using the loaded KNN model
        prediction = Knb.predict(vect_text)

        # When the model has successfully run, it will print the prediction
        st.success("Text Categorized as: {}".format(prediction[0]))

    # ... (same as your existing code)

# Required to let Streamlit instantiate our web app.
if __name__ == '__main__':
    main()







