from fastapi import FastAPI
from src.routes.querying import router as querying_router

app = FastAPI()

app.include_router(querying_router)


# if __name__ == '__main__':
#     text = 'ホンダとスズキ原付きバイクの代わりに電動バイクを増やす'
#     result = translation("jpn_Jpan", 'eng_Latn', text, 'nllb-distilled-1.3B')
#     print(result)
