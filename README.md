# AI Agent with Video Search and Transcription

## Overview
This project implements an AI agent capable of:
- Searching YouTube videos using SerpAPI
- Extracting transcription-style summaries using Gemini multimodal API
- Saving results in a local knowledge base

## Tech Stack
- Python
- SerpAPI
- Gemini API
- Streamlit

## Workflow
1. User enters a video topic
2. Agent searches YouTube
3. Gemini processes the video
4. Transcript is saved locally

## How to Run
pip install -r requirements.txt
streamlit run streamlit_app.py
