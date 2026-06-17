from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_quiz(topic):
    word_count = len(topic.split())
    
    if word_count >= 4:
        num_questions = 50
    elif word_count >= 2:
        num_questions = 10
    else:
        num_questions = 5

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""Analyze the topic: "{topic}"
                
                Rules:
                - If topic is very broad (like ML, AI, Deep Learning) → generate 50 questions
                - If topic is medium (like Data Science, Python) → generate 10 questions  
                - If topic is specific/small (like loops, arrays) → generate 5 questions
                
                Decide yourself how many questions to generate based on topic depth.
                
                Format each question like this:
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