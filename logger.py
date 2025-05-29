from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client.mental_health_chatbot

def log_message(user_text: str, emotion: str, sentiment: str):
    db.logs.insert_one({
        "timestamp": datetime.utcnow(),
        "message": user_text,
        "emotion": emotion,
        "sentiment": sentiment
    })
