import os
import requests
from dotenv import load_dotenv
from typing import Dict, List, Optional

# Load environment variables
load_dotenv()

class YouTubeCommentsFetcher:
    def __init__(self):
        self.api_key = os.getenv('YOUTUBE_API_KEY')
        if not self.api_key:
            raise ValueError("YouTube API key not found in environment variables")
        
        self.base_url = "https://www.googleapis.com/youtube/v3"

    def get_video_details(self, video_id: str) -> Dict:
        """Fetch video details including title and statistics."""
        url = f"{self.base_url}/videos"
        params = {
            'part': 'snippet,statistics,contentDetails',
            'id': video_id,
            'key': self.api_key
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_comments(self, video_id: str, max_results: int = 100, order: str = 'relevance') -> List[Dict]:
        """
        Fetch comments for a video.
        
        Args:
            video_id: The YouTube video ID
            max_results: Maximum number of comments to fetch (default: 100)
            order: Comment ordering ('relevance', 'time', 'rating') (default: 'relevance')
            
        Returns:
            List of comment dictionaries
        """
        url = f"{self.base_url}/commentThreads"
        params = {
            'part': 'snippet',
            'videoId': video_id,
            'maxResults': max_results,
            'order': order,  # 'relevance' for popular/top comments
            'key': self.api_key
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get('items', [])

def main():
    try:
        # Initialize the fetcher
        fetcher = YouTubeCommentsFetcher()
        
        # Get video ID from user input
        video_id = input("Enter YouTube video ID: ")
        
        # Get video details
        video_data = fetcher.get_video_details(video_id)
        if not video_data.get('items'):
            print("Video not found!")
            return
            
        video_info = video_data['items'][0]
        print("\nVideo Details:")
        print(f"Title: {video_info['snippet']['title']}")
        print(f"Views: {video_info['statistics']['viewCount']}")
        
        # Get comments
        print("\nFetching comments...")
        comments = fetcher.get_comments(video_id)
        
        if not comments:
            print("No comments found or comments are disabled for this video.")
            return
            
        print("\nComments:")
        for item in comments:
            comment = item['snippet']['topLevelComment']['snippet']
            print(f"\nComment by {comment['authorDisplayName']}:")
            print(comment['textDisplay'])
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 