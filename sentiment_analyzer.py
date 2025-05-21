import os
from typing import Dict, List, Tuple
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SentimentAnalyzer:
    def __init__(self):
        self.endpoint = os.getenv('TEXT_ANALYTICS_ENDPOINT')
        self.key = os.getenv('TEXT_ANALYTICS_KEY')
        
        if not self.endpoint or not self.key:
            raise ValueError("Azure Text Analytics credentials not found in environment variables")
        
        # Initialize the Text Analytics client
        self.client = TextAnalyticsClient(
            endpoint=self.endpoint,
            credential=AzureKeyCredential(self.key)
        )

    def analyze_comments(self, comments: List[Dict]) -> Tuple[Dict[str, int], List[Dict]]:
        """
        Analyze the sentiment of YouTube comments.
        
        Args:
            comments: List of comment dictionaries from YouTube API
            
        Returns:
            Tuple containing:
            - Dictionary with sentiment counts (positive, neutral, negative, mixed)
            - List of comments with their sentiment analysis results
        """
        # Extract comment texts
        comment_texts = [
            item['snippet']['topLevelComment']['snippet']['textDisplay']
            for item in comments
        ]
        
        # Initialize sentiment counts
        sentiment_counts = {
            'positive': 0,
            'neutral': 0,
            'negative': 0,
            'mixed': 0
        }
        
        # Process comments in batches of 10
        analyzed_comments = []
        batch_size = 10
        
        for i in range(0, len(comment_texts), batch_size):
            batch_texts = comment_texts[i:i + batch_size]
            batch_comments = comments[i:i + batch_size]
            
            try:
                # Analyze sentiment for the current batch
                results = self.client.analyze_sentiment(batch_texts)
                
                # Process results and combine with original comments
                for comment, result in zip(batch_comments, results):
                    sentiment = result.sentiment.lower()
                    sentiment_counts[sentiment] += 1
                    
                    analyzed_comment = {
                        'text': comment['snippet']['topLevelComment']['snippet']['textDisplay'],
                        'author': comment['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                        'sentiment': sentiment,
                        'confidence_scores': {
                            'positive': result.confidence_scores.positive,
                            'neutral': result.confidence_scores.neutral,
                            'negative': result.confidence_scores.negative
                        }
                    }
                    analyzed_comments.append(analyzed_comment)
            except Exception as e:
                print(f"Error processing batch {i//batch_size + 1}: {str(e)}")
                continue
        
        return sentiment_counts, analyzed_comments

    def get_dominant_sentiment(self, sentiment_counts: Dict[str, int]) -> str:
        """Get the dominant sentiment from the sentiment counts."""
        # Remove 'mixed' from consideration for dominant sentiment
        counts_without_mixed = {k: v for k, v in sentiment_counts.items() if k != 'mixed'}
        return max(counts_without_mixed.items(), key=lambda x: x[1])[0] 