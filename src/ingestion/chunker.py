def split_text(text, separator):
    return text.split(separator)

def recursive_split(text, chunk_size, separators):
    if len(text) <= chunk_size:
        return [text]
    if not separators:
        return list(text)

    separator = separators[0]
    remaining_separators = separators[1:]

    splits = split_text(text, separator)

    chunks = []

    for split in splits:
        if len(split)<=chunk_size:
            chunks.append(split)
        else:
            chunks.extend(
                recursive_split(
                    split, chunk_size, remaining_separators
                )
            )

    return chunks
    

if __name__ == '__main__':
    text = (
    "AWS Lambda is a serverless compute service. "
    "Python is a programming language. "
    "Spark supports distributed processing."
    )

    chunks = recursive_split(
    text,
    chunk_size=50,
    separators=["\n\n", "\n", ". ", " ", ""]
    )

    print(chunks)