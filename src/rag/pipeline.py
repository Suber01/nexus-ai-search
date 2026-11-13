from src.retrieval.semantic_search import search_semantic
from src.retrieval.reranker import rerank
from src.generation.prompt_builder import build_prompt
from src.generation.llm import generate_response


def answer_question(query, top_k=3):

    candidates = search_semantic(query, top_k=top_k)

    print("\nRetrieved documents:")
    for doc in candidates:
        print(doc["doc_id"], doc["text"])

    ranked_documents = rerank(query, candidates)

    print("\nReranked documents:")
    for doc in ranked_documents:
        print(doc["doc_id"], doc["rerank_score"])

    prompt = build_prompt(query, ranked_documents)

    answer = generate_response(prompt)

    return answer

if __name__ == "__main__":
    query = "How can I run code without managing servers?"

    answer = answer_question(query)

    print("\nQuestion:", query)
    print("\nNexus Answer:", answer)