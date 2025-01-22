import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

load_dotenv()

api = os.getenv("GROQ_API_KEY")

# Initialize the agent
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile", api_key= api),
    tools=[DuckDuckGo()],
    markdown=True
)

# Streamlit interface
st.title("AI Generator")

# Input text box for user query     
user_input = st.text_input("Enter your prompt:")

# Button to generate the story
if st.button("ask"):
    if user_input:
        response = agent.run(user_input)
        st.write(response.content)
    else:
        st.write("Please enter a prompt.")