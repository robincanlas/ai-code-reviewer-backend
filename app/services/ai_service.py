import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL = os.getenv("MODEL", "deepseek-coder")

def review_code(code: str, language: str) -> str:
    prompt = f"""
You are a senior software engineer.

Review the following {language} code.

Provide:
1. Bugs
2. Security issues
3. Performance concerns
4. Refactoring suggestions
5. Best practice improvements
6. Final score from 1-10

Code:
{code}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    return data["response"]