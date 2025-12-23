import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv
from agent import AIAgent

# Load .env reliably
load_dotenv(find_dotenv())

st.set_page_config(page_title="AI Video Transcription Agent")
st.title("AI Video Search & Transcription Agent")
st.write("Enter a YouTube video topic/title. The agent will search and transcribe it using Gemini.")

query = st.text_input("Video topic or title")

if st.button("Search & Transcribe"):
    if not query.strip():
        st.warning("Please enter a video title.")
    else:
        with st.spinner("Searching and transcribing..."):
            try:
                agent = AIAgent()
                refined_query = query.strip() + " explained"
                title, transcript = agent.run(refined_query)

                # DEBUG
                #st.write("SERPAPI_KEY loaded:", os.getenv("SERPAPI_KEY"))
                #st.write("GEMINI_API_KEY loaded:", os.getenv("GEMINI_API_KEY"))
                #st.write("DEBUG: Video title:", title)
                #st.write("DEBUG: Transcript length:", len(transcript) if transcript else 0)

            except Exception as e:
                st.error(f"An error occurred: {e}")
                title, transcript = "No video found", ""

        if title == "No video found":
            st.warning("No video found for this query. Try a more specific query.")
        else:
            st.subheader("Video Title")
            st.write(title)
            st.subheader("Transcription")
            st.text_area("Transcript", transcript, height=400)
