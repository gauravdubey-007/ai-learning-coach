from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_topics(text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""You are an expert syllabus analyzer.

Read this syllabus/document text and extract ONLY the main subjects/topics 
that should be tested in an exam (like "General Knowledge", "Mathematics", 
"Reasoning", "Physical Standards", "Data Structures", "Operating Systems" etc.)

Rules:
- Ignore dates, page numbers, marks, instructions, names, addresses
- Ignore generic words like "topic", "syllabus", "exam", "chapter"
- Give MAXIMUM 5 topics only
- Each topic should be 1-4 words only

Return ONLY in this exact format, nothing else:
TOPIC: topic name here
TOPIC: topic name here

Document text:
{text[:3000]}"""
            }
        ]
    )
    
    result = response.choices[0].message.content.strip()
    
    topics = []
    for line in result.split("\n"):
        line = line.strip()
        if line.upper().startswith("TOPIC:"):
            topic = line.split(":", 1)[1].strip()
            if topic and len(topic) > 2:
                topics.append(topic)
    
    return topics[:5]