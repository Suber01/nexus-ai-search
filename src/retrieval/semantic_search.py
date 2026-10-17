
from sentence_transformers import SentenceTransformer
from src.retrieval.keyword_search import documents


#Load the pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


#Prepare document data
document_ids = list(documents.keys())
document_texts = list(documents.values())


#Generate document embeddings once
document_embeddings = model.encode(document_texts)


#Search documents by semantic similarity
def search_semantic(query, top_k = 5):

    if not query or not query.strip():
        return []

    # Convert the query into an embedding
    query_embedding = model.encode(query)

    # Compare the query with all document embeddings
    similarities = model.similarity(
        query_embedding,
        document_embeddings
    )

    # Sort document indices by similarity, highest first
    ranked_indices = similarities[0].argsort(descending=True)

    # Collect ranked search results
    results = []

    for index in ranked_indices[:top_k]:
        index = index.item()

        doc_id = document_ids[index]
        doc_text = document_texts[index]
        score = similarities[0][index].item()

        results.append({
            "doc_id": doc_id,
            "score": score,
            "text": doc_text
        })

    return results


# Run a sample search when executing this module
if __name__ == "__main__":
    query = "How can I run code without managing servers?"

    results = search_semantic(query, top_k = 5)

    print(f"\nQuery: {query}\n")
    print("Empty query:", search_semantic(""))
    print("Whitespace query:", search_semantic("   "))
    for result in results:
        print(
            f"{result['doc_id']} | "
            f"Score: {result['score']:.4f} | "
            f"{result['text']}"
        )
