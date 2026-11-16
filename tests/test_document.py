from src.ingestion.document import DocumentChunk


def test_document_chunk_creation():
    chunk = DocumentChunk(
        chunk_id="chunk_001",
        doc_id="doc_001",
        source="AWS_Guide.pdf",
        file_type="pdf",
        text="AWS Lambda is a serverless compute service."
    )

    assert chunk.chunk_id == "chunk_001"
    assert chunk.doc_id == "doc_001"
    assert chunk.source == "AWS_Guide.pdf"
    assert chunk.file_type == "pdf"
    assert chunk.text == "AWS Lambda is a serverless compute service."


def test_metadata_defaults_to_empty_dictionary():
    chunk = DocumentChunk(
        "chunk_001",
        "doc_001",
        "AWS_Guide.pdf",
        "pdf",
        "AWS Lambda information."
    )

    assert chunk.metadata == {}


def test_metadata_is_independent_between_chunks():
    chunk1 = DocumentChunk(
        "chunk_001", "doc_001", "AWS.pdf", "pdf", "Text 1"
    )

    chunk2 = DocumentChunk(
        "chunk_002", "doc_001", "AWS.pdf", "pdf", "Text 2"
    )

    chunk1.metadata["page"] = 12

    assert chunk1.metadata["page"] == 12
    assert chunk2.metadata == {}


def test_metadata_supports_different_file_types():
    pdf_chunk = DocumentChunk(
        "chunk_001",
        "doc_001",
        "AWS_Guide.pdf",
        "pdf",
        "AWS Lambda information.",
        metadata={
            "page_number": 7,
            "paragraph_number": 3
        }
    )

    excel_chunk = DocumentChunk(
        "chunk_002",
        "doc_002",
        "sales.xlsx",
        "xlsx",
        "Revenue data.",
        metadata={
            "sheet_name": "Revenue",
            "row_start": 10,
            "row_end": 15
        }
    )

    assert pdf_chunk.metadata["page_number"] == 7
    assert excel_chunk.metadata["sheet_name"] == "Revenue"
    assert excel_chunk.metadata["row_start"] == 10
    assert excel_chunk.metadata["row_end"] == 15