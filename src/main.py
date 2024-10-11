from fastapi import FastAPI
from src.routes.query import router as query_router


tags_metadata = [
    {
        "name": "query",
        "description": "endpoints for translating",
    },
]


description = """
Service that utilizes NLLB model to translate japanese text into english
"""


app = FastAPI(
    openapi_tags=tags_metadata,
    title="jpn-to-eng",
    description=description,
    summary="",
    version="0.0.1",
    terms_of_service="https://www.apache.org/licenses/LICENSE-2.0",
    contact={
        "name": "evakuator",
        "url": "https://t.me/bigchungusgaming",
    },
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT",
    },
)

app.include_router(query_router)

