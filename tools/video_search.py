# tools/video_search.py

import os
from serpapi.serp_api_client import SerpApiClient

class VideoSearchTool:
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_KEY")
        if not self.api_key:
            raise ValueError("SERPAPI_KEY not set")

    def search(self, query: str):
        """
        Search YouTube for a video using SerpApi.
        Returns a dictionary with 'title' and 'link' or None if not found.
        """
        params = {
            "engine": "youtube",
            "search_query": query,
            "api_key": self.api_key
        }

        try:
            client = SerpApiClient(params)
            results = client.get_dict()
        except Exception as e:
            print(f"Error fetching results from SerpApi: {e}")
            return None

        # DEBUG: show the full search results
        print("DEBUG: Full search results:", results)

        # Some responses may use different keys
        videos = results.get("video_results") or results.get("videos_results") or []

        if not videos:
            print("No video results found for this query.")
            return None

        # Return the first video found
        first_video = videos[0]
        title = first_video.get("title", "No title")
        link = first_video.get("link", "No link")

        print(f"DEBUG: First video found - Title: {title}, Link: {link}")

        return {
            "title": title,
            "link": link
        }
