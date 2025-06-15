from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()

#os.environ["OPENAI_API_KEY"] = "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"

response = completion(
    model="openai/gpt-4o",
    messages=[{"content": "Hello, how are you?", "role": "user"}]
)

print(response.choices[0].message.content)

