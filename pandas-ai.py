import os
import pandas as pd
import streamlit as st
from pandasai import Agent
from dotenv import load_dotenv

# load_dotenv()
user_data = pd.read_csv('final_data.csv')

agent = Agent(user_data)

st.title("PandasAI Query Interface")
st.markdown("Enter a question about the dataset, and the AI will respond!")

user_query = st.text_input("Enter your query here:")

if st.button("Get Answer"):
    if user_query.strip():
        try:
            st.write(os.environ.get('PANDASAI_API_KEY', 'Key not found!'))
            response = agent.chat(user_query)
            st.subheader("Response:")
            st.write(response)
            # Debugging output
            st.text(f"Raw Response: {response}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a valid query.")
