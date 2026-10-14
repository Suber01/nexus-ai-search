import math
from src.retrieval.keyword_search import tokenize, documents, build_index, ranking

def term_frequency(term, document):
    tokens = tokenize(document)
    
    return tokens.count(term)

def inverse_document_frequency(term, documents):
    index = build_index(documents)

    N = len(documents)
    df = len(index.get(term.lower(), set()))

    if df == 0:
        return 0

    return math.log(N / df)

def tf_idf(term, document, documents):
    tf = term_frequency(term, document)
    idf = inverse_document_frequency(term, documents)

    return tf * idf


'''
query — what the user searches for.
document — the text of the current document.
documents — the entire collection.'''
def score_document(query, document, documents):
    query_tokens = tokenize(query)
    score = 0

    for term in query_tokens:
        score += tf_idf(term, document, documents)

    return score

def search_tfidf(query, documents):
    results = {}

    for doc_id, document in documents.items():
        score = score_document(query, document, documents)

        if score > 0:
            results[doc_id] = score

    return ranking(results)

print(term_frequency("lambda", documents["D1"]))
print(term_frequency("lambda", documents["D4"]))
print(term_frequency("AWS", documents["D1"]))

print(inverse_document_frequency("lambda", documents))
print(inverse_document_frequency("repartition", documents))
print(inverse_document_frequency("docker", documents))

print(tf_idf("lambda", documents["D1"], documents))
print(tf_idf("repartition", documents["D3"], documents))

print(score_document("lambda timeout", documents["D1"], documents))
print(score_document("lambda timeout", documents["D4"], documents))

print(search_tfidf("lambda timeout", documents))

results = search_tfidf("lambda timeout", documents)
ranked_results = ranking(results)

print(ranked_results)