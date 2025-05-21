import os
from typing import Optional
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AudioGenerator:
    def __init__(self):
        self.speech_key = os.getenv('AZURE_SPEECH_KEY')
        self.speech_region = os.getenv('AZURE_SPEECH_REGION')
        self.voice_name = "en-US-AriaNeural"
        
        if not self.speech_key or not self.speech_region:
            raise ValueError("Azure Speech credentials not found in environment variables")
        
        # Initialize speech config
        self.speech_config = speechsdk.SpeechConfig(
            subscription=self.speech_key,
            region=self.speech_region
        )
        self.speech_config.speech_synthesis_voice_name = self.voice_name

    def _create_ssml(self, lyrics: str) -> str:
        # Split lyrics into sections
        sections = lyrics.split('\n\n')
        ssml_lines = []
        for section in sections:
            if section.strip():
                lines = section.split('\n')
                for line in lines:
                    if line.strip():
                        ssml_lines.append(f'<prosody rate="0.9">{line}</prosody><break time="500ms"/>')
        # Wrap all lines in a single <speak> tag
        ssml = f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US"><voice name="{self.voice_name}">{" ".join(ssml_lines)}</voice></speak>'
        return ssml

    def generate_audio(self, lyrics: str, output_file: str = "generated_song.mp3") -> Optional[str]:
        """
        Convert lyrics to audio using Azure Speech service.
        
        Args:
            lyrics: The lyrics to convert to audio
            output_file: Path to save the audio file (default: generated_song.mp3)
            
        Returns:
            Path to the generated audio file if successful, None otherwise
        """
        try:
            # Create SSML markup
            ssml = self._create_ssml(lyrics)
            
            # Create audio config
            audio_config = speechsdk.audio.AudioOutputConfig(filename=output_file)
            
            # Create speech synthesizer
            speech_synthesizer = speechsdk.SpeechSynthesizer(
                speech_config=self.speech_config,
                audio_config=audio_config
            )
            
            # Synthesize speech
            result = speech_synthesizer.speak_ssml_async(ssml).get()
            
            if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                print(f"Audio generated successfully: {output_file}")
                return output_file
            elif result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speechsdk.CancellationDetails(result)
                print(f"Speech synthesis canceled: {cancellation_details.reason}")
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print(f"Error details: {cancellation_details.error_details}")
                return None
            else:
                print(f"Speech synthesis failed: {result.reason}")
                return None
                
        except Exception as e:
            print(f"Error generating audio: {str(e)}")
            return None 