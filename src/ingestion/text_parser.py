from pathlib import Path
from src.ingestion.document import DocumentChunk

def parse_text_file(file_path):
    file_path = Path(file_path)

    text = file_path.read_text(encoding="utf-8")

    lines = text.splitlines(keepends=True)
    
    char_position = 0

    for line_number, line in enumerate(lines, start=1):
        char_start = char_position
        char_end = char_start + len(line)

       
        char_position = char_end


    chunk = DocumentChunk(
        chunk_id=f"{file_path.stem}_chunk_001",
        doc_id=file_path.stem,
        source=file_path.name,
        file_type=file_path.suffix.lstrip("."),
        text=text
    )

    return [chunk]

if __name__ == "__main__":
    chunks = parse_text_file("data/aws_guide.txt")
    print(chunks)