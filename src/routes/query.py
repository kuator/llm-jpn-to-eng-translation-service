from typing import Annotated
from fastapi import APIRouter, Depends
from src.dependencies import get_translation_service
from src.schemas.query import QueryRequest, QueryResponse
from src.services.translation_service import TranslationService

router = APIRouter()

@router.post("/query/", tags=["query"])
async def query(
    translation_service: Annotated[TranslationService, Depends(get_translation_service)],
    body: QueryRequest
) -> QueryResponse:
    query = body.query
    translation = translation_service.translation("jpn_Jpan", 'eng_Latn', query, 'nllb-distilled-1.3B')
    response = QueryResponse(answer=translation)
    return response
