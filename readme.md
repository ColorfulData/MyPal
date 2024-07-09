# MyPal: Mental Health Diagnosis and Support Application

## Overview
![MyPal](image-2.png)

MyPal is a Streamlit-based application designed to assist users in understanding their mental health conditions through natural language processing (NLP) and logistic linear regression models. The application provides personalized suggestions, meditation techniques, and additional resources to support users based on their symptoms.

## Features

- **Mental Health Prediction**: Uses a logistic linear regression model to predict mental health conditions based on user input.
- **Chatbot Integration**: Provides personalized advice, meditation suggestions, and additional resources through a chatbot interface.
- **Visualization**: Displays prediction probabilities using Altair charts.
- **YouTube Integration**: Suggests guided meditation videos using the YouTube API.

## Application Structure

### Home Page

The home page allows users to input their text describing their symptoms. The application then predicts the mental health condition and provides personalized suggestions.

#### Input Form
- **Text Area**: Users can type their symptoms or feelings.
- **Submit Button**: Submits the text for prediction.
- **Clear Button**: Clears the input text.

#### Output
- **Original Text**: Displays the user's input.
- **Prediction**: Shows the predicted mental health condition and confidence level.
- **Suggestions**: Provides personalized advice and meditation suggestions.
- **Prediction Probability**: Visualizes the prediction probabilities for different mental health conditions.

### About Page

Provides information about the application and its purpose.

## Key Components

### NLP Model

- **Model**: Logistic linear regression model trained to predict mental health conditions.
- **Libraries**: Utilizes `joblib` for model loading and `numpy` for numerical operations.

### Chatbot

- **LLM**: Uses the Ollama model for generating personalized responses.
- **Integration**: Combines prediction results with the chatbot to provide tailored suggestions.

### YouTube API

- **Function**: Fetches guided meditation videos based on the predicted mental health condition.
- **API Key**: Utilizes a YouTube API key to access video data.

## Meditation Techniques

The application suggests various meditation techniques based on individual needs:

1. **Mindfulness Meditation**: Focus on the present moment without judgment.
2. **Loving-kindness Meditation**: Send kind thoughts to oneself and others.
3. **Grounding Techniques**: Use senses to stay grounded in the present moment.

## Additional Resources

The application provides links to trusted organizations and resources for further support:

1. **National Alliance on Mental Illness (NAMI)**
2. **Mental Health America**
3. **Healthcare Providers**

## Usage

To use the MyPal application:

1. **Install Dependencies**: Ensure all required libraries are installed (`streamlit`, `pandas`, `numpy`, `joblib`, `altair`, `requests`).
2. **Run the Application**: Execute the Streamlit application using `streamlit run app.py`.
3. **Input Symptoms**: Enter your symptoms or feelings in the text area and submit.
4. **View Results**: Review the predicted mental health condition, confidence level, and personalized suggestions.
5. **Explore Resources**: Utilize the additional resources and YouTube meditation suggestions for further support.



## Images

### MyPal Prediction Result

![MyPal Prediction Result](<MyPal Prediction Result.jpg>)

### Mindfulness Tips

![Mindfulness Tips](<Mindfulness Tips.jpg>)


### YouTube Video Suggestion

![YouTube Video Suggestion](<Youtube Video Suggestion-1.jpg>)



## Conclusion

MyPal is a comprehensive tool designed to support mental health through prediction, personalized suggestions, and access to valuable resources. By integrating NLP, chatbot technology, and meditation techniques, MyPal aims to provide a holistic approach to mental well-being.

