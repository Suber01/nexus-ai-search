import math

from src.retrieval.keyword_search import (
    tokenize,
    documents,
    build_index,
    ranking,
)


def term_frequency(term, document):
    tokens = tokenize(document)
    return tokens.count(term.lower())


def inverse_document_frequency(term, documents):
    index = build_index(documents)

    total_documents = len(documents)
    document_frequency = len(index.get(term.lower(), set()))

    if document_frequency == 0:
        return 0

    return math.log(total_documents / document_frequency)


def tf_idf(term, document, documents):
    tf = term_frequency(term, document)
    idf = inverse_document_frequency(term, documents)

    return tf * idf


def score_document(query, document, documents):
    query_tokens = tokenize(query)
    score = 0

    for term in query_tokens:
        score += tf_idf(term, document, documents)

    return score


def search_tfidf(query, documents):
    if not query or not query.strip():
        return {}

    results = {}

    for doc_id, document in documents.items():
        score = score_document(query, document, documents)

        if score > 0:
            results[doc_id] = score

    return ranking(results)


if __name__ == "__main__":
    query = "lambda timeout"
    results = search_tfidf(query, documents)
    print(results)
