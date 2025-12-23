import os
from serpapi.serp_api_client import SerpApiClient

class VideoSearchTool:
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_KEY")
        if not self.api_key:
            raise ValueError("SERPAPI_KEY not set")

    def search(self, query: str):
        params = {
            "engine": "youtube",
            "search_query": query,
            "api_key": self.api_key,
            "sp": "EgIQAQ%3D%3D" 
        }

        client = SerpApiClient(params)
        results = client.get_dict()

        videos = results.get("video_results", [])
        if not videos:
            return None

        return {
            "title": videos[0]["title"],
            "link": videos[0]["link"]
        }
