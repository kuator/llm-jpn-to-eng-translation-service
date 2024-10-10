from typing import Any
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, PreTrainedTokenizer, PreTrainedTokenizerFast, pipeline


class TranslationService:

    def __init__(self) -> None:
        self._models_dict = {
            'nllb-1.3B': 'facebook/nllb-200-1.3B',
            'nllb-3.3B': 'facebook/nllb-200-3.3B',
            'nllb-distilled-600M': 'facebook/nllb-200-distilled-600M',
            'nllb-distilled-1.3B': 'facebook/nllb-200-distilled-1.3B',
        }


    def load_model(self, model_name: str) -> tuple[Any, PreTrainedTokenizer | PreTrainedTokenizerFast]:
        model = AutoModelForSeq2SeqLM.from_pretrained(self._models_dict[model_name])
        tokenizer = AutoTokenizer.from_pretrained(self._models_dict[model_name])
        
        return (model, tokenizer)

    def translation(self, source: str, target: str, text: str, model_name: str = 'nllb-distilled-1.3B') -> str:

        (model, tokenizer) = self.load_model(model_name)

        translator = pipeline(
            'translation',
            model=model,
            tokenizer=tokenizer,
            src_lang=source,
            tgt_lang=target
        )

        output = translator(text, max_length=400)

        output = output[0]['translation_text']
        return output


    if __name__ == '__main__':
        text = 'ホンダとスズキ原付きバイクの代わりに電動バイクを増やす'
        result = translation("jpn_Jpan", 'eng_Latn', text, 'nllb-distilled-1.3B')
        print(result)
