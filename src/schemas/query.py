from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    query: str = Field(..., title = 'The translation query', max_length=400)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"query": "ホンダとスズキ原付きバイクの代わりに電動バイクを増やす"}
            ]
        }
    }


class QueryResponse(BaseModel):
    answer: str = Field(..., title = 'The translation response', max_length=400)
