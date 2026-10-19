
from sentence_transformers import CrossEncoder


reranker_model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank(query, candidates):
    if not query or not query.strip() or not candidates:
        return []

    pairs = [
        (query, candidate["text"])
        for candidate in candidates
    ]

    scores = reranker_model.predict(pairs)

    reranked_results = []

    for candidate, score in zip(candidates, scores):
        reranked_results.append({
            **candidate,
            "rerank_score": float(score)
        })

    return sorted(
        reranked_results,
        key=lambda result: result["rerank_score"],
        reverse=True
    )
