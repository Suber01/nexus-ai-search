from src.generation.prompt_builder import build_prompt



def test_prompt_contains_question():
    prompt = build_prompt(
        "What is AWS Lambda?",
        []
    )

    assert "What is AWS Lambda?" in prompt


def test_prompt_contains_document_context():
    documents = [
        {
            "doc_id": "D1",
            "text": "AWS Lambda runs code without managing servers."
        }
    ]

    prompt = build_prompt("What is Lambda?", documents)

    assert "AWS Lambda runs code without managing servers." in prompt


def test_prompt_contains_multiple_documents():
    documents = [
        {"text": "Lambda is a serverless compute service."},
        {"text": "Lambda has a configurable timeout."}
    ]

    prompt = build_prompt("Explain Lambda.", documents)

    assert "Lambda is a serverless compute service." in prompt
    assert "Lambda has a configurable timeout." in prompt