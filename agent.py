from tools.video_search import VideoSearchTool
from tools.gemini_transcription import GeminiTranscriptionTool

class AIAgent:
    def __init__(self):
        self.video_search_tool = VideoSearchTool()
        self.transcription_tool = GeminiTranscriptionTool()

    def run(self, query: str):
        print("Searching YouTube...")
        video = self.video_search_tool.search(query)

        if not video:
            return "No video found", "No transcript available"

        title = video["title"]
        url = video["link"]

        print("Video found:", title)
        print("Processing with Gemini...")

        transcript = self.transcription_tool.transcribe(url)

        return title, transcript
