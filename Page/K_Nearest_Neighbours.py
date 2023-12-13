import streamlit as st
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report

# Sample data for demonstration
data = {
    'sentiment': [1, 1, 2, 1, 1],
    'message': [
        "PolySciMajor EPA chief doesn't think carbon di...",
        "It's not like we lack evidence of anthropogeni...",
        "RT @RawStory: Researchers say we have three ye...",
        "#TodayinMaker# WIRED : 2016 was a pivotal year...",
        "RT @SoyNovioDeTodas: It's 2016, and a racist, ..."
    ],
    'tweetid': [625221, 126103, 698562, 573736, 466954]
}

df = pd.DataFrame(data)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    df['message'], df['sentiment'], test_size=0.2, random_state=42
)

# Create a pipeline with CountVectorizer and KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=10)
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('knn', knn)
])

# Fit the model
pipeline.fit(X_train, y_train)

# Streamlit app
def main():
    st.title('KNN Classifier App')

    # Text input for user to enter a message
    user_input = st.text_input('Enter a message for sentiment analysis:')
    
    if user_input:
        # Make prediction
        prediction = pipeline.predict([user_input])[0]
        
        # Display the prediction
        st.write(f'Sentiment Prediction: {prediction}')

# Required to let Streamlit instantiate our web app.
if __name__ == '__main__':
    main()




