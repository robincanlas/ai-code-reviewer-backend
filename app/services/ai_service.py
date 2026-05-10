import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL = os.getenv("MODEL", "deepseek-coder")


def review_code(code: str, language: str) -> str:
    prompt = f"""
You are an expert senior software engineer and code reviewer.

Your task is to review the provided {language} code.

Analyze the code carefully and provide constructive feedback.

## Review Requirements

Provide the following sections:

1. Code Summary
- Briefly explain what the code does.

2. Bugs & Logical Issues
- Identify possible bugs or incorrect behavior.
- Explain why they are problematic.

3. Security Concerns
- Identify security vulnerabilities or unsafe patterns.
- Mention severity if applicable.

4. Performance Concerns
- Identify inefficient logic or unnecessary operations.
- Suggest optimizations if relevant.

5. Readability & Maintainability
- Evaluate naming, structure, modularity, and clarity.
- Suggest improvements.

6. Best Practice Improvements
- Suggest modern or recommended practices for {language}.

7. Refactored Example
- Provide an improved version of the code if possible.

8. Final Score
- Provide a score from 1-10.
- Explain the reasoning behind the score.

## Response Rules

- Respond ONLY using markdown.
- Use headings, bullet points, and code blocks.
- Use syntax-highlighted code blocks when providing examples.
- Be concise but helpful.
- Do not invent functionality not present in the code.
- If no issues are found, explicitly say so.

## Code to Review

```{language}
{code}
```
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
    )

    data = response.json()

    return data["response"]

def stream_review_code(code: str, language: str) -> str:
    prompt = f"""
You are an expert senior software engineer and code reviewer.

Your task is to review the provided {language} code.

Analyze the code carefully and provide constructive feedback.

## Review Requirements

Provide the following sections:

1. Code Summary
- Briefly explain what the code does.

2. Bugs & Logical Issues
- Identify possible bugs or incorrect behavior.
- Explain why they are problematic.

3. Security Concerns
- Identify security vulnerabilities or unsafe patterns.
- Mention severity if applicable.

4. Performance Concerns
- Identify inefficient logic or unnecessary operations.
- Suggest optimizations if relevant.

5. Readability & Maintainability
- Evaluate naming, structure, modularity, and clarity.
- Suggest improvements.

6. Best Practice Improvements
- Suggest modern or recommended practices for {language}.

7. Refactored Example
- Provide an improved version of the code if possible.

8. Final Score
- Provide a score from 1-10.
- Explain the reasoning behind the score.

## Response Rules

- Respond ONLY using markdown.
- Use headings, bullet points, and code blocks.
- Use syntax-highlighted code blocks when providing examples.
- Be concise but helpful.
- Do not invent functionality not present in the code.
- If no issues are found, explicitly say so.

## Code to Review

```{language}
{code}
```
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )

    for line in response.iter_lines():
        if not line:
            continue

        try:
            data = json.loads(
                line.decode("utf-8")
            )

            chunk = data.get(
                "response",
                "",
            )

            if chunk:
                yield chunk

        except Exception:
            continue