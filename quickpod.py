

import os
from dotenv import load_dotenv
from spotifypodcast import SpotifyPodcast
from youtubedownloader import YouTubeDownloader
from whipertranscriber import WhisperTranscriber
from gpt3summarizer import GPT3Summarizer

from pydub import AudioSegment


# Load API credentials from .env file
load_dotenv()

SPOTIFY_CLIENT_ID =  os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET =  os.getenv("SPOTIFY_CLIENT_SECRET")
OPENAI_API_KEY =  os.getenv("OPENAI_API_KEY")


def download_spotify(podcast_url):
    podcast = SpotifyPodcast(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    # file_id = podcast.get_episode_id(podcast_url)
    audio_path = podcast.download_episode(podcast_url)
    return audio_path


def summarize(audio_path, file_id, max_sentences=10):
    transcriber = WhisperTranscriber(OPENAI_API_KEY)
    transcript = transcriber.transcribe(audio_path)
    print(transcript)

    summarizer = GPT3Summarizer(OPENAI_API_KEY, model_engine="gpt-3.5-turbo")
    summary = summarizer.summarize(file_id, transcript, max_sentences)
    return transcript, summary


def main():
    podcast_url = "https://open.spotify.com/episode/6edTClXMUOX5BEMgseBMSr?si=7U5OdqeIQFS4S_zmNuNYww"
    audio_path = download_spotify(podcast_url)
    file_id = 101
    summarize(audio_path, file_id)

if __name__ == '__main__':
    main()