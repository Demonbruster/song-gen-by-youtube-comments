# YouTube Comment Song Generator 🎵

Transform YouTube video comments into an original song! This project analyzes comments from any YouTube video, determines the overall sentiment, and generates both lyrics and audio based on the comment content.

## ✨ Features

- **YouTube Comment Analysis**: Fetches and processes comments from any public YouTube video
- **Sentiment Analysis**: Analyzes the emotional tone of comments (positive, negative, neutral, mixed)
- **AI-Powered Lyrics Generation**: Creates original song lyrics based on comment content and sentiment
- **Audio Generation**: Converts the generated lyrics into an actual song with music

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A YouTube API key (for fetching comments)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tube-song-creation.git
cd tube-song-creation
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your YouTube API key:
   - Get an API key from the [Google Cloud Console](https://console.cloud.google.com/)
   - Enable the YouTube Data API v3
   - Add your API key to the environment variables or configuration file

### Usage

1. Run the main script:
```bash
python main.py
```

2. Enter a YouTube video ID when prompted
3. Wait for the process to complete:
   - Comment fetching
   - Sentiment analysis
   - Lyrics generation
   - Audio creation

4. The generated song will be saved as `generated_song.mp3`

## 🛠️ Project Structure

- `main.py` - Main application entry point
- `youtube_comments.py` - Handles YouTube API interaction and comment fetching
- `sentiment_analyzer.py` - Analyzes comment sentiment
- `lyrics_generator.py` - Generates song lyrics from analyzed comments
- `audio_generator.py` - Creates audio from generated lyrics

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- YouTube Data API for comment access
- Various AI and NLP libraries for sentiment analysis
- Audio generation libraries for music creation

---

Made with ❤️ by Suhail (https://github.com/demonbruster)
