from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load the emotion classifier once
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

class Message(BaseModel):
    message: str

# Empathetic responses mapped to emotions
emotion_responses = {
    "joy": "I'm glad you're feeling good! Keep doing what brings you joy.",
    "sadness": "I'm sorry you're feeling sad. You're not alone. I'm here to support you.",
    "anger": "It's okay to feel angry sometimes. Would you like to talk about what's bothering you?",
    "fear": "It sounds like you're feeling scared or anxious. Try some deep breaths or calming music. I'm here for you.",
    "surprise": "That sounds unexpected! Would you like to share more about it?",
    "disgust": "I can sense you're upset. Want to talk more about what's bothering you?",
    "neutral": "Thanks for sharing. How can I support you further?"
}

@app.get("/")
def read_root():
    return {"message": "Mental Health Support Chatbot is running"}

@app.post("/chat")
async def chat(message: Message):
    user_message = message.message
    results = emotion_classifier(user_message)
    
    # If top_k=None, results will be a list of list of dicts
    # top_emotion = results[0][0]['label'].lower() 
    top_emotion = results[0]['label'].lower()
 # Access the top label
    response = emotion_responses.get(top_emotion, "Thank you for sharing. How can I help?")
    
    return {
        "emotion": top_emotion,
        "reply": response
    }

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            results = emotion_classifier(data)
            top_emotion = results[0]['label'].lower()
            bot_reply = emotion_responses.get(top_emotion, "Thank you for sharing. I'm here to listen.")

            await websocket.send_json({
                "emotion": top_emotion,
                "reply": bot_reply
            })
    except WebSocketDisconnect:
        print("Client disconnected")


