from transformers import pipeline
from textblob import TextBlob

# Load lightweight distilbert model for emotion detection
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)

def detect_emotion(text: str):
    result = emotion_classifier(text)
    # result example: [{'label': 'joy', 'score': 0.99}]
    return result[0]['label']

def get_sentiment(text: str):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"
