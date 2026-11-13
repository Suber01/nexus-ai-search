def build_prompt(query, documents):
    context = "\n\n".join(
        document["text"]
        for document in documents
    )

    prompt = f"""
    Answer the question using only the context provided below.

    If the context does not contain enough information,
    say that you don't have enough information.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    return prompt