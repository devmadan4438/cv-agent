from fastapi import APIRouter, UploadFile
import shutil
import tempfile
from uuid import uuid4
import logging

# services
from app.services.section_detect.section_detector import SectionDetector
from app.services.parser import ParserFactory
from app.services.metadata.factory import MetadataExtractorFactory
from app.services.chunking.factory import ChunkFactory
from app.services.embedding.factory import EmbeddingFactory
from app.services.vector_store.faiss import FAISSService

from app.schemas.metadata import Skill, SkillList

from app.core.response import success_response
from app.core.config import VECTOR_DIR

# logger
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/")
async def upload_resume(file: UploadFile):
    session_id = str(uuid4())
    
    logger.info(f"Start CV Processing for {session_id}: >", file.filename)
   
    suffix = "." + file.filename.split(".")[-1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        shutil.copyfileobj(file.file, tmp)

    # CV Parse
    parser = ParserFactory.get_parser(file.filename)
    parsed_document = parser.parse(tmp.name)

    # CV Sections
    detector = SectionDetector()
    sections = detector.detect(parsed_document)

    # Extract metaInfo
    metadata = []
    
    for section in sections:

        extractor = MetadataExtractorFactory.get(section.name)

        if extractor:
            metadata.extend(
                extractor.extract(section)
            )

    # Semantic Chunking
    documents = []
    skillList  = SkillList(skills=[])

    for entity in metadata:
        if isinstance(entity, Skill):
            # Collect all skills together
            skillList.skills.append(entity)
            continue

        # Flush accumulated skills before processing a non-skill entity
        if skillList.skills:
            chunker = ChunkFactory.get(skillList)
            if chunker:
                documents.extend(chunker.chunk(skillList))
            skillList = SkillList(skills=[])

        # Process current non-skill entity
        chunker = ChunkFactory.get(entity)
        if chunker:
            documents.extend(chunker.chunk(entity))

    # Flush remaining skills (if metadata ends with skills)
    if skillList.skills:
        chunker = ChunkFactory.get(skillList)
        if chunker:
            documents.extend(chunker.chunk(skillList))
            
    # Embedding
    embedding = EmbeddingFactory.get('nomic')

    faiss = FAISSService(embedding.get_embeddings())

    faiss.build(documents)

    logger.info(f"CV Embedding Done for {session_id}: >", file.filename)
    
    faiss.save(f"{VECTOR_DIR}/{session_id}")

    logger.info(f"CV Process Done for {session_id}: >", file.filename)

    return success_response(
        message="You are ready to ask questions about your CV", 
        data={ "session_id" : session_id}
    )