from youtube_comments import YouTubeCommentsFetcher
from sentiment_analyzer import SentimentAnalyzer

def main():
    try:
        # Initialize the fetchers
        fetcher = YouTubeCommentsFetcher()
        sentiment_analyzer = SentimentAnalyzer()
        
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
            
        # Analyze sentiment
        print("\nAnalyzing sentiment...")
        sentiment_counts, analyzed_comments = sentiment_analyzer.analyze_comments(comments)
        dominant_sentiment = sentiment_analyzer.get_dominant_sentiment(sentiment_counts)
        
        # Display results
        print("\nSentiment Analysis Results:")
        print(f"Positive comments: {sentiment_counts['positive']}")
        print(f"Neutral comments: {sentiment_counts['neutral']}")
        print(f"Negative comments: {sentiment_counts['negative']}")
        print(f"Mixed sentiment comments: {sentiment_counts['mixed']}")
        print(f"\nDominant sentiment: {dominant_sentiment.upper()}")
        
        print("\nComments with Sentiment:")
        for comment in analyzed_comments:
            print(f"\nComment by {comment['author']} ({comment['sentiment'].upper()}):")
            print(comment['text'])
            print(f"Confidence scores: {comment['confidence_scores']}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
