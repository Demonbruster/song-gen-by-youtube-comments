import os
from typing import Dict, List
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LyricsGenerator:
    def __init__(self):
        self.api_key = os.getenv('AZURE_OPENAI_KEY')
        self.endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
        self.model = os.getenv('AZURE_OPENAI_MODEL')
        self.version = os.getenv('AZURE_OPENAI_VERSION')
        self.temperature = os.getenv('AZURE_OPENAI_TEMPERATURE') or 0.7
        self.max_tokens = os.getenv('AZURE_OPENAI_MAX_TOKENS') or 1000
        
        if not self.api_key or not self.endpoint:
            raise ValueError("Azure OpenAI credentials not found in environment variables")
        
        # Initialize the Azure OpenAI client
        self.client = AzureOpenAI(
            api_key=self.api_key,
            api_version=self.version,
            azure_endpoint=self.endpoint
        )

    def _create_prompt(self, comments: List[Dict], sentiment_counts: Dict[str, int], dominant_sentiment: str) -> str:
        """Create a prompt for the lyrics generation based on comments and sentiment."""
        # Extract some example comments for context
        example_comments = [
            f"- {comment['text']} ({comment['sentiment']})"
            for comment in comments[:3]  # Use first 3 comments as examples
        ]
        
        prompt = f"""Based on the following YouTube comments and their sentiment analysis, write a song that captures the overall mood and themes.

Sentiment Analysis:
- Positive comments: {sentiment_counts['positive']}
- Neutral comments: {sentiment_counts['neutral']}
- Negative comments: {sentiment_counts['negative']}
- Mixed sentiment comments: {sentiment_counts['mixed']}
Dominant sentiment: {dominant_sentiment}

Example comments:
{chr(10).join(example_comments)}

Please write a song with:
1. A catchy chorus that reflects the dominant sentiment
2. At least two verses that incorporate themes from the comments
3. A poetic style that matches the overall mood
4. Clear separation between chorus and verses

Format the output with clear section headers (CHORUS, VERSE 1, VERSE 2, etc.)."""
        
        return prompt

    def generate_lyrics(self, comments: List[Dict], sentiment_counts: Dict[str, int], dominant_sentiment: str) -> str:
        """
        Generate song lyrics based on comments and sentiment analysis.
        
        Args:
            comments: List of analyzed comments
            sentiment_counts: Dictionary of sentiment counts
            dominant_sentiment: The dominant sentiment
            
        Returns:
            Generated song lyrics
        """
        prompt = self._create_prompt(comments, sentiment_counts, dominant_sentiment)
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,  # or your specific model deployment name
                messages=[
                    {"role": "system", "content": "You are a creative songwriter who can write engaging lyrics based on social media comments and sentiment analysis."},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            raise Exception(f"Error generating lyrics: {str(e)}") 