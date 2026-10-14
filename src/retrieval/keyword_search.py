import string 

documents = {
     "D1": "AWS Lambda functions have a maximum execution timeout.",
    "D2": "Python dictionaries store key-value pairs.",
    "D3": "Spark repartition can cause a shuffle operation.",
    "D4": "Lambda functions can be configured with memory and timeout.",
    "D5": "SQL window functions allow calculations across related rows."
}


def tokenize(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()

#This builds inverted index 
def build_index(documents):
    index = {}
    for doc_id, text in documents.items(): 
        #doc_id = D1
        #text = ....
        tokens = tokenize(text)
        for token in tokens:
            if token not in index: 
                index[token] = set()
            index[token].add(doc_id)
    return index

def search(query, index):
    if not query:
        return {}
    
    query_tokens = tokenize(query)
    result = {}
    for q_token in query_tokens: 
        for doc_id in index.get(q_token, set()):
            result[doc_id] = result.get(doc_id, 0) + 1
    return result
    

def ranking(result):    
    return dict(sorted(result.items(), key=lambda x:x[1], reverse = True))



if __name__ == "__main__": 
    index = build_index(documents)

    result = search("lambda timeout", index)
    print(ranking(result))

    result = search("docker", index)
    print(ranking(result))

    result = search("spark repartition", index)
    print(ranking(result))



