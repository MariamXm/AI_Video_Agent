import os
from google import genai
from google.genai import types

class GeminiTranscriptionTool:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not set")

        self.client = genai.Client(api_key=api_key)

    def transcribe(self, video_url: str) -> str:
        response = self.client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=types.Content(
                parts=[
                    types.Part(
                        file_data=types.FileData(file_uri=video_url)
                    ),
                    types.Part(
                        text=    "Listen to the spoken content of this video and write down the spoken explanation in clear text form. "
                                    "Do not summarize unless necessary."
                    )
                ]
            )
        )

        return response.text.strip()
