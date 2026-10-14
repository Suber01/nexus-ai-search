
from src.retrieval.tfidf import (
    term_frequency,
    inverse_document_frequency,
    tf_idf,
    score_document,
    search_tfidf,
    documents,
)


def test_term_frequency():
    assert term_frequency("lambda", documents["D1"]) == 1


def test_idf_rare_term():
    assert inverse_document_frequency("repartition", documents) > \
           inverse_document_frequency("functions", documents)


def test_tf_idf():
    assert tf_idf("lambda", documents["D1"], documents) > 0


def test_search_tfidf():
    results = search_tfidf("lambda timeout", documents)
    assert list(results.keys()) == ["D1", "D4"]


def test_search_unknown_term():
    assert search_tfidf("docker", documents) == {}


def test_search_empty_query():
    assert search_tfidf("", documents) == {}
