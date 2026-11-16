from src.ingestion.text_parser import parse_text_file


def test_parse_text_file(tmp_path):
    file_path = tmp_path / "aws_guide.txt"

    file_path.write_text(
        "AWS Lambda is a serverless compute service.",
        encoding="utf-8"
    )

    chunks = parse_text_file(file_path)

    assert len(chunks) == 1

    chunk = chunks[0]

    assert chunk.source == "aws_guide.txt"
    assert chunk.file_type == "txt"
    assert chunk.text == "AWS Lambda is a serverless compute service."
    assert chunk.doc_id == "aws_guide"
    assert chunk.chunk_id == "aws_guide_chunk_001"