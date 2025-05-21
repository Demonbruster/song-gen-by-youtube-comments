Create an Azure Foundry notebook pipeline that does the following:

### 📥 Step 1: Fetch YouTube Comments
- Use the YouTube Data API v3
- Input: `VIDEO_ID` and `API_KEY`
- Fetch top-level comments (max 100) for the video

### 🔍 Step 2: Analyze Sentiment
- Use the `azure-ai-textanalytics` library
- Connect to Azure AI Language service using `TEXT_ANALYTICS_KEY` and `TEXT_ANALYTICS_ENDPOINT`
- Analyze the sentiment of all fetched comments
- Output: A sentiment count summary (positive, neutral, negative)

### 🎤 Step 3: Generate Song Lyrics
- Use Azure OpenAI's `chat/completions` endpoint (GPT-4 or GPT-3.5-turbo)
- Prompt: “Write a song (chorus + verse) in a poetic style based on these comments and overall sentiment.”
- Dynamically adjust the prompt based on the dominant sentiment

### 🔊 (Optional) Step 4: Convert Lyrics to Audio
- Use Azure Speech (Text-to-Speech)
- Input: generated lyrics
- Voice: `en-US-AriaNeural`
- Output: synthesized audio file (MP3 or WAV)

### 📊 Step 5: Display Results
- Show sentiment pie/bar chart using Plotly or Matplotlib
- Display generated lyrics in markdown
- Provide audio playback (if audio was generated)

### 🧪 Configuration
Use `.env` or `os.environ` to store:
- `YOUTUBE_API_KEY`
- `TEXT_ANALYTICS_KEY`
- `TEXT_ANALYTICS_ENDPOINT`
- `AZURE_OPENAI_KEY`
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_SPEECH_KEY`
- `AZURE_SPEECH_REGION`

Use `!pip install` as needed for:
- `azure-ai-textanalytics`
- `openai`
- `azure-cognitiveservices-speech`
- `requests`
- `matplotlib` or `plotly`

Make each step modular and testable.
Add markdown cells to explain each section in the notebook.
