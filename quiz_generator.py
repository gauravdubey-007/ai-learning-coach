from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_quiz(topic):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""Generate exactly 10 multiple choice questions on topic: {topic}
                
                Format each question EXACTLY like this:
                Q1. Question here?
                A. Option 1
                B. Option 2
                C. Option 3
                D. Option 4
                Answer: A"""
            }
        ]
    )
    return response.choices[0].message.content