# Speech-To-Text-Sentiment-Analyser-
It accepts speech as input and converts it into text and then determines the sentiment


```markdown
# Speech Recognition and Sentiment Analysis

## Overview

This repository contains a Python script that utilizes the SpeechRecognition library to transcribe spoken words and then employs the TextBlob library for sentiment analysis on the transcribed text.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/speech-recognition-sentiment-analysis.git
   cd speech-recognition-sentiment-analysis
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script:**
   Execute the Python script to capture speech input, transcribe it using Google Speech Recognition, and perform sentiment analysis.
   ```bash
   python speech_sentiment_analysis.py
   ```

## Dependencies

- speech_recognition
- TextBlob

## How it Works

1. **Speech Recognition:**
   - The script uses the SpeechRecognition library to capture audio input from the default microphone.

2. **Transcription:**
   - Google Speech Recognition is employed to transcribe the spoken words into text.

3. **Sentiment Analysis:**
   - The transcribed text is analyzed for sentiment using the TextBlob library.

4. **Output:**
   - The sentiment analysis result (positive, negative, or neutral) is displayed.

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Your feedback is highly appreciated!
