from groq import Groq
import os
from dotenv import load_dotenv


load_dotenv()
groq_api_key = os.environ.get("GROQ_API_KEY")


client = Groq(
    api_key=groq_api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Do you know IELTs?",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)