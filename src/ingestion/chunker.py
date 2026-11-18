import re

def split_text(text, separator):
    if not separator:
        return list(text)

    parts = re.split(f"({re.escape(separator)})", text)

    chunks = []

    for i in range(0, len(parts), 2):
        piece = parts[i]

        
        if i + 1 < len(parts):
            piece += parts[i + 1]

        chunks.append(piece)

    return chunks

def merge_splits(splits, chunk_size):
    chunks = []
    current_chunk = ""

    for split in splits:
        if len(current_chunk) + len(split) <= chunk_size:
            current_chunk += split
        else:
            chunks.append(current_chunk)
            current_chunk = split

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def recursive_split(text, chunk_size, separators):
    if len(text) <= chunk_size:
        return [text]
    if not separators:
        return list(text)

    separator = separators[0]
    remaining_separators = separators[1:]

    splits = split_text(text, separator)

    good_splits = []

    for split in splits:
        if len(split)<=chunk_size:
            good_splits.append(split)
        else:
            good_splits.extend(
                recursive_split(
                    split, chunk_size, remaining_separators
                )
            )

    return merge_splits(good_splits, chunk_size)
    

if __name__ == '__main__':
    text = (
    "AWS Lambda is a serverless compute service. "
    "Python is a programming language. "
    "Spark supports distributed processing."
    )

    chunks = recursive_split(
    text,
    chunk_size=90,
    separators=["\n\n", "\n", ". ", " ", ""]
    )

    print(chunks)