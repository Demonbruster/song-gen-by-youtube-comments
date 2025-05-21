from youtube_comments import YouTubeCommentsFetcher

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
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
