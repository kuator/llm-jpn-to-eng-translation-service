from typing import Annotated
from fastapi import APIRouter, Depends
from src.dependencies import get_translation_service
from src.services.translation_service import TranslationService

router = APIRouter()

@router.get("/query/", tags=["querying"])
async def query(translation_service: Annotated[TranslationService, Depends(get_translation_service)]):
    text = 'ホンダとスズキ原付きバイクの代わりに電動バイクを増やす'
    result = translation("jpn_Jpan", 'eng_Latn', text, 'nllb-distilled-1.3B')
    print(result)
    return [{"username": "Rick"}, {"username": "Morty"}]
