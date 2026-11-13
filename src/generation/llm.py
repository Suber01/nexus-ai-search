import requests
from src.generation.prompt_builder import build_prompt

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_response(prompt):
    payload = {
        "model": "gemma3:1b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    result = response.json()
    return result["response"]

if __name__ == "__main__":
    query = "What is AWS Lambda?"

    documents = [
    {
        "doc_id": "D1",
        "text": (
            "AWS Lambda is a serverless compute service "
            "that runs code without requiring users to "
            "manage servers. It has a maximum execution timeout."
        )
    },
    {
        "doc_id": "D4",
        "text": (
            "Lambda functions can be configured with "
            "memory and timeout settings."
        )
    }
    ]

    prompt = build_prompt(query, documents)

    answer = generate_response(prompt)

    print("\nGenerated Answer:\n")
    print(answer)
       