import streamlit as st
import pandas as pd
import numpy as np
import joblib
import altair as alt
import requests
from langchain_community.llms import Ollama

# Initialize the Ollama model
llm = Ollama(model="llama3")

# Load your logistic regression model
pipe_lr = joblib.load(open(r'C:\Projects\Mypal\logisticmentalhealthmodel.pkl', 'rb'))

# Function for mental health prediction
def predict_mhealth(docs):
    results = pipe_lr.predict([docs])
    return results[0]

def get_predictions_proba(docs):
    results = pipe_lr.predict_proba([docs])
    return results

# Function to get YouTube video
def get_youtube_video(query):
    api_key = 'AIzaSyA5YCpek9tIfcNbZSCaMt4WMX75d3laP6E'
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={query}&key={api_key}'
    response = requests.get(url)
    video_id = response.json()['items'][0]['id']['videoId']
    return f'https://www.youtube.com/watch?v={video_id}'

# Function for generating a chatbot response with suggestions
def generate_response(prompt, prediction, confidence):
    if prediction == 'positive' and confidence > 0.7:
        response = llm.invoke(prompt + " It seems like you're doing well! How about trying some mindfulness exercises or going for a walk in nature?")
    elif prediction == 'negative' and confidence > 0.7:
        response = llm.invoke(prompt + " I'm here for you. Consider practicing deep breathing exercises or journaling about your feelings.")
    else:
        response = llm.invoke(prompt + " How am I feeling today? Remember to take some time for self-care and reach out to a trusted friend or professional if needed.")

    youtube_link = get_youtube_video('guided meditation for ' + prediction)
    response += f" Here is a [guided meditation video]({youtube_link}) that might help."
    return response

def main():
    st.set_page_config(page_title="MyPal", layout="wide", initial_sidebar_state="expanded")
    st.title("MyPal")
    menu = ['Home', 'About']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.subheader('My Pal: Home - Mental Health Prediction and Chatbot')

        with st.form(key='Mental_clf'):
            raw_text = st.text_area('Type text')
            submit_text = st.form_submit_button(label='Submit')
            clear_text = st.form_submit_button(label='Clear')

        if submit_text:
            prediction = predict_mhealth(raw_text)
            probability = get_predictions_proba(raw_text)
            confidence = np.max(probability)

            # Generate a response with suggestions
            response = generate_response(f"I detected {prediction} with a confidence of {confidence:.2f}. Can you provide advice or meditation suggestions?", prediction, confidence)

            col1, col2 = st.columns(2)

            with col1:
                st.success('Original Text')
                st.write(raw_text)

                st.success("Prediction")
                st.write(prediction)
                st.write('Confidence: {}'.format(np.max(probability)))

                st.success('My Pal suggestion: ')
                st.markdown(response, unsafe_allow_html=True)

            with col2:
                st.success('Prediction Probability')
                proba_df = pd.DataFrame(probability, columns=pipe_lr.classes_)
                proba_df_clean = proba_df.T.reset_index()
                proba_df_clean.columns = ['Mental_Health', 'Probability']
                fig = alt.Chart(proba_df_clean).mark_bar().encode(x='Mental_Health', y='Probability', color='Mental_Health').properties(height=400)
                st.altair_chart(fig, use_container_width=True)

        if clear_text:
            st.empty()

    else:
        st.subheader('About')

if __name__ == '__main__':
    main()
