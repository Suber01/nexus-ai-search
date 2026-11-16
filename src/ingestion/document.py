from dataclasses import dataclass, field

@dataclass
class DocumentChunk:
    chunk_id: str
    doc_id: str
    source: str
    file_type: str
    text: str
    metadata: dict = field(default_factory=dict)