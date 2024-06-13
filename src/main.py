import os
import sys
from youtube_api import YouTubeAPI
from transcript_processor import TranscriptProcessor
from corrector import Corrector

def main():
    api_key = os.environ["YOUTUBE_API_KEY"]
    youtube_api = YouTubeAPI(api_key)
    transcript_processor = TranscriptProcessor()
    corrector = Corrector()

    video_id = sys.argv[1]
    transcript = youtube_api.get_video_transcript(video_id)
    if transcript:
        processed_transcript = transcript_processor.process_transcript(transcript)
        corrected_transcript = corrector.correct_transcript(processed_transcript)
        print(corrected_transcript)
    else:
        print("No transcript found")

if __name__ == "__main__":
    main()