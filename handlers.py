from aiogram import Router, types, F
from aiogram.filters import Command
import text
import db
import os
import re
import asyncio
import numpy as np
# from sentence_transformers import SentenceTransformer
# import faiss
from utils import *
from config import bot_hub_API, deepseek_API
from openai import OpenAI
import random as r
from io import BytesIO
from aiogram.types import BufferedInputFile, Message, FSInputFile, InputFile, Voice, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder
import json
from QUESTIONS import drafting_easy_questions, drafting_deep_questions
import keyboards
import uuid
from pydub import AudioSegment
from aiogram.fsm.context import FSMContext
# from model_translate import translate_model
from text_to_speech import google_text_to_speech as text_to_speech, deepgram_text_to_speech
from speech_to_text import speech_to_text_assemblyai, speech_to_text_deepgram, vosk
# from model_speech_to_text import whisper_3v_turbo
from essay import get_promt_to_essay, get_random_topic
from local_model import query_lm_studio
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


# os.makedirs("logs", exist_ok=True)
# log_filename = f"logs/bot_{datetime.now().strftime('%Y-%m-%d')}.log"
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
#     handlers=[logging.FileHandler(log_filename, encoding="utf-8")],
#     force=True
# )
# logger = logging.getLogger(__name__)
# logger.info("Бот запущен!")

os.makedirs("logs", exist_ok=True)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
handler = TimedRotatingFileHandler(
    "logs/bot.log",
    when="midnight",
    interval=1,
    backupCount=7,
    encoding="utf-8"
)
handler.setFormatter(formatter)
handler.suffix = "%Y-%m-%d"  # bot.log.2025-04-05
logger.addHandler(handler)
logger.propagate = False
logger.info("✅ Бот запущен!")
# logger.info("Бот запущен!")
# logger.warning("Памяти осталось мало")
# logger.error("Не удалось обработать голосовое сообщение") в обработчеке ошибок

router = Router()

users = db.Users('users')
study_words_user = db.UserStudyWords('study_words_user')

en = db.DataBaseWordsLanguage('en')
es = db.DataBaseWordsLanguage('es')
fr = db.DataBaseWordsLanguage('fr')
de = db.DataBaseWordsLanguage('de')
it = db.DataBaseWordsLanguage('it')
rus = db.DataBaseWordsLanguage('rus')

client_bot_hub = OpenAI(api_key=bot_hub_API,
                base_url='https://bothub.chat/api/v2/openai/v1')

client_deepseek = OpenAI(api_key=deepseek_API,
                         base_url="https://api.deepseek.com")

keyboards = {'ru': keyboards.Russian_keyboards(),
             'en': keyboards.English_keyboards(),
             'es': keyboards.Spanish_keyboards(),
             'de': keyboards.German_keyboards(),
             'fr': keyboards.French_keyboards(),
             'it': keyboards.Italian_keyboards()}

texts = {'ru': text.Russian_text(),
         'en': text.English_text(),
         'es': text.Spanish_text(),
         'de': text.German_text(),
         'fr': text.French_text(),
         'it': text.Italian_text()}

# Поиск на наличие запрещенных слов в запросе к нейросети
# model = SentenceTransformer('deepvk/USER-bge-m3')
# index = faiss.IndexFlatIP(1024)
# materials_texts = []
#
# def embed_text(text):
#     embedding = model.encode(text)
#     return np.array(embedding, dtype=np.float32)
#
# def rag(query, top_k=1, threshold=0.5):
#     query_embedding = embed_text(query).reshape(1, -1)
#     faiss.normalize_L2(query_embedding)
#     D, I = index.search(query_embedding, top_k)
#     similar_info = [materials_texts[i] for i, dist in zip(I[0], D[0]) if dist > threshold and i < len(materials_texts)]
#     return similar_info
#
# async def async_embed_text(text):
#     func = lambda: embed_text(text)
#     loop = asyncio.get_event_loop()
#     return await loop.run_in_executor(None, func)
#
# async def async_rag(text):
#     func = lambda: rag(text)
#     loop = asyncio.get_event_loop()
#     return await loop.run_in_executor(None, func)
#
# for title in materials:
#     material_embedding = embed_text(title).reshape(1, -1)
#     faiss.normalize_L2(material_embedding)
#     materials_texts.append(title)
#     index.add(material_embedding)


async def all_user_words_on_repeat(bot):
    info = await db.UsersWords.schedule_all_pending_repeats()
    for user_id in info:
        for unique_id, timer in info[user_id]:
            if timer == 1:
                asyncio.create_task(repeat_1(user_id, bot, unique_id, 1800 - r.randint(600, 1200)))
            elif timer == 2:
                asyncio.create_task(repeat_2(user_id, bot, unique_id, 28800 - r.randint(7200, 18000)))
            elif timer == 3:
                asyncio.create_task(repeat_3(user_id, bot, unique_id, 86400 - r.randint(21600, 43200)))
            elif timer == 4:
                asyncio.create_task(repeat_4(user_id, bot, unique_id, 259200 - r.randint(72000, 144000)))


async def async_translate_with_detection(text: str, src_lang, target_lang: str = "rus_Cyrl"):
    func = lambda: translate_model(text, src_lang)
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, func)


async def async_speech_to_text(audio, lang):
    func = lambda: whisper_3v_turbo(audio, lang)
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, func)


async def request_to_AI(messages, local=False):
    # Вариант 1 через API к local model
    if local:
        return await query_lm_studio(messages)

    # Запрос к нейросети Вариант 2 через API к удалленому серверу через BotHub / models: deepseek-chat-v3-0324:free , deepseek-chat-v3-0324 , qwen3-235b-a22b
    response = client_bot_hub.chat.completions.create(
        messages=messages,
        model='deepseek-chat-v3-0324',
    )

    # Запрос к нейросети Вариант 3 через API к удалленому серверу через Deepseek
    # response = client_deepseek.chat.completions.create(
    #     model="deepseek-chat",
    #     messages=messages,
    #     stream=False
    # )

    return re.sub(r'[*#_~`]', '', response.choices[0].message.content)

async def text_and_keyboard(user_id):
    level = await users.get_level(user_id)
    lang = await users.get_learn_lang(user_id)
    native = await users.get_native_lang(user_id)
    if level > 'A2':
        text = texts[lang]
        keyboard = keyboards[lang]
    else:
        text = texts[native]
        keyboard = keyboards[native]
    return text, keyboard

async def valid_msg_text(text):
    if len(text) > 300:
        return False
    return True

# REGISTRATION
@router.message(Command('start'))
async def start_handler(msg, state: FSMContext, bot):
    user_id = msg.from_user.id
    data = await state.get_data()
    if data.get('to_delete', 0):
        await bot.delete_message(chat_id=user_id, message_id=data['to_delete'])
        await state.update_data(to_delete=None)

    if user_id not in await users.get_users_ids():
        logger.info(f"📱 Пользователь {user_id} запустил бота")
        keyboard = keyboards['ru']
        to_delete = await msg.answer(text=texts['ru'].greet.format(name=msg.from_user.first_name) + '\n\n' + texts['en'].greet.format(name=msg.from_user.first_name),
                                     reply_markup=keyboard.choose_native_lang())

        await state.update_data(to_delete=to_delete.message_id)
    await bot.delete_message(chat_id=user_id, message_id=msg.message_id)


@router.callback_query(F.data.startswith('native_'))
async def ru_native(callback, state: FSMContext):
    native_lang = callback.data.split("_")[-1]
    keyboard = keyboards[native_lang]
    text = texts[native_lang]
    await state.update_data(native_lang=native_lang)
    await callback.message.edit_text(text=text.choose_language.format(name=callback.from_user.first_name),
                                     reply_markup=keyboard.will_learn_lang())


@router.callback_query(F.data.startswith('will_learn_'))
async def will_learn_lang_usa(callback, state: FSMContext):
    will_learn_lang = callback.data.split("_")[-1]
    data = await state.get_data()
    keyboard = keyboards[data['native_lang']]
    text = texts[data['native_lang']]
    await state.update_data(will_learn_lang=will_learn_lang,
                            registration=True)
    await callback.message.edit_text(text=text.level,
                                     reply_markup=keyboard.level(will_learn_lang))


@router.callback_query(F.data.startswith("level_"))
async def level0(callback, state: FSMContext):
    level = callback.data.split("_")[-1]
    data = await state.get_data()
    if level > 'A2':
        text = texts[data['will_learn_lang']]
    else:
        text = texts[data['native_lang']]
    await state.set_state(Registration.quantity_words)
    to_delete = await callback.message.edit_text(text=text.range_learn_words)
    await state.update_data(to_delete=to_delete.message_id,
                            level=level)


@router.message(Registration.quantity_words)
async def quantity_words(msg, state: FSMContext, bot):
    data = await state.get_data()
    level = data['level']
    user_id = msg.from_user.id
    if level > 'A2':
        text = texts[data['will_learn_lang']]
        keyboard = keyboards[data['will_learn_lang']]
    else:
        text = texts[data['native_lang']]
        keyboard = keyboards[data['native_lang']]
    if msg.text.isdigit() and await valid_msg_text(msg.text) and 4 < int(msg.text) < 31:
        if user_id not in await users.get_users_ids():
            await msg.answer(text.success)
        menu = await bot.send_message(chat_id=user_id,
                                      text=text.menu,
                                      reply_markup=keyboard.menu(user_id))
        await bot.delete_message(chat_id=user_id, message_id=msg.message_id)
        await bot.delete_message(chat_id=user_id, message_id=data['to_delete'])

        await state.update_data(quantity_words=int(msg.text),
                                menu_id=menu.message_id)

        data = await state.get_data()
        await state.clear()
        if user_id not in await users.get_users_ids():
            await users.add_user_info(user_id, data)
            await db.UsersDicts.create_table(user_id)
            await db.UsersWords.create_table(user_id)
            await study_words_user.add_user(user_id)
            await db.UsersTexts.create_table(user_id)
            logger.info(f"📱 Пользователь {user_id} зарегистрировался!")
        else:
            await users.update_info(user_id, data)

        if data['will_learn_lang'] == 'en':
            words = await en.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        elif data['will_learn_lang'] == 'es':
            words = await es.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        elif data['will_learn_lang'] == 'de':
            words = await de.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        elif data['will_learn_lang'] == 'fr':
            words = await fr.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        elif data['will_learn_lang'] == 'it':
            words = await it.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        elif data['will_learn_lang'] == 'rus':
            words = await rus.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
    else:
        await bot.delete_message(chat_id=user_id, message_id=msg.message_id)
        await bot.delete_message(chat_id=user_id, message_id=data['to_delete'])
        to_delete = await msg.answer(text=text.range_learn_words_2)
        await state.update_data(to_delete=to_delete.message_id)


@router.callback_query(F.data == 'change_language')
async def change_language(callback):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboard.new_lang())


@router.callback_query(F.data.startswith('new_lang_'))
async def will_learn_lang_usa(callback, state: FSMContext):
    will_learn_lang = callback.data.split("_")[-1]
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await state.update_data(registration=True,
                            native_lang='ru',
                            will_learn_lang=will_learn_lang)
    await callback.message.edit_text(text=text.level,
                                     reply_markup=keyboard.level(will_learn_lang))
    await users.update_menu_id(user_id)


@router.callback_query(F.data == 'info_lang')
async def info_lang(callback):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboard.info_lang())

# DIOLOG
@router.callback_query(F.data == 'dialog')
async def dialog(callback):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await callback.message.edit_text(text=text.dialog_1,
                                     reply_markup=keyboard.dialog())


@router.callback_query(F.data == 'dialog_to_start')
async def dialog2(callback, state, bot):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await callback.message.edit_text(text=text.dialog_2)
    await bot.send_message(chat_id=user_id,
                           text=text.dialog_4,
                           reply_markup=ReplyKeyboardMarkup(
                               keyboard=[[KeyboardButton(text=text.dialog_cancel)]],
                               resize_keyboard=True,
                               one_time_keyboard=True))
    await users.update_menu_id(user_id)
    await state.set_state(Dialog.dialog)


@router.message(Dialog.dialog)
async def dialog3(msg, state: FSMContext, bot):
    user_id = msg.from_user.id
    text, keyboard = await text_and_keyboard(user_id)

    text_user = msg.text

    if not text_user:
        await bot.delete_message(chat_id=user_id, message_id=msg.message_id)
        await msg.answer(text=text.dialog_4)
        await state.set_state(Dialog.dialog)
        return

    # similar_info = await async_rag(text_user)  # использовать в функциях где идет запрос к нейросети
    # if similar_info:
    #     await msg.answer("В сообщении используются недопустимые слова/фразы. При их повторном употреблении Вы будете заблокированны.")
    #     await msg.answer(text=text.dialog_4)
    #     await state.set_state(Dialog.dialog)
    #     return

    if await valid_msg_text(text_user):
        level = await users.get_level(user_id)
        lang = await users.get_learn_lang(user_id)
        lang_to_prompt = {
            'es': 'Spanish',
            'en': 'English',
            'de': 'German',
            'fr': 'French',
            'it': 'Italian'
                }[lang]
        if text_user == text.dialog_cancel:
            await state.clear()
            await msg.answer(text=text.dialog_3,
                             reply_markup=ReplyKeyboardRemove())
            menu = await msg.answer(text=text.menu,
                                    reply_markup=keyboard.menu(user_id))
            await users.update_menu_id(user_id, menu.message_id)
            return

        data = await state.get_data()
        if 'voice_msg' in data:
            if data['bot_reply_translated_flag']:
                await bot.edit_message_reply_markup(
                    chat_id=user_id,
                    message_id=data['voice_msg'],
                    reply_markup=keyboard.text_and_translate(text=False,
                                                             translate=False))

        if "dialog_history" not in data:
            history = []
        else:
            history = data["dialog_history"][-6:]
        history.append({"role": "user", "content": text_user})

        messages = [
            {"role": "system", "content": text.SYSTEM_PROMPT.format(lang=lang_to_prompt, level=level)},
            *history
        ]

        try:
            bot_reply = await request_to_AI(messages)
        except Exception as e:
            logger.error(f"🔴 Ошибка запроса к API bot_hub у пользователя {user_id}: {e}")
            await msg.answer('К сожалению не получилось обработать информацию. Попробуйте еще раз.')
            return

        # Перевод Вариант 1.1 через локальную модель-переводчик
        # bot_reply_translated = await async_translate_with_detection(bot_reply, lang)
        # Перевод Вариант 1.2 через локальную модель нейросети
        messages_for_translate = [
            {"role": "system", "content": 'Ты проффесинальный переводчик, который легко определяет язык текста и переводит его на русский. Напиши только перевод и ничего больше.'},
            {"role": "user", "content": f'Переведи этот текст: {bot_reply}'}
        ]

        try:
            bot_reply_translated = await request_to_AI(messages_for_translate)
        except Exception as e:
            logger.error(f"🔴 Ошибка запроса к API bot_hub у пользователя {user_id}: {e}")
            await msg.answer('К сожалению не получилось обработать информацию. Попробуйте еще раз.')
            return

        history.append({"role": "assistant", "content": bot_reply})
        voice_msg = await msg.answer(text=bot_reply,
                                     reply_markup=keyboard.text_and_translate(text=False))
        await state.update_data(dialog_history=history,
                                bot_reply_translated=bot_reply_translated,
                                bot_reply_flag=False,
                                bot_reply_translated_flag=True,
                                voice_msg=voice_msg.message_id)

        await state.set_state(Dialog.dialog)
    else:
        await msg.answer(text=text.long_msg)
        await msg.answer(text=text.dialog_2)
        await state.set_state(Dialog.dialog)


@router.callback_query(F.data == 'voice')
async def dialog2(callback, state, bot):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    lang = await users.get_learn_lang(user_id)
    await callback.message.edit_text(text=text.dialog_2)
    await bot.send_message(chat_id=user_id,
                           text=text.dialog_5,
                           reply_markup=ReplyKeyboardMarkup(
                                         keyboard=[[KeyboardButton(text=text.dialog_cancel)]],
                                         resize_keyboard=True,
                                         one_time_keyboard=True))
    await users.update_menu_id(user_id)
    await state.set_state(Chat_voice.chat_voice)


@router.message(Chat_voice.chat_voice)
async def dialog4(msg, state: FSMContext, bot):
    user_id = msg.from_user.id
    text, keyboard = await text_and_keyboard(user_id)

    text_user = msg.text
    if text_user == text.dialog_cancel:
        await state.clear()
        await msg.answer(text=text.dialog_3, reply_markup=ReplyKeyboardRemove())
        menu = await msg.answer(text=text.menu, reply_markup=keyboard.menu(user_id))
        await users.update_menu_id(user_id, menu.message_id)
        return
    elif text_user:
        await bot.delete_message(chat_id=user_id, message_id=msg.message_id)
        await msg.answer(text=text.dialog_5)
        await state.set_state(Chat_voice.chat_voice)
        return

    data = await state.get_data()
    if 'voice_msg' in data:
        if data['bot_reply_flag'] or data['bot_reply_translated_flag']:
            await bot.edit_message_reply_markup(
                chat_id=user_id,
                message_id=data['voice_msg'],
                reply_markup=keyboard.text_and_translate(text=False,
                                                         translate=False))

    user_dir = f"audio_files/user_{user_id}"
    os.makedirs(user_dir, exist_ok=True)

    # Скачиваем голосовое сообщение
    file_id = msg.voice.file_id
    file = await bot.get_file(file_id)
    file_data = await bot.download_file(file.file_path)

    audio_bytes = BytesIO(file_data.read())
    try:
        audio = AudioSegment.from_ogg(audio_bytes)
    except Exception as e:
        logger.error(f"🔴 Ошибка обработки аудиосообщения от пользователя {user_id}: {e}")
        await msg.answer("❌ Не удалось обработать аудиофайл.")
        await msg.answer(text=text.dialog_5)
        await state.set_state(Chat_voice.chat_voice)
        return

    duration_sec = len(audio) / 1000

    if duration_sec > 60:
        await msg.answer("🎙️ Голосовое сообщение слишком длинное. Пожалуйста, отправьте запись не более 30 секунд.")
        await msg.answer(text=text.dialog_5)
        await state.set_state(Chat_voice.chat_voice)
        return

    level = await users.get_level(user_id)
    lang = await users.get_learn_lang(user_id)

    # готовый вариант без сохранения на диск, при необходимости менять формат wav или mp3, использовать рпи работе с API
    wav_bytes = BytesIO()
    audio.export(wav_bytes, format="wav")
    wav_bytes.seek(0)

    # 2 вариант с сохранением на диск, только таким способом можно пользоваться локальной моделью
    # file_name = f"{user_dir}/voice_user.wav"
    # audio.export(file_name, format="wav")

    try:
        # вариант 1 assemblyai
        transcript = await speech_to_text_assemblyai(wav_bytes)
        if transcript.status == "error":
            raise RuntimeError(f"Transcription failed: {transcript.error}")
        text_user = transcript.text

        # вариант 2 deepgram
        # text_user = await speech_to_text_deepgram(wav_bytes)

        # вариант 3 локальная модель
        # text_user = await async_speech_to_text(file_name, lang)

        # вариант 4 Vosk
        # text_user = await vosk(wav_bytes)
    except Exception as e:
        logger.error(f"🔴 Ошибка запроса к API assemblyai (транскрипция аудио) у пользователя {user_id}: {e}")
        try:
            text_user = await speech_to_text_deepgram(wav_bytes)
        except Exception as e:
            logger.error(f"🔴 Ошибка запроса к API deepgram (транскрипция аудио) у пользователя {user_id}: {e}")
            await msg.answer("Ошибка при распознавании речи. Попробуйте ещё раз.")
            await msg.answer(text=text.dialog_5)
            await state.set_state(Chat_voice.chat_voice)
            return

    # similar_info = await async_rag(text_user)  # использовать в функциях где идет запрос к нейросети
    # if similar_info:
    #     await msg.answer("В голосовом сообщении используются недопустимые слова/фразы. При их повторном употреблении Вы будете заблокированны.")
    #     await msg.answer(text=text.dialog_5)
    #     await state.set_state(Chat_voice.chat_voice)
    #     return

    lang_to_prompt = {
        'es': 'Spanish',
        'en': 'English',
        'de': 'German',
        'fr': 'French',
        'it': 'Italian'
    }[lang]

    if "dialog_history" not in data:
        history = []
    else:
        history = data["dialog_history"][-6:]
    history.append({"role": "user", "content": text_user})
    messages = [
        {"role": "system", "content": text.VOICE_PROMPT.format(lang=lang_to_prompt, level=level)},
        *history
    ]

    # При использовании локальной модели передавать аргумент local=True
    try:
        bot_reply = await request_to_AI(messages)
    except Exception as e:
        logger.error(f"🔴 Ошибка запроса к API bot_hub у пользователя {user_id}: {e}")
        await msg.answer('К сожалению не получилось обработать информацию. Попробуйте еще раз.')
        return

    history.append({"role": "assistant", "content": bot_reply})

    # Перевод Вариант 1.1 через локальную модель
    # bot_reply_translated = await async_translate_with_detection(bot_reply, lang)
    # Перевод Вариант 1.2 через локальную модель нейросети
    messages_for_translate = [
        {"role": "system", "content": 'Ты проффесинальный переводчик, который легко определяет язык текста и переводит его на русский. Напиши только перевод и ничего больше.'},
        {"role": "user", "content": f'Переведи этот текст: {bot_reply}'}
    ]

    try:
        bot_reply_translated = await request_to_AI(messages_for_translate)
    except Exception as e:
        logger.error(f"🔴 Ошибка запроса к API bot_hub у пользователя {user_id}: {e}")
        await msg.answer('К сожалению не получилось обработать информацию. Попробуйте еще раз.')
        return

    # Вариант 2 через API translate
    # -
    if level == 'B1' and lang == 'en':
        # janus
        try:
            voice = await deepgram_text_to_speech(bot_reply, "aura-2-janus-en")
        except Exception as e:
            logger.error(f"🔴 Ошибка запроса к API deepgram (озвучка текста) у пользователя {user_id}: {e}")
            voice = await text_to_speech(bot_reply, lang)
    elif level > 'B1' and lang == 'en':
        # aura-2-andromeda-en, aura-2-thalia-en, aura-2-cordelia-en, aura-2-helena-en, aura-2-janus-en медленная, aura-2-odysseus-en, aura-2-orpheus-en хороший диктор
        try:
            voice = await deepgram_text_to_speech(bot_reply, "aura-2-helena-en")
        except Exception as e:
            logger.error(f"🔴 Ошибка запроса к API deepgram (озвучка текста) у пользователя {user_id}: {e}")
            voice = await text_to_speech(bot_reply, lang)
    else:
        voice = await text_to_speech(bot_reply, lang)

    if voice is None:
        logger.error(f"🔴 Ошибка запроса к API deepgram (озвучка текста) у пользователя {user_id}")
        voice = await text_to_speech(bot_reply, lang)

    audio_file = BufferedInputFile(file=voice.read(),
                                   filename="Answer.mp3")
    voice_msg = await bot.send_voice(
        chat_id=msg.chat.id,
        voice=audio_file,
        reply_markup=keyboard.text_and_translate()
    )

    await state.update_data(dialog_history=history,
                            bot_reply=bot_reply,
                            bot_reply_translated=bot_reply_translated,
                            voice_msg=voice_msg.message_id,
                            bot_reply_flag=True,
                            bot_reply_translated_flag=True)

    await state.set_state(Chat_voice.chat_voice)


@router.callback_query(F.data == 'voice_text')
async def voice_text(callback, state, bot):
    await callback.answer()
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await state.update_data(bot_reply_flag=False)

    data = await state.get_data()
    voice_message_id = data['voice_msg']

    await bot.edit_message_reply_markup(
        chat_id=user_id,
        message_id=voice_message_id,
        reply_markup=keyboard.text_and_translate(text=data['bot_reply_flag'], translate=data['bot_reply_translated_flag']))
    await bot.send_message(
        chat_id=user_id,
        text=data['bot_reply'])


@router.callback_query(F.data == 'voice_translate')
async def voice_text(callback, state, bot):
    await callback.answer()
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await state.update_data(bot_reply_translated_flag=False)

    data = await state.get_data()
    voice_message_id = data['voice_msg']

    await bot.edit_message_reply_markup(
        chat_id=user_id,
        message_id=voice_message_id,
        reply_markup=keyboard.text_and_translate(text=data['bot_reply_flag'], translate=data['bot_reply_translated_flag']))
    await bot.send_message(
        chat_id=user_id,
        text=data['bot_reply_translated'])

# TESTING
@router.callback_query(F.data == 'test_lang')
async def test_lang(callback, state):
    user_id = callback.from_user.id
    data = await state.get_data()
    if user_id not in await users.get_users_ids():
        native = data['native_lang']
        text = texts[native]
        keyboard = keyboards[native]
    else:
        text, keyboard = await text_and_keyboard(user_id)

    if 'registration' in data:
        lang = data['will_learn_lang']
        await callback.message.edit_text(text=text.test_main,
                                         reply_markup=keyboard.test(lang, True))
    else:
        lang = await users.get_learn_lang(user_id)
        await callback.message.edit_text(text=text.test_main,
                                         reply_markup=keyboard.test(lang))


@router.callback_query(F.data.startswith('start_test'))
async def test_lang_(callback, state):
    mode = int(callback.data.split("_")[-1])
    user_id = callback.from_user.id
    data = await state.get_data()
    if user_id not in await users.get_users_ids():
        native = data['native_lang']
        text = texts[native]
        lang = data['will_learn_lang']
    else:
        text, keyboard = await text_and_keyboard(user_id)
        if 'registration' in data:
            lang = data['will_learn_lang']
        else:
            lang = await users.get_learn_lang(user_id)

    if mode:
        QUESTIONS = drafting_easy_questions(lang)
        max_num_q = 5
        max_num_wrongs = 20
    else:
        QUESTIONS = drafting_deep_questions(lang)
        max_num_q = 10
        max_num_wrongs = 50

    test_level = 'A1'
    stats = {
        "A1": 0,
        "A2": 0,
        "B1": 0,
        "B2": 0,
        "C1": 0,
    }
    level_idx = {
        "A1": 0,
        "A2": 0,
        "B1": 0,
        "B2": 0,
        "C1": 0,
    }
    await state.update_data(stats=stats,
                            level_idx=level_idx,
                            QUESTIONS=QUESTIONS,
                            max_num_q=max_num_q,
                            max_num_wrongs=max_num_wrongs,
                            test_level=test_level,
                            correct_answers=0,
                            mode=mode,
                            wrongs=0,
                            num_q=1)

    question = QUESTIONS[test_level][0]
    builder = InlineKeyboardBuilder()
    for i, option in enumerate(question["options"]):
        builder.add(InlineKeyboardButton(
            text=option,
            callback_data=f"starttest_{i}_{question['correct']}"
        ))
    builder.add(InlineKeyboardButton(
        text=text.not_know,
        callback_data=f"starttest_{4}_{question['correct']}"
    ))
    builder.adjust(1)

    await callback.message.edit_text(text=question["question"],
                                     reply_markup=builder.as_markup())


@router.callback_query(F.data.startswith('starttest_'))
async def test_lang_(callback, state):
    data = await state.get_data()
    user_id = callback.from_user.id
    if user_id not in await users.get_users_ids():
        native = data['native_lang']
        text = texts[native]
        keyboard = keyboards[native]
    else:
        text, keyboard = await text_and_keyboard(user_id)

    QUESTIONS = data['QUESTIONS']
    stats = data['stats']
    level_idx = data['level_idx']
    max_num_q = data['max_num_q']
    max_num_wrongs = data['max_num_wrongs']
    test_level = data['test_level']
    correct_answers = data['correct_answers']
    mode = data['mode']
    wrongs = data['wrongs']
    num_q = data['num_q']

    parts = callback.data.split("_")
    answer = int(parts[1])
    correct = int(parts[2])

    level_idx[test_level] += 1
    if correct == answer:
        to_up = {
            'A1': 'A2',
            'A2': 'B1',
            'B1': 'B2',
            'B2': 'C1',
            'C1': 'C1',
        }
        stats[test_level] += 1
        test_level = to_up[test_level]
        correct_answers += 1
    else:
        to_down = {
            'A1': 'A1',
            'A2': 'A1',
            'B1': 'A2',
            'B2': 'B1',
            'C1': 'B2',
        }
        test_level = to_down[test_level]
        wrongs += 1

    if max(stats.values()) < max_num_q and wrongs < max_num_wrongs:
        question = QUESTIONS[test_level][level_idx[test_level]]
        num_q += 1
        builder = InlineKeyboardBuilder()
        for i, option in enumerate(question["options"]):
            builder.add(InlineKeyboardButton(
                text=option,
                callback_data=f"starttest_{i}_{question['correct']}"
            ))
        builder.add(InlineKeyboardButton(
            text=text.not_know,
            callback_data=f"starttest_{4}_{question['correct']}"
        ))
        builder.adjust(1)

        await state.update_data(stats=stats,
                                level_idx=level_idx,
                                test_level=test_level,
                                correct_answers=correct_answers,
                                wrongs=wrongs,
                                num_q=num_q)

        await callback.message.edit_text(text=question["question"],
                                         reply_markup=builder.as_markup())
    else:
        level = max(stats, key=stats.get)
        await state.update_data(level=level)

        if 'registration' in data:
            await state.set_state(Registration.quantity_words)
            to_delete = await callback.message.edit_text(text=text.final.format(l=level) + '\n\n' + text.range_learn_words)
            await state.update_data(to_delete=to_delete.message_id)
        else:
            await callback.message.edit_text(text=text.final_no_mode.format(l=level,
                                                                            corrects=correct_answers,
                                                                            num_q=num_q,
                                                                            a1=stats['A1'],
                                                                            a1o=level_idx['A1'],
                                                                            a2=stats['A2'],
                                                                            a2o=level_idx['A2'],
                                                                            b1=stats['B1'],
                                                                            b1o=level_idx['B1'],
                                                                            b2=stats['B2'],
                                                                            b2o=level_idx['B2'],
                                                                            c1=stats['C1'],
                                                                            c1o=level_idx['C1']),
                                             reply_markup=keyboard.final_test())


@router.callback_query(F.data == 'change')
async def change_level(callback, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    level = data['level']
    user_id = callback.from_user.id
    await users.change_level(level, user_id)
    text, keyboard = await text_and_keyboard(user_id)
    lang = await users.get_learn_lang(user_id)

    if lang == 'en':
        words = await en.get_words_level(level)
        await study_words_user.update_words_study_level(user_id, words, 'main_words')
    elif lang == 'es':
        words = await es.get_words_level(level)
        await study_words_user.update_words_study_level(user_id, words, 'main_words')
    elif lang == 'de':
        words = await de.get_words_level(level)
        await study_words_user.update_words_study_level(user_id, words, 'main_words')
    elif lang == 'fr':
        words = await fr.get_words_level(level)
        await study_words_user.update_words_study_level(user_id, words, 'main_words')
    elif lang == 'it':
        words = await it.get_words_level(level)
        await study_words_user.update_words_study_level(user_id, words, 'main_words')
    elif lang == 'rus':
        words = await rus.get_words_level(level)
        await study_words_user.update_words_study_level(user_id, words, 'main_words')

    await callback.answer(text=text.change.format(level=level))
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboard.menu(user_id))


@router.callback_query(F.data == 'back_to_settings')
async def back_to_settings(callback):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboard.settings())


@router.callback_query(F.data == 'back')
async def back(callback, state):
    await state.clear()
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboard.menu(user_id))


@router.callback_query(F.data == 'info_level')
async def level_info_(callback, bot):
    user_id = callback.from_user.id
    info = await study_words_user.get_percent_of_level(user_id)
    text, keyboard = await text_and_keyboard(user_id)
    level = await users.get_level(user_id)
    lang = await users.get_learn_lang(user_id)
    theme = await users.get_theme(user_id)
    if level < 'B1':
        await callback.message.edit_text(text=text.level_info[theme][lang].format(level=level, num=info),
                                         reply_markup=keyboard.back())
    else:
        if theme == 'main_words':
            await callback.message.edit_text(text=text.level_info[theme].format(level=level, num=info),
                                             reply_markup=keyboard.back())
        else:
            await callback.message.edit_text(text=text.level_info[theme].format(num=info),
                                             reply_markup=keyboard.back())


@router.callback_query(F.data == 'settings')
async def settings(callback):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboard.settings())

# CHANGE LEVEL
@router.callback_query(F.data == 'change_level')
async def change_level(callback):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboard.change_level())


@router.callback_query(F.data == 'up_level')
async def up_level(callback):
    user_id = callback.from_user.id
    lang = await users.get_learn_lang(user_id)
    level = await users.get_level(user_id)
    if level in ('C1',):
        await callback.answer(text=texts[lang].maximum)
        await callback.message.edit_text(text=texts[lang].menu,
                                         reply_markup=keyboards[lang].menu())
    else:
        await users.increase_level(user_id)
        text, keyboard = await text_and_keyboard(user_id)
        level = await users.get_level(user_id)
        if lang == 'en':
            words = await en.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        elif lang == 'es':
            words = await es.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        elif lang == 'fr':
            words = await fr.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        elif lang == 'it':
            words = await it.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        elif lang == 'de':
            words = await de.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        elif lang == 'rus':
            words = await rus.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        await callback.answer(text=text.raised.format(level=level))
        await callback.message.edit_text(text=text.menu,
                                         reply_markup=keyboard.menu(user_id))


@router.callback_query(F.data == 'down_level')
async def down_level(callback):
    user_id = callback.from_user.id
    lang = await users.get_learn_lang(user_id)
    level = await users.get_level(user_id)
    native = await users.get_native_lang(user_id)
    if level in ('A1',):
        await callback.answer(text=texts[native].minimum)
        await callback.message.edit_text(text=texts[native].menu,
                                         reply_markup=keyboards[native].menu())
    else:
        await users.reduce_level(user_id)
        level = await users.get_level(user_id)
        text, keyboard = await text_and_keyboard(user_id)

        if lang == 'en':
            words = await en.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        elif lang == 'es':
            words = await es.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        elif lang == 'fr':
            words = await fr.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        elif lang == 'it':
            words = await it.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        elif lang == 'de':
            words = await de.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        elif lang == 'rus':
            words = await rus.get_words_level(level)
            await study_words_user.update_words_study_level(user_id, words, 'main_words')
        await callback.answer(text=text.lowered.format(level=level))
        await callback.message.edit_text(text=text.menu,
                                         reply_markup=keyboard.menu(user_id))


@router.callback_query(F.data == 'update_quantity_words')
async def update_quantity_words(callback, bot, state: FSMContext):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await callback.message.edit_text(text=text.range_learn_words)
    await users.update_menu_id(user_id)
    await state.set_state(New_quantity_words.quantity_words)
    await callback.answer()


@router.message(New_quantity_words.quantity_words)
async def new_quantity_words(msg, state: FSMContext, bot):
    user_id = msg.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    if msg.text.isdigit() and await valid_msg_text(msg.text) and 4 < int(msg.text) < 31:
        user_id = msg.from_user.id
        await state.clear()
        await users.new_quantity_words(user_id, int(msg.text))
        await bot.send_message(chat_id=user_id,
                               text=text.successfully)
        menu = await bot.send_message(chat_id=user_id,
                                      text=text.menu,
                                      reply_markup=keyboard.menu(user_id))
        await users.update_menu_id(user_id, menu.message_id)
    else:
        await msg.answer(text=text.range_learn_words_2)

# MY DICTIONARY
@router.callback_query(F.data == 'my_dict')
async def my_dict(callback):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboard.my_dict())


@router.callback_query(F.data == 'print_my_words')
async def print_my_words(callback, bot, state: FSMContext):
    user_id = callback.from_user.id
    words = await db.UsersDicts.get_words(user_id)
    text, keyboard = await text_and_keyboard(user_id)

    if words:
        await callback.message.edit_text(text=text.your_words + words)
    else:
        await callback.message.edit_text(text=text.empty_dict)

    menu = await bot.send_message(chat_id=user_id,
                                  text=text.menu,
                                  reply_markup=keyboard.menu(user_id))
    await users.update_menu_id(user_id, menu.message_id)


@router.callback_query(F.data == 'learn_my_words')
async def learn_my_words(callback, bot, state: FSMContext):
    user_id = callback.from_user.id
    words = await db.UsersDicts.get_words(user_id)
    await callback.answer()
    text, keyboard = await text_and_keyboard(user_id)

    if words:
        await study_words_user.update_words_study_level(user_id, words, 'dict_words')
        await start_learn(callback, state, bot)
    else:
        await callback.message.edit_text(text=text.empty_dict)
        menu = await bot.send_message(chat_id=user_id,
                                      text=text.menu,
                                      reply_markup=keyboard.menu(user_id))
        await users.update_menu_id(user_id, menu.message_id)


@router.callback_query(F.data == 'add_word')
async def add_word(callback, bot, state: FSMContext):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    to_delete = await callback.message.edit_text(text=text.enter_u_word1)
    await state.update_data(to_delete=to_delete.message_id)
    await state.set_state(Mydict.en_word)


@router.message(Mydict.en_word)
async def en_word(msg, state: FSMContext, bot):
    user_id = msg.from_user.id
    text, keyboard = await text_and_keyboard(user_id)

    data = await state.get_data()
    await bot.delete_message(chat_id=user_id, message_id=data['to_delete'])
    en_word = msg.text
    await bot.delete_message(chat_id=user_id, message_id=msg.message_id)

    if await valid_msg_text(en_word):
        await state.set_state(Mydict.ru_word)
        to_delete = await bot.send_message(chat_id=user_id,
                                           text=text.enter_u_word2)
        await state.update_data(to_delete=to_delete.message_id,
                                en_word=en_word.lower())
    else:
        to_delete = await bot.send_message(chat_id=user_id,
                                           text=text.long_msg + '\n\n' + text.enter_u_word1)
        await state.update_data(to_delete=to_delete.message_id)
        await state.set_state(Mydict.en_word)


@router.message(Mydict.ru_word)
async def ru_word(msg, state: FSMContext, bot):
    user_id = msg.from_user.id
    text, keyboard = await text_and_keyboard(user_id)

    data = await state.get_data()
    await bot.delete_message(chat_id=user_id, message_id=data['to_delete'])
    ru_word = msg.text
    await bot.delete_message(chat_id=user_id, message_id=msg.message_id)

    if await valid_msg_text(ru_word):
        data = await state.get_data()
        await state.clear()
        word = data['en_word'] + ' – ' + ru_word.lower()
        await db.UsersDicts.add_word(user_id, word)
        await bot.send_message(chat_id=user_id,
                               text=text.enter_u_word3)
        menu = await bot.send_message(chat_id=user_id,
                                      text=text.menu,
                                      reply_markup=keyboard.menu(user_id))
        await users.update_menu_id(user_id, menu.message_id)
    else:
        to_delete = await bot.send_message(chat_id=user_id,
                                           text=text.long_msg + '\n\n' + text.enter_u_word2)
        await state.update_data(to_delete=to_delete.message_id)
        await state.set_state(Mydict.ru_word)

# THEMES
@router.callback_query(F.data == 'choose_theme')
async def settings(callback):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboard.choose_theme())


@router.callback_query(F.data == '5000')
async def l5000(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    lang = await users.get_learn_lang(user_id)
    text, keyboard = await text_and_keyboard(user_id)
    if lang == 'en':
        words = await en.get_words_level('5000')

    await study_words_user.update_words_study_level(user_id, words, '5000')
    await callback.answer(text=text.successfully)
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboard.menu(user_id))


@router.callback_query(F.data == 'agro')
async def agro(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    lang = await users.get_learn_lang(user_id)
    text, keyboard = await text_and_keyboard(user_id)
    if lang == 'en':
        words = await en.get_words_level('agro')

    await study_words_user.update_words_study_level(user_id, words, 'agro')
    await callback.answer(text=text.successfully)
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboard.menu(user_id))


@router.callback_query(F.data == 'cybersecurity')
async def cybersecurity(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    lang = await users.get_learn_lang(user_id)
    text, keyboard = await text_and_keyboard(user_id)
    if lang == 'en':
        words = await en.get_words_level('cybersecurity')

    await study_words_user.update_words_study_level(user_id, words, 'cybersecurity')
    await callback.answer(text=text.successfully)
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboard.menu(user_id))


@router.callback_query(F.data == 'IT')
async def IT(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    lang = await users.get_learn_lang(user_id)
    text, keyboard = await text_and_keyboard(user_id)
    if lang == 'en':
        words = await en.get_words_level('IT')

    await study_words_user.update_words_study_level(user_id, words, 'IT')
    await callback.answer(text=text.successfully)
    await callback.message.edit_text(text=text.menu,
                                     reply_markup=keyboard.menu(user_id))


@router.callback_query(F.data == 'сontinue_to_study_the_words')
async def continue_to_study_the_words(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    lang = await users.get_learn_lang(user_id)
    text, keyboard = await text_and_keyboard(user_id)
    level = await users.get_level(user_id)

    if lang == 'en':
        words = await en.get_words_level(level)
        await study_words_user.update_words_study_level(user_id, words, 'main_words')
        await callback.answer()
        await callback.message.edit_text(text=text.menu,
                                         reply_markup=keyboard.menu(user_id))
    elif lang == 'rus':
        words = await rus.get_words_level(level)
        await study_words_user.update_words_study_level(user_id, words, 'main_words')
        await callback.answer()
        await callback.message.edit_text(text=text.menu,
                                         reply_markup=keyboard.menu(user_id))
    elif lang == 'de':
        words = await de.get_words_level(level)
        await study_words_user.update_words_study_level(user_id, words, 'main_words')
        await callback.answer()
        await callback.message.edit_text(text=text.menu,
                                         reply_markup=keyboard.menu(user_id))
    elif lang == 'fr':
        words = await fr.get_words_level(level)
        await study_words_user.update_words_study_level(user_id, words, 'main_words')
        await callback.answer()
        await callback.message.edit_text(text=text.menu,
                                         reply_markup=keyboard.menu(user_id))
    elif lang == 'it':
        words = await it.get_words_level(level)
        await study_words_user.update_words_study_level(user_id, words, 'main_words')
        await callback.answer()
        await callback.message.edit_text(text=text.menu,
                                         reply_markup=keyboard.menu(user_id))
    elif lang == 'es':
        words = await es.get_words_level(level)
        await study_words_user.update_words_study_level(user_id, words, 'main_words')
        await callback.answer()
        await callback.message.edit_text(text=text.menu,
                                         reply_markup=keyboard.menu(user_id))


@router.callback_query(F.data == 'writing_skills')
async def writing_skills(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await callback.answer()
    await callback.message.edit_text(text=text.translate_text_6,
                                     reply_markup=keyboard.writing_skills())


@router.callback_query(F.data == 'essay')
async def essay1(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await callback.answer()
    await callback.message.edit_text(text=text.essay_1,
                                     reply_markup=keyboard.essay())


@router.callback_query(F.data == 'essay_start')
async def essay2(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    level = await users.get_level(user_id)
    await callback.answer()
    theme = await get_random_topic(level)
    await callback.message.edit_text(text=text.essay_2.format(theme=theme))
    await users.update_menu_id(user_id)
    await state.set_state(Essay.essay)


@router.message(Essay.essay)
async def essay3(msg: types.Message, state: FSMContext, bot):
    user_essay = msg.text
    user_id = msg.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    if len(user_essay) < 1001:
        # similar_info = await async_rag(user_essay)  # использовать в функциях где идет запрос к нейросети
        # if similar_info:
        #     await msg.answer("В эссе используются недопустимые слова/фразы. При их повторном употреблении Вы будете заблокированны.")
        #     await msg.answer(text=text.essay_3)
        #     await state.set_state(Essay.essay)
        #     return

        msg_to_delete = await msg.answer(text.translate_text_5)
        level = await users.get_level(user_id)
        lang = await users.get_learn_lang(user_id)
        lang_to_promt = {
            'es': 'Spanish',
            'en': 'English',
            'de': 'German',
            'fr': 'French',
            'it': 'Italian'
        }[lang]

        promt_to_essay = await get_promt_to_essay(level)

        messages = [
            {
                'role': 'user',
                'content': promt_to_essay.format(lang=lang_to_promt, essay_text=user_essay),
            }
        ]

        try:
            bot_reply = await request_to_AI(messages)
        except Exception as e:
            logger.error(f"🔴 Ошибка запроса к API bot_hub у пользователя {user_id}: {e}")
            await msg.answer('К сожалению не получилось обработать информацию. Попробуйте еще раз.')
            return

        messages_for_translate = [
            {"role": "system",
             "content": 'Ты проффесинальный переводчик, который легко определяет язык текста и переводит его на русский. Напиши только перевод и ничего больше.'},
            {"role": "user", "content": f'Переведи этот текст: {bot_reply}'}
        ]

        try:
            translate_text = await request_to_AI(messages_for_translate)
        except Exception as e:
            logger.error(f"🔴 Ошибка запроса к API bot_hub у пользователя {user_id}: {e}")
            await msg.answer('К сожалению не получилось обработать информацию. Попробуйте еще раз.')
            return

        if level > 'B1' and lang == 'en':
            try:
                # aura-2-andromeda-en, aura-2-thalia-en, aura-2-cordelia-en, aura-2-helena-en, aura-2-janus-en медленная, aura-2-odysseus-en, aura-2-orpheus-en хороший диктор
                audio_buffer = await deepgram_text_to_speech(bot_reply, "aura-2-janus-en")
            except Exception as e:
                logger.error(f"🔴 Ошибка запроса к API deepgram (озвучка текста) у пользователя {user_id}: {e}")
                audio_buffer = await text_to_speech(bot_reply, lang)
        else:
            audio_buffer = await text_to_speech(bot_reply, lang)

        if audio_buffer is None:
            logger.error(f"🔴 Ошибка запроса к API deepgram (озвучка текста) у пользователя {user_id}")
            audio_buffer = await text_to_speech(bot_reply, lang)

        audio_file = BufferedInputFile(file=audio_buffer.read(),
                                       filename="The voiced version of the feedback.mp3")

        await bot.delete_message(chat_id=msg.chat.id, message_id=msg_to_delete.message_id)
        unique_id = str(uuid.uuid4()).split('-')[0]
        feedback = await bot.send_message(chat_id=user_id,
                                          text=bot_reply,
                                          reply_markup=keyboard.show_translate_essay_feedback(unique_id))
        await msg.answer_audio(audio_file)
        menu = await bot.send_message(chat_id=user_id,
                                      text=text.menu,
                                      reply_markup=keyboard.menu(user_id))
        await users.update_menu_id(user_id, menu.message_id)
        await db.UsersTexts.add_user_text(user_id, unique_id, bot_reply, translate_text, feedback.message_id)
    else:
        await msg.answer(text=text.long_msg)
        await msg.answer(text=text.essay_3)
        await state.set_state(Essay.essay)


@router.callback_query(F.data.startswith('ste_'))
async def listening_6(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    unique_id = callback.data.split("_")[-1]
    bot_reply, translate_text, feedback = await db.UsersTexts.get_translation(user_id, unique_id)

    await callback.answer()
    await bot.edit_message_text(chat_id=user_id,
                                message_id=feedback,
                                text=bot_reply)

    delete_menu = await users.get_menu_id(user_id)
    if delete_menu:
        await bot.delete_message(chat_id=user_id, message_id=delete_menu)

    await bot.send_message(chat_id=user_id,
                           text=translate_text)

    menu = await bot.send_message(chat_id=user_id,
                                  text=text.menu,
                                  reply_markup=keyboard.menu(user_id))
    await users.update_menu_id(user_id, menu.message_id)
    await state.clear()

# TRANSLATE THE TEXT
@router.callback_query(F.data == 'translate_text')
async def translate_text_1_(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await callback.answer()
    await callback.message.edit_text(text=text.translate_text_1,
                                     reply_markup=keyboard.text_symbols())


@router.callback_query(F.data.startswith('symbols_'))
async def translate_text_2_(callback, state: FSMContext, bot):
    number_of_characters = int(callback.data.split("_")[-1])
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await state.update_data(number_of_characters=number_of_characters)
    await state.set_state(Translate_text.theme)
    await callback.message.edit_text(text=text.translate_text_2)
    await users.update_menu_id(user_id)


@router.message(Translate_text.theme)
async def translate_text_3_(msg: types.Message, state: FSMContext, bot):
    user_id = msg.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    text_user = msg.text
    if await valid_msg_text(text_user):
        # similar_info = await async_rag(text_user)  # использовать в функциях где идет запрос к нейросети
        # if similar_info:
        #     await msg.answer("В запросе используются недопустимые слова/фразы. При их повторном употреблении Вы будете заблокированны.")
        #     await msg.answer(text=text.translate_text_2)
        #     await state.set_state(Translate_text.theme)
        #     return

        await state.update_data(theme=text_user)
        msg_to_delete = await msg.answer(text.translate_text_4)
        data = await state.get_data()
        level = await users.get_level(user_id)
        lang = await users.get_learn_lang(user_id)
        lang_to_promt = {
            'es': 'Spanish',
            'en': 'English',
            'de': 'German',
            'fr': 'French',
            'it': 'Italian'
        }[lang]

        system_prompt = """
        You are a highly experienced {lang_to_promt} teacher at Harvard University,
        with 40 years of experience teaching foreign language learners.
        Your specialty is creating natural, engaging, and educationally valuable texts
        at the {level} level of the CEFR for students.
        Your writing is clear, grammatically accurate, and includes useful vocabulary
        in context, but avoids unnecessary complexity.
        You never add explanations, comments, formatting, or meta-text —
        only a plain title (without 'Title:' or markdown) followed by a coherent text.
        Ensure the total length is approximately {number_of_characters} characters,
        including spaces. Do not mention the character count in the response.
        """
        user_promt = """
        Write a text in {lang_to_promt} at {level} level on the topic: {theme}.
        The text should be around {number_of_characters} characters long,
        natural, educational, and suitable for language learners.
        Only return the title (without formatting) and the text — nothing else.
        """
        messages = [
            {'role': 'system',
             'content': system_prompt.format(lang_to_promt=lang_to_promt,
                                            level=level,
                                            number_of_characters=data['number_of_characters'])},
            {
                'role': 'user',
                'content': user_promt.format(lang_to_promt=lang_to_promt,
                                             level=level,
                                             theme=data['theme'],
                                             number_of_characters=data['number_of_characters']),
            }
        ]

        try:
            bot_reply = await request_to_AI(messages)
        except Exception as e:
            logger.error(f"🔴 Ошибка запроса к API bot_hub у пользователя {user_id}: {e}")
            await msg.answer('К сожалению не получилось обработать информацию. Попробуйте еще раз.')
            return

        if level > 'B1' and lang == 'en':
            try:
                audio_buffer = await deepgram_text_to_speech(bot_reply, "aura-2-janus-en")
            except Exception as e:
                logger.error(f"🔴 Ошибка запроса к API deepgram (озвучка текста) у пользователя {user_id}: {e}")
                audio_buffer = await text_to_speech(bot_reply, lang)
        else:
            audio_buffer = await text_to_speech(bot_reply, lang)

        if audio_buffer is None:
            logger.error(f"🔴 Ошибка запроса к API deepgram (озвучка текста) у пользователя {user_id}")
            audio_buffer = await text_to_speech(bot_reply, lang)

        audio_file = BufferedInputFile(file=audio_buffer.read(),
                                       filename="The voiced version of the text.mp3")

        await state.update_data(text=bot_reply)
        await bot.delete_message(chat_id=msg.chat.id, message_id=msg_to_delete.message_id)
        await bot.send_message(chat_id=user_id,
                               text=bot_reply)
        await msg.answer_audio(audio_file)
        await msg.answer(text.translate_text_3)
        await state.set_state(Translate_text.translate)
    else:
        await msg.answer(text=text.long_msg)
        await msg.answer(text=text.translate_text_2)
        await state.set_state(Translate_text.theme)


@router.message(Translate_text.translate)
async def translate_text_4_(msg, state: FSMContext, bot):
    await state.update_data(translate=msg.text)
    user_id = msg.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    msg_to_delete = await msg.answer(text.translate_text_5)
    data = await state.get_data()
    await state.clear()
    level = await users.get_level(user_id)
    lang = await users.get_learn_lang(user_id)
    lang_to_promt = {'es': 'испанского',
                     'en': 'английского',
                     'de': 'немецкого',
                     'fr': 'французского',
                     'it': 'итальянского'
                     }[lang]
    lang_to_promt_1 = {'es': 'испанском',
                       'en': 'английском',
                       'de': 'немецком',
                       'fr': 'французском',
                       'it': 'итальянском'
                       }[lang]
    # Old
    # messages = [
    #     {'role': 'system',
    #      'content': f'Ты — учитель {lang_to_promt} языка Гарварда с 40 летним стажем. Который помогает пользователям с лексикой.'},
    #     {
    #         'role': 'user',
    #         'content': f"Оригинальный текст на {lang_to_promt_1} языке: \"{data['text']}\".\nПользовательский перевод: \"{data['translate']}\".\n\nПроверь этот перевод на точность. Укажи:\n- Что является правильным\n- Что нуждается в улучшении\n- Правильный перевод\n\nБез дополнительных вопросов и уточнений.",
    #     }
    # ]
    # New
    system_prompt = """
            Вы — опытный преподаватель {lang_to_promt} языка в Гарварде с 40-летним стажем.
            Вы специализируетесь на обучении студентов уровня {level} по шкале CEFR.
            Вы даёте чёткую, структурированную и образовательную обратную связь на русском языке.
            Вы никогда не задаёте вопросов и не добавляете лишних комментариев — только анализ перевода.
            """
    user_promt = """
            Оригинальный текст на {lang_to_promt} языке: \"{text}\"
            Перевод пользователя: \"{translate}\"
            "Проанализируйте перевод и предоставьте обратную связь на русском языке в следующем формате:
            1. ✅ Что переведено верно
               - Укажите части перевода, которые точны и естественны.
            2. ⚠️ Что можно улучшить
               - Найдите ошибки: грамматические, лексические, стилистические или по смыслу.
               - Для каждой укажите, что не так и почему.
            3. ✅ Улучшенный перевод
               - Приведите исправленный, естественный и соответствующий уровню {level} вариант перевода.
               - Перевод должен быть понятным и звучать как речь носителя.
            Не добавляйте вступлений, вопросов или дополнительных замечаний. Только три указанных пункта.
            """
    messages = [
        {'role': 'system',
         'content': system_prompt.format(lang_to_promt=lang_to_promt,
                                         level=level)},
        {
            'role': 'user',
            'content': user_promt.format(lang_to_promt=lang_to_promt,
                                         text=data['text'],
                                         translate=data['translate'],
                                         level=level),
        }
    ]

    try:
        bot_reply = await request_to_AI(messages)
    except Exception as e:
        logger.error(f"🔴 Ошибка запроса к API bot_hub у пользователя {user_id}: {e}")
        await msg.answer('К сожалению не получилось обработать информацию. Попробуйте еще раз.')
        return

    await bot.delete_message(chat_id=msg.chat.id, message_id=msg_to_delete.message_id)
    await bot.send_message(chat_id=user_id,
                           text=bot_reply)
    menu = await bot.send_message(chat_id=user_id,
                                  text=text.menu,
                                  reply_markup=keyboard.menu(user_id))
    await users.update_menu_id(user_id, menu.message_id)

# LISTENING
@router.callback_query(F.data == 'audio')
async def LISTENING_1(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await callback.message.edit_text(text=text.listening_2,
                                     reply_markup=keyboard.listening())


@router.callback_query(F.data == 'audio_theme')
async def LISTENING_2(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    await state.set_state(Listening_skills.theme)
    await callback.message.edit_text(text=text.listening_3)
    await users.update_menu_id(user_id)


@router.message(Listening_skills.theme)
async def LISTENING_3(msg: types.Message, state: FSMContext, bot):
    text_user = msg.text
    user_id = msg.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    if await valid_msg_text(text_user):
        # similar_info = await async_rag(text_user)  # использовать в функциях где идет запрос к нейросети
        # if similar_info:
        #     await msg.answer("В запросе используются недопустимые слова/фразы. При их повторном употреблении Вы будете заблокированны.")
        #     await msg.answer(text=text.listening_3)
        #     await state.set_state(Listening_skills.theme)
        #     return

        await state.update_data(theme=text_user)
        msg_to_delete = await msg.answer(text.listening_1)
        data = await state.get_data()
        level = await users.get_level(user_id)
        lang = await users.get_learn_lang(user_id)
        lang_to_promt = {
            'es': 'Spanish',
            'en': 'English',
            'de': 'German',
            'fr': 'French',
            'it': 'Italian'
        }[lang]

        characters = {
            'A1': '(A1 level on the CEFR scale, around 200–300 characters)',
            'A2': '(A2 level on the CEFR scale, around 400–600 characters)',
            'B1': '(B1 level on the CEFR scale, around 800–1000 characters)',
            'B2': '(B2 level on the CEFR scale, around 1200–1500 characters)',
            'C1': '(C1 level on the CEFR scale, around 1600–2000 characters)'
                      }[level]

        questions = {
            'A1': 3,
            'A2': 5,
            'B1': 7,
            'B2': 10,
            'C1': 12
                      }[level]

        output_format = '''
        {
          "text": "generated text",
          "questions": [
            {
              "question": "Question text",
              "options": ["Option A", "Option B", "Option C"],
              "correct": 0
            }
          ]
        }
        '''

        prompt = f"""
        Generate a listening text in {lang_to_promt} {characters} about the topic: "{msg.text}", make it natural and educational.

        Then create exactly {questions} multiple-choice questions with 3 options each.
        Make sure that the correct answer is randomly placed among the options, not always first or last.

        Return everything strictly in JSON format like this:
        {output_format}

        Do NOT include any additional explanation, markdown formatting, or starting lines like ```json.
        Only output the raw JSON without extra text.
        """
        messages = [
            {"role": "system", "content": f"You are a Harvard {lang_to_promt} teacher with 40 years of experience. Your task is to generate a text for listening and a set of questions about it."},
            {"role": "user", "content": prompt}
        ]

        try:
            bot_reply = await request_to_AI(messages)
        except Exception as e:
            logger.error(f"🔴 Ошибка запроса к API bot_hub у пользователя {user_id}: {e}")
            await msg.answer('К сожалению не получилось обработать информацию. Попробуйте еще раз.')
            return

        try:
            data = json.loads(bot_reply)
        except Exception as e:
            logger.error(f"🔴 Ошибка обрабокти json от нейросети на bot_hub у пользователя {user_id}: {e}")
            try:
                bot_reply = await request_to_AI(messages)
                data = json.loads(bot_reply)
            except Exception as e:
                logger.error(f"🔴 Ошибка обрабокти json от нейросети на bot_hub у пользователя {user_id}: {e}")
                await bot.delete_message(chat_id=msg.chat.id, message_id=msg_to_delete.message_id)
                await msg.answer(text=text.sww)
                menu = await bot.send_message(chat_id=user_id,
                                              text=text.menu,
                                              reply_markup=keyboard.menu(user_id))
                await users.update_menu_id(user_id, menu.message_id)
                return

        text_for_listening = data['text']
        questions = data['questions']

        messages_for_translate = [
            {"role": "system",
             "content": 'Ты проффесинальный переводчик, который легко определяет язык текста и переводит его на русский. Напиши только перевод и ничего больше.'},
            {"role": "user", "content": f'Переведи этот текст: {text_for_listening}'}
        ]

        try:
            translate_text = await request_to_AI(messages_for_translate)
        except Exception as e:
            logger.error(f"🔴 Ошибка запроса к API bot_hub у пользователя {user_id}: {e}")
            await msg.answer('К сожалению не получилось обработать информацию. Попробуйте еще раз.')
            return

        if level > 'B1' and lang == 'en':
            # aura-2-andromeda-en, aura-2-thalia-en, aura-2-cordelia-en, aura-2-helena-en, aura-2-janus-en медленная, aura-2-odysseus-en, aura-2-orpheus-en хороший диктор
            try:
                audio_buffer = await deepgram_text_to_speech(text_for_listening, "aura-2-janus-en")
            except Exception as e:
                logger.error(f"🔴 Ошибка запроса к API deepgram (озвучка текста) у пользователя {user_id}: {e}")
                audio_buffer = await text_to_speech(text_for_listening, lang)
        else:
            audio_buffer = await text_to_speech(text_for_listening, lang)

        if audio_buffer is None:
            logger.error(f"🔴 Ошибка запроса к API deepgram (озвучка текста) у пользователя {user_id}")
            audio_buffer = await text_to_speech(text_for_listening, lang)

        audio_file = BufferedInputFile(file=audio_buffer.read(),
                                       filename="The voiced version of the text.mp3")

        await state.update_data(text_for_listening=text_for_listening,
                                translate_text_listening=translate_text,
                                questions=questions,
                                idx=0)

        await bot.delete_message(chat_id=msg.chat.id, message_id=msg_to_delete.message_id)
        await msg.answer_audio(audio_file)
        exercise = await msg.answer(text=text.listening_4,
                                    reply_markup=keyboard.listening_test())

        unique_id = str(uuid.uuid4()).split('-')[0]
        await state.update_data(exercise_listening=exercise.message_id,
                                unique_id_listening=unique_id)

        await db.UsersTexts.add_user_text(user_id, unique_id, text_for_listening, translate_text, exercise.message_id)
    else:
        await msg.answer(text=text.long_msg)
        await msg.answer(text=text.listening_3)
        await state.set_state(Listening_skills.theme)


@router.callback_query(F.data == 'audio_test')
async def listening_55(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    await callback.answer()
    await listening_test(user_id, state, bot)


@router.callback_query(F.data.startswith('stl_'))
async def listening_6(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    unique_id = callback.data.split("_")[-1]
    text_for_listening, translate_text_listening, exercise_listening = await db.UsersTexts.get_translation(user_id, unique_id)

    await callback.answer()
    await bot.edit_message_text(chat_id=user_id,
                                message_id=exercise_listening,
                                text=text.listening_5 + text_for_listening + '\n\n' + translate_text_listening)


async def listening_test(user_id, state, bot):
    text, keyboard = await text_and_keyboard(user_id)

    data = await state.get_data()
    idx = data['idx']
    questions = data['questions']
    if idx == len(questions):
        await bot.edit_message_text(chat_id=user_id,
                                    message_id=data['exercise_listening'],
                                    text=text.listening_5 + data['text_for_listening'],
                                    reply_markup=keyboard.show_translate_listening(data['unique_id_listening']))
        menu = await bot.send_message(chat_id=user_id,
                                      text=text.menu,
                                      reply_markup=keyboard.menu(user_id))
        await users.update_menu_id(user_id, menu.message_id)
        await state.clear()
        return

    question = questions[idx]
    correct = question['correct']
    builder = InlineKeyboardBuilder()
    for i, option in enumerate(question['options']):
        builder.add(InlineKeyboardButton(
            text=option,
            callback_data=f"Listening_{correct}_{i}"
        ))
    builder.adjust(1)

    await bot.edit_message_text(chat_id=user_id,
                                message_id=data['exercise_listening'],
                                text=question['question'],
                                reply_markup=builder.as_markup())


@router.callback_query(F.data.startswith('Listening_'))
async def exercise_listening(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)

    _, correct, answer = callback.data.split("_")
    data = await state.get_data()
    if correct == answer:
        await callback.answer(r.choice(text.good_attempt))
        await state.update_data(idx=data['idx'] + 1)
        await listening_test(user_id, state, bot)
    else:
        builder = InlineKeyboardBuilder()
        buttons = callback.message.reply_markup.inline_keyboard
        for row in buttons:
            for button in row:
                if button.callback_data == callback.data:
                    builder.add(InlineKeyboardButton(
                        text=f"❌ {button.text}",
                        callback_data="none"
                    ))
                else:
                    builder.add(InlineKeyboardButton(
                        text=button.text,
                        callback_data=button.callback_data
                    ))
            builder.adjust(1)

        question = data['questions'][data['idx']]['question']
        await bot.edit_message_text(
            chat_id=user_id,
            message_id=data['exercise_listening'],
            text=question,
            reply_markup=builder.as_markup()
        )
        await callback.answer(r.choice(text.bad_attempt))

# LEARNING THE WORDS
@router.callback_query(F.data == 'start_learn')
async def start_learn(callback, state: FSMContext, bot):
    await state.update_data(start_learn=True)
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    words = await study_words_user.get_words(user_id)
    await users.update_menu_id(user_id)
    await callback.answer()
    await callback.message.delete()
    if not words:
        await bot.send_message(chat_id=user_id,
                               text=text.all_words_learned)
        menu = await bot.send_message(chat_id=user_id,
                               text=text.menu,
                               reply_markup=keyboard.menu(user_id))
        await users.update_menu_id(user_id, menu.message_id)
        return

    quantity = await users.get_quantity_words(user_id)
    selected_words = r.sample(words, min(quantity, len(words)))
    await state.update_data(remaining=len(selected_words))

    if len(words) <= quantity:
        await bot.send_message(chat_id=user_id,
                               text=text.all_words_learned_0)
        await state.update_data(end_of_level_or_theme=True)

    for pair in selected_words:
        word, translate = pair.split(' – ', maxsplit=1)
        await bot.send_message(
            chat_id=user_id,
            text=text.translates.format(word=word, translate=translate),
            reply_markup=keyboard.word())


@router.callback_query(F.data == 'know')
async def know(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)

    data = await state.get_data()
    if not data:
        await callback.message.delete()
        return

    end_of_level_or_theme = data.get('end_of_level_or_theme', False)
    remaining = data['remaining']

    word = ' – '.join(callback.message.text.split(text.word_split))
    await study_words_user.add_learnt_word(user_id, word)
    await callback.message.delete()

    if end_of_level_or_theme:
        remaining -= 1
        if not remaining:
            if data.get('words', 0):
                await starting_learn_words_1(data['words'], user_id, bot, state)
            else:
                await state.clear()
                await bot.send_message(chat_id=user_id,
                                       text=text.all_words_learned)
                await bot.send_message(chat_id=user_id,
                                       text=text.menu,
                                       reply_markup=keyboard.menu(user_id))
    else:
        words = await study_words_user.get_words(user_id)
        if not words:
            await state.update_data(end_of_level_or_theme=True,
                                    remaining=remaining - 1)
        else:
            word, translate = r.choice(words).split(' – ', maxsplit=1)
            await bot.send_message(chat_id=user_id,
                                       text=text.translates.format(word=word, translate=translate),
                                       reply_markup=keyboard.word())


@router.callback_query(F.data == 'learn_word')
async def learn_word(callback, state: FSMContext, bot):
    await callback.message.delete()
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    level = await users.get_level(user_id)

    data = await state.get_data()
    if not data:
        return

    word = ' – '.join(callback.message.text.split(text.word_split))
    words = data.get('words', [])
    words.append(word)
    await state.update_data(remaining=data['remaining'] - 1,
                            words=words)
    data = await state.get_data()
    if not data['remaining']:
        lang = await users.get_learn_lang(user_id)

        r.shuffle(words)
        en_words = [part.split(' [')[0] for part in [part.split(' – ')[0] for part in words]]

        # if level > 'B1' and lang == 'en':
        #     # aura-2-andromeda-en, aura-2-thalia-en, aura-2-cordelia-en, aura-2-helena-en, aura-2-janus-en медленная, aura-2-odysseus-en, aura-2-orpheus-en хороший диктор
        #     audio_buffer = await deepgram_text_to_speech(', '.join(en_words), "aura-2-orpheus-en")
        # else:
        #     audio_buffer = await text_to_speech(', '.join(en_words), lang)

        audio_buffer = await text_to_speech('. '.join(en_words), lang)
        audio_file = BufferedInputFile(file=audio_buffer.read(), filename="Words.mp3")

        msg_to_hide = await bot.send_message(chat_id=user_id,
                                             text=text.words + "\n\n" + "\n".join(words) + "\n\n" + text.words_)
                                             # text=text.words + f"\n\n{'\n'.join(words)}\n\n" + text.words_)
        if '[' in words[0]:
            words = [part.split(' [')[0] + ' – ' + part.split(' – ')[1] for part in words]

        await bot.send_audio(chat_id=user_id,
                             audio=audio_file)

        to_delete_button = await bot.send_message(chat_id=user_id,
                                          text=text.ready_learn,
                                          reply_markup=keyboard.ready_learn())
        await state.update_data(words=words,
                                msg_to_hide=msg_to_hide.message_id,
                                to_delete_button=to_delete_button.message_id)


@router.callback_query(F.data == 'ex_to_learn')
async def learn_word(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)

    data = await state.get_data()
    await bot.edit_message_text(chat_id=user_id,
                                message_id=data['msg_to_hide'],
                                text=text.words + f"\n\n. . .\n??? 🫥\n. . .\n\n" + text.words_)
    await state.update_data(idx=0,
                            timer=0)
    await starting_learn_words_1(data['words'], user_id, bot, state, True)

# LESSONS
async def build_answer_keyboard(options, tried_answers, selected_index, exercise):
    builder = InlineKeyboardBuilder()

    for i, option in enumerate(options):
        if i == selected_index:
            builder.add(InlineKeyboardButton(
                text=f"❌ {option}",
                callback_data="none"
            ))
        elif option in tried_answers:
            builder.add(InlineKeyboardButton(
                text=f"❌ {option}",
                callback_data="none"
            ))
        else:
            builder.add(InlineKeyboardButton(
                text=option,
                callback_data=f"Exercise{exercise}_{i}"
            ))

    builder.adjust(1)
    return builder.as_markup()


async def starting_learn_words_1(words, user_id, bot, state, first_msg=False):
    text, keyboard = await text_and_keyboard(user_id)
    data = await state.get_data()
    idx = data['idx']
    if idx == len(words):
        await state.update_data(idx=0)
        await starting_learn_words_2(words, user_id, bot, state)
        return

    word, translation = words[idx].split(' – ')
    wrong_options = r.sample([w.split(' – ')[1] for w in (words[:idx] + words[idx + 1:])], k=3)

    options = [translation] + wrong_options
    r.shuffle(options)

    await state.update_data(current_word=word,
                            current_translation=translation,
                            current_options=options)

    builder = InlineKeyboardBuilder()
    for i, option in enumerate(options):
        builder.add(InlineKeyboardButton(
            text=option,
            callback_data=f"Exercise1_{i}"
        ))
    builder.adjust(1)

    if first_msg:
        exercise = await bot.send_message(chat_id=user_id,
                                          text=text.Exercise_1 + f"\n\n{word} - ?",
                                          reply_markup=builder.as_markup())
        await state.update_data(exercise=exercise.message_id)
        try:
            await bot.delete_message(chat_id=user_id,
                                     message_id=data['to_delete_button'])
        except Exception as e:
            logger.error(f"🔴 Ошибка {e} при удалении сообщения у пользователя: {user_id}")
            await bot.edit_message_text(chat_id=user_id,
                                        message_id=data['to_delete_button'],
                                        text='😎')
    else:
        await bot.edit_message_text(chat_id=user_id,
                                    message_id=data['exercise'],
                                    text=text.Exercise_1 + f"\n\n{word} - ?",
                                    reply_markup=builder.as_markup())


@router.callback_query(F.data.startswith('Exercise1_'))
async def exercise_1(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)

    selected_index = int(callback.data.split('_')[-1])
    data = await state.get_data()

    word = data['current_word']
    correct_answer = data['current_translation']
    options = data['current_options']

    selected_option = options[selected_index]
    is_correct = selected_option == correct_answer

    tried_answers = data.get("tried_answers", [])

    if is_correct:
        tried_answers.clear()
        await callback.answer(r.choice(text.good_attempt))
        await state.update_data(idx=data['idx'] + 1,
                                tried_answers=[])
        await starting_learn_words_1(data['words'], user_id, bot, state)
    else:
        if selected_option not in tried_answers:
            tried_answers.append(selected_option)
            await state.update_data(tried_answers=tried_answers)

        reply_markup = await build_answer_keyboard(options, tried_answers, selected_index, 1)

        await bot.edit_message_text(
            chat_id=user_id,
            message_id=data['exercise'],
            text=text.wrong_ans + f"{word} - ?",
            reply_markup=reply_markup
        )
        await callback.answer(r.choice(text.bad_attempt))


async def starting_learn_words_2(words, user_id, bot, state):
    text, keyboard = await text_and_keyboard(user_id)
    data = await state.get_data()
    idx = data['idx']
    if idx == len(words):
        await state.update_data(idx=0)
        await starting_learn_words_3(words, user_id, bot, state)
        return

    word, translation = words[idx].split(' – ')
    wrong_options = r.sample([w.split(' – ')[0] for w in (words[:idx] + words[idx + 1:])], k=3)

    options = [word] + wrong_options
    r.shuffle(options)

    await state.update_data(current_word=word,
                            current_translation=translation,
                            current_options=options)

    builder = InlineKeyboardBuilder()
    for i, option in enumerate(options):
        builder.add(InlineKeyboardButton(
            text=option,
            callback_data=f"Exercise2_{i}"
        ))
    builder.adjust(1)

    await bot.edit_message_text(chat_id=user_id,
                                message_id=data['exercise'],
                                text=text.Exercise_2 + f"\n\n{translation} - ?",
                                reply_markup=builder.as_markup())


@router.callback_query(F.data.startswith('Exercise2_'))
async def exercise_1(callback, state: FSMContext, bot):
    user_id = callback.from_user.id
    text, keyboard = await text_and_keyboard(user_id)

    selected_index = int(callback.data.split('_')[-1])
    data = await state.get_data()

    word = data['current_translation']
    correct_answer = data['current_word']
    options = data['current_options']

    selected_option = options[selected_index]
    is_correct = selected_option == correct_answer

    tried_answers = data.get("tried_answers", [])

    if is_correct:
        tried_answers.clear()
        await callback.answer(r.choice(text.good_attempt))
        await state.update_data(idx=data['idx'] + 1,
                                tried_answers=[])
        await starting_learn_words_2(data['words'], user_id, bot, state)
    else:
        if selected_option not in tried_answers:
            tried_answers.append(selected_option)
            await state.update_data(tried_answers=tried_answers)

        reply_markup = await build_answer_keyboard(options, tried_answers, selected_index, 2)

        await bot.edit_message_text(
            chat_id=user_id,
            message_id=data['exercise'],
            text=text.wrong_ans + f"{word} - ?",
            reply_markup=reply_markup
        )
        await callback.answer(r.choice(text.bad_attempt))


async def starting_learn_words_3(words, user_id, bot, state):
    text, keyboard = await text_and_keyboard(user_id)
    data = await state.get_data()
    idx = data['idx']
    if idx == len(words):
        await state.clear()
        await bot.delete_message(chat_id=user_id, message_id=data['exercise'])
        timer = data['timer']
        timer += 1
        if timer > 4:
            await bot.send_message(chat_id=user_id,
                                   text=text.Congratulations)
            menu = await bot.send_message(chat_id=user_id,
                                          text=text.menu,
                                          reply_markup=keyboard.menu(user_id))
            await users.update_menu_id(user_id, menu.message_id)
            await study_words_user.add_learnt_word(user_id, '\n'.join(words))
            await db.UsersWords.delete_info(user_id, data['unique_id'])
        else:
            if timer == 1:
                to_delete_please_wait = await bot.send_message(chat_id=user_id,
                                                               text=text.please_wait)
                level = await users.get_level(user_id)
                lang = await users.get_learn_lang(user_id)
                lang_to_promt = {'es': 'испанского',
                                 'en': 'английского',
                                 'de': 'немецкого',
                                 'fr': 'французского',
                                 'it': 'итальянского'
                                 }[lang]
                lang_to_promt_1 = {'es': 'испанском',
                                   'en': 'английском',
                                   'de': 'немецком',
                                   'fr': 'французском',
                                   'it': 'итальянском'
                                   }[lang]

                en_words = [part.split(' – ')[0] for part in words]
                messages = [
                    {'role': 'system',
                     'content': f'Ты — учитель {lang_to_promt} языка Гарварда с 40 летним стажем. Который помогает пользователям с лексикой.'},
                    {
                        'role': 'user',
                        'content': f"Напиши по одной фразе использования слова из списка {en_words} на {lang_to_promt_1} языке если бы твой уровень владения языком был бы {level}. Напиши только номер фразы, фразу и через дефис перевод на русский язык, без лишних слов и выделений слов. Дефис используй только для разделения фразы и ее перевода, не в словах. Пример: 1. Фраза. – Перевод.",
                    }
                ]

                try:
                    bot_reply = await request_to_AI(messages)
                except Exception as e:
                    logger.error(f"🔴 Ошибка запроса к API bot_hub у пользователя {user_id}: {e}")
                    await msg.answer('К сожалению не получилось обработать информацию. Попробуйте еще раз.')
                    return

                t = '\n'.join([part.split('–')[0] for part in bot_reply.split('\n')])

                if level > 'B1' and lang == 'en':
                    # aura-2-andromeda-en, aura-2-thalia-en, aura-2-cordelia-en, aura-2-helena-en, aura-2-janus-en медленная, aura-2-odysseus-en, aura-2-orpheus-en хороший диктор
                    try:
                        audio_buffer = await deepgram_text_to_speech(t, "aura-2-janus-en")
                    except Exception as e:
                        logger.error(f"🔴 Ошибка запроса к API deepgram (озвучка текста) у пользователя {user_id}: {e}")
                        audio_buffer = await text_to_speech(t, lang)
                else:
                    audio_buffer = await text_to_speech(t, lang)

                if audio_buffer is None:
                    logger.error(f"🔴 Ошибка запроса к API deepgram (озвучка текста) у пользователя {user_id}")
                    audio_buffer = await text_to_speech(t, lang)

                audio_file = BufferedInputFile(file=audio_buffer.read(),
                                               filename="Examples of the use of learned words.mp3")

                await bot.delete_message(chat_id=user_id, message_id=to_delete_please_wait.message_id)

                await bot.send_message(chat_id=user_id,
                                       text=text.words_1 + f"\n\n{bot_reply}")
                await bot.send_audio(chat_id=user_id,
                                     audio=audio_file)
                await bot.edit_message_text(chat_id=user_id,
                                            message_id=data['msg_to_hide'],
                                            text=text.words + "\n\n" + "\n".join(words) + "\n\n" + text.words_)
                                            # text=text.words + f"\n\n{'\n'.join(words)}\n\n" + text.words_)

            await bot.send_message(chat_id=user_id,
                                   text=text.reminder)
            menu = await bot.send_message(chat_id=user_id,
                                          text=text.menu,
                                          reply_markup=keyboard.menu(user_id))
            await users.update_menu_id(user_id, menu.message_id)

            if timer == 1:
                unique_id = str(uuid.uuid4())
                await db.UsersWords.add_user_info(user_id, unique_id, '\n'.join(words), timer)
                await repeat_1(user_id, bot, unique_id)
            elif timer == 2:
                unique_id = data['unique_id']
                await db.UsersWords.update_words(user_id, unique_id, timer)
                await repeat_2(user_id, bot, unique_id)
            elif timer == 3:
                unique_id = data['unique_id']
                await db.UsersWords.update_words(user_id, unique_id, timer)
                await repeat_3(user_id, bot, unique_id)
            elif timer == 4:
                unique_id = data['unique_id']
                await db.UsersWords.update_words(user_id, unique_id, timer)
                await repeat_4(user_id, bot, unique_id)

        return

    word, translation = words[idx].split(' – ')
    bot_say = text.bot_say
    hint = ''
    if 'attempt' not in data:
        await state.update_data(attempt=0)
    elif data['attempt']:
        hidden_part = int(len(word))
        attempt = data['attempt']
        if attempt < 4:
            hidden_parts = {1: 0.3,
                            2: 0.5,
                            3: 0.8}
            hidden_part = int(len(word) * hidden_parts[attempt])

        bot_say = r.choice(text.bad_attempt)
        hint = text.hint.format(word=word[:hidden_part] + '?' * len(word[hidden_part:]))
    else:
        bot_say = r.choice(text.good_attempt)
        await state.update_data(attempt=0)

    await state.update_data(Exercise_3=word)
    await bot.edit_message_text(chat_id=user_id,
                                message_id=data['exercise'],
                                text=text.Exercise_3.format(bot_say=bot_say, translation=translation) + hint)
    await state.set_state(Exercise.three)


@router.message(Exercise.three, F.text)
async def attempt(msg, state: FSMContext, bot):
    user_id = msg.from_user.id
    text, keyboard = await text_and_keyboard(user_id)

    data = await state.get_data()
    answer = msg.text.lower()
    await bot.delete_message(chat_id=user_id, message_id=msg.message_id)
    if answer == data['Exercise_3']:
        await state.update_data(idx=data['idx'] + 1,
                                attempt=0)
    else:
        await state.update_data(attempt=data['attempt'] + 1)

    await starting_learn_words_3(data['words'], user_id, bot, state)

# REPEATES
async def repeat_1(user_id, bot, unique_id, time=1800):
    text, keyboard = await text_and_keyboard(user_id)
    await asyncio.sleep(time) #1800 = 30 minutes
    words, timer = await db.UsersWords.get_words(user_id, unique_id)
    await bot.send_message(chat_id=user_id,
                           text=text.Repeat.format(words=words),
                           reply_markup=keyboard.repeat(unique_id))
    await db.UsersWords.sent_True(user_id=user_id, unique_id=unique_id)


async def repeat_2(user_id, bot, unique_id, time=28800):
    text, keyboard = await text_and_keyboard(user_id)
    await asyncio.sleep(time)  # 28800 8hours
    words, timer = await db.UsersWords.get_words(user_id, unique_id)
    await bot.send_message(chat_id=user_id,
                           text=text.Repeat.format(words=words),
                           reply_markup=keyboard.repeat(unique_id))
    await db.UsersWords.sent_True(user_id=user_id, unique_id=unique_id)


async def repeat_3(user_id, bot, unique_id, time=86400):
    text, keyboard = await text_and_keyboard(user_id)
    await asyncio.sleep(time)  # 86400 24hours
    words, timer = await db.UsersWords.get_words(user_id, unique_id)
    await bot.send_message(chat_id=user_id,
                           text=text.Repeat.format(words=words),
                           reply_markup=keyboard.repeat(unique_id))
    await db.UsersWords.sent_True(user_id=user_id, unique_id=unique_id)


async def repeat_4(user_id, bot, unique_id, time=259200):
    text, keyboard = await text_and_keyboard(user_id)
    await asyncio.sleep(time) #259200 3days
    words, timer = await db.UsersWords.get_words(user_id, unique_id)
    await bot.send_message(chat_id=user_id,
                           text=text.Repeat.format(words=words),
                           reply_markup=keyboard.repeat(unique_id))
    await db.UsersWords.sent_True(user_id=user_id, unique_id=unique_id)


@router.callback_query(F.data.startswith('repeat_'))
async def repeat1(callback, state: FSMContext, bot):
    data = await state.get_data()
    user_id = callback.from_user.id
    await callback.answer()
    if data.get('start_learn', False):
        to_delete = await bot.send_message(chat_id=user_id,
                                           text="Пожалуйста закончите процедуру запоминания слов (отберите незнакомые слова для запоминания и закончите 3 упражнения с ними) это займет не больше 2 минут")
        await state.update_data(to_delete=to_delete.message_id)
        return

    text, keyboard = await text_and_keyboard(user_id)
    unique_id = callback.data.split("_")[-1]
    words, timer = await db.UsersWords.get_words(user_id, unique_id)
    words = words.split('\n')
    await state.update_data(to_delete_button=callback.message.message_id,
                            idx=0,
                            timer=timer,
                            unique_id=unique_id,
                            words=words)

    delete_menu = await users.get_menu_id(user_id)
    if delete_menu:
        try:
            await bot.delete_message(chat_id=user_id,
                                     message_id=delete_menu)
        except Exception as e:
            logger.error(f"🔴 Ошибка {e} при удалении сообщения (меню) у пользователя: {user_id}")
            await bot.edit_message_text(chat_id=user_id,
                                        message_id=delete_menu,
                                        text="😎")
        await users.update_menu_id(user_id)

    await state.update_data(start_learn=True)
    await starting_learn_words_1(words, user_id, bot, state, True)


@router.callback_query(F.data == 'none')
async def exercise_1(callback):
    await callback.answer()


@router.message(F.text.startswith('/'))
async def start_handler_02(msg, bot, state):
    user_id = msg.from_user.id
    text, keyboard = await text_and_keyboard(user_id)
    data = await state.get_data()
    await bot.delete_message(chat_id=user_id, message_id=msg.message_id)

    if data.get('to_delete', 0):
        await bot.delete_message(chat_id=user_id, message_id=data['to_delete'])

    if data.get('start_learn', False):
        to_delete = await msg.answer("Пожалуйста закончите процедуру запоминания слов (отберите незнакомые слова для запоминания и закончите 3 упражнения с ними) это займет не больше 2 минут")
        await state.update_data(to_delete=to_delete.message_id)
        return

    delete_menu = await users.get_menu_id(user_id)
    if delete_menu:
        await bot.delete_message(chat_id=user_id, message_id=delete_menu)

    menu = await msg.answer(text=text.menu,
                            reply_markup=keyboard.menu(user_id))
    await users.update_menu_id(user_id, menu.message_id)
    await state.clear()


@router.message(F.text)
async def any_text(msg, bot, state: FSMContext):
    user_id = msg.from_user.id
    await bot.delete_message(chat_id=user_id, message_id=msg.message_id)
    if user_id not in await users.get_users_ids():
        to_delete = await msg.answer('Для пользования возможностями бота, пожалуйста зарегистрируйтесь через команду /start')
        await state.update_data(to_delete=to_delete.message_id)
        return

    text, keyboard = await text_and_keyboard(user_id)
    data = await state.get_data()

    if data.get('to_delete', 0):
        await bot.delete_message(chat_id=user_id, message_id=data['to_delete'])

    if data.get('start_learn', False):
        to_delete = await msg.answer("Пожалуйста закончите процедуру запоминания слов (отберите незнакомые слова для запоминания и закончите 3 упражнения с ними) это займет не больше 2 минут")
        await state.update_data(to_delete=to_delete.message_id)
        return

    to_delete = await msg.answer(text.incomprehensible_set_of_characters)
    await state.update_data(to_delete=to_delete.message_id)