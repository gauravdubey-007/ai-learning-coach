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

Extract ONLY the main academic/exam topics from this syllabus text.
Ignore everything else like dates, page numbers, instructions, college names, random words.

Return ONLY a Python list of topics like:
["Topic 1", "Topic 2", "Topic 3"]

No explanation, no extra text — just the list!

Syllabus text:
{text}"""
            }
        ]
    )
    
    result = response.choices[0].message.content.strip()
    
    # List parse karo
    try:
        import ast
        topics = ast.literal_eval(result)
        return topics
    except:
        # Agar parse na ho toh line by line lo
        topics = []
        for line in result.split("\n"):
            line = line.strip().strip("-").strip("*").strip()
            if line and len(line) > 2:
                topics.append(line)
        return topics