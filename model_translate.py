from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, TranslationPipeline
import torch


"""
1. facebook/nllb-200-distilled-600M ~1.2 ГБ ❌ Низкое ✅ Очень быстро Облегчённая версия NLLB
2. facebook/nllb-mt5-418M ~800 МБ ⚠️ Ниже среднего ✅ Быстро Хуже, чем основные NLLB
3. facebook/nllb-mt5-base ~1.5 ГБ ⚠️ Среднее ✅–⚠️ Лучше, чем distilled
4. facebook/nllb-200-1.3B ~2.5 ГБ ✅ Выше среднего ⚠️–❌ Отличное качество, но медленно
5. Helsinki-NLP/opus-mt-* ~100–300 МБ ⚠️ Среднее ✅ Очень быстро Ограниченное число языков Примеры : opus-mt-en-ru, opus-mt-es-fr, opus-mt-multi_higher (Два языка)
6. m2m100_418M ~800 МБ ✅ Среднее+ ✅ Быстро От Meta, поддерживает 100 языков
7. m2m100_1.2B ~2.3 ГБ ✅ Отличное ⚠️–❌ Лучшая из Meta, но тяжёлая
8. facebook/nllb-200-distilled-1.3B
"""
# Загрузка модели и токенизатора
model_name = "facebook/nllb-200-distilled-1.3B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
# Делаем pipeline для удобства
translator = TranslationPipeline(model=model, tokenizer=tokenizer)

def translate_model(text, src_lang, tgt_lang='ru'):
    lang_map = {
        'en': 'eng_Latn',
        'ru': 'rus_Cyrl',
        'es': 'spa_Latn',
        'fr': 'fra_Latn',
        'de': 'deu_Latn',
        'it': 'ita_Latn'
    }

    src_code = lang_map[src_lang]
    tgt_code = lang_map[tgt_lang]

    translated = translator(
        text,
        src_lang=src_code,
        tgt_lang=tgt_code,
        max_length=512,
        num_beams=5,
        length_penalty=1.2,
        truncation=False,
        clean_up_tokenization_spaces=True
    )

    return translated[0]['translation_text']