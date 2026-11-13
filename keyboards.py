from aiogram import types


class Russian_keyboards:

    def choose_native_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='Русский', callback_data='native_ru')],
            # [types.InlineKeyboardButton(text='English', callback_data='native_en')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def will_learn_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='🇺🇸 English', callback_data='will_learn_en')],
            [types.InlineKeyboardButton(text='🇪🇸 Spanish', callback_data='will_learn_es')],
            [types.InlineKeyboardButton(text='🇩🇪 German', callback_data='will_learn_de')],
            [types.InlineKeyboardButton(text='🇫🇷 French', callback_data='will_learn_fr')],
            [types.InlineKeyboardButton(text='🇮🇹 Italian', callback_data='will_learn_it')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def new_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='Назад 🔙', callback_data='back_to_settings')],
            [types.InlineKeyboardButton(text='🇺🇸 English', callback_data='new_lang_en')],
            [types.InlineKeyboardButton(text='🇪🇸 Spanish', callback_data='new_lang_es')],
            [types.InlineKeyboardButton(text='🇩🇪 German', callback_data='new_lang_de')],
            [types.InlineKeyboardButton(text='🇫🇷 French', callback_data='new_lang_fr')],
            [types.InlineKeyboardButton(text='🇮🇹 Italian', callback_data='new_lang_it')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def word(self):
        buttons = [
            [types.InlineKeyboardButton(text='Учим! 📚', callback_data='learn_word')],
            [types.InlineKeyboardButton(text='Знаю ✅', callback_data='know')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def show_translate_listening(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text='Показать перевод текста', callback_data=f'stl_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def show_translate_essay_feedback(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text='Показать перевод сообщения', callback_data=f'ste_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def repeat(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text="Поехали!", callback_data=f'repeat_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def text_and_translate(self, text=True, translate=True):
        buttons = []
        if text:
            buttons.append([types.InlineKeyboardButton(text="Текст ответа", callback_data='voice_text')])
        if translate:
            buttons.append([types.InlineKeyboardButton(text="Перевод ответа", callback_data='voice_translate')])
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def test(self, lang, flag=False):
        available = ('en',)
        buttons = [
            [types.InlineKeyboardButton(text='Назад 🔙', callback_data='back_to_settings')]
        ]
        if lang in available:
            buttons.extend([[types.InlineKeyboardButton(text="Начать быстрый тест! (Только лексика)", callback_data='start_test_1')],
                            [types.InlineKeyboardButton(text="Начать глубокий тест! (Лексика + Грамматика)", callback_data='start_test_0')]])
            if flag:
                buttons = [
                    [types.InlineKeyboardButton(text="Начать тест!", callback_data='start_test_1')]
                ]

        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def final_test(self):
        buttons = [
            [types.InlineKeyboardButton(text="Изменить", callback_data='change')],
            [types.InlineKeyboardButton(text="Оставить прежний", callback_data='back')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def ready_learn(self):
        buttons = [
            [types.InlineKeyboardButton(text="Поехали!", callback_data='ex_to_learn')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def dialog(self):
        buttons = [
            [types.InlineKeyboardButton(text="Назад 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text="Переписываться", callback_data='dialog_to_start')],
            [types.InlineKeyboardButton(text="Говорить", callback_data='voice')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def menu(self, user):
        buttons = [
            [types.InlineKeyboardButton(text='Информация ℹ️', callback_data='info_lang')],
            [types.InlineKeyboardButton(text='Настройки ⚙️', callback_data='settings'),
             types.InlineKeyboardButton(text='Мой словарь 📕', callback_data='my_dict')],
            [types.InlineKeyboardButton(text='Аудирование 🎧', callback_data='audio')],
            [types.InlineKeyboardButton(text='Работа с текстом 📄', callback_data='writing_skills'),
             types.InlineKeyboardButton(text='Ввести диалог 🎙', callback_data='dialog')],
            [types.InlineKeyboardButton(text='Начать запоминать слова! 📌', callback_data='start_learn')],
        ]
        # if user in (764124336,):
        #     buttons.append([types.InlineKeyboardButton(text="Админка 👀", callback_data='admin')])
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def writing_skills(self):
        buttons = [
            [types.InlineKeyboardButton(text="Назад 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text='Перевод текста 📖', callback_data='translate_text')],
            [types.InlineKeyboardButton(text='Проверка эссе 📝', callback_data='essay')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def essay(self):
        buttons = [
            [types.InlineKeyboardButton(text="Назад 🔙", callback_data='writing_skills')],
            [types.InlineKeyboardButton(text='Начать!', callback_data='essay_start')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def listening(self):
        buttons = [
            [types.InlineKeyboardButton(text="Назад 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text="Начать!", callback_data='audio_theme')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def listening_test(self):
        buttons = [
            [types.InlineKeyboardButton(text="Поехали!", callback_data='audio_test')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def text_symbols(self):
        buttons = [
            [types.InlineKeyboardButton(text='Назад 🔙', callback_data='writing_skills')],
            [types.InlineKeyboardButton(text="1️⃣0️⃣0️⃣", callback_data='symbols_100'),
             types.InlineKeyboardButton(text="2️⃣0️⃣0️⃣", callback_data='symbols_200')],
            [types.InlineKeyboardButton(text="5️⃣0️⃣0️⃣", callback_data='symbols_500'),
             types.InlineKeyboardButton(text="1️⃣0️⃣0️⃣0️⃣", callback_data='symbols_1000')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def my_dict(self):
        buttons = [
            [types.InlineKeyboardButton(text='Назад 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Добавить словосочетание 🖊', callback_data='add_word')],
            [types.InlineKeyboardButton(text='Вывести список в чат 📄', callback_data='print_my_words')],
            [types.InlineKeyboardButton(text='Учить мои слова', callback_data='learn_my_words')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def level(self, lang):
        available = ('en',)

        buttons = [
            [types.InlineKeyboardButton(text="Я начинающий", callback_data='level_A1')],
            [types.InlineKeyboardButton(text='A1', callback_data='level_A1'),
             types.InlineKeyboardButton(text='A2', callback_data='level_A2')],
            [types.InlineKeyboardButton(text='B1', callback_data='level_B1'),
             types.InlineKeyboardButton(text='B2', callback_data='level_B2')],
            [types.InlineKeyboardButton(text='C1', callback_data='level_C1')]
            # types.InlineKeyboardButton(text='C2', callback_data='C2')]
        ]
        if lang in available:
            buttons.append([types.InlineKeyboardButton(text='Пройти тест', callback_data='test_lang')])

        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def info_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='Назад 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='% изучения уровня/темы', callback_data='info_level')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def back(self):
        buttons = [
            [types.InlineKeyboardButton(text='Назад 🔙', callback_data='back')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def settings(self):
        buttons = [
            [types.InlineKeyboardButton(text='Назад 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Изменить уровень', callback_data='change_level')],
            [types.InlineKeyboardButton(text='Тест на уровень владения языком', callback_data='test_lang')],
            [types.InlineKeyboardButton(text='Выбрать другой язык', callback_data='change_language')],
            [types.InlineKeyboardButton(text='Выбрать тематику слов', callback_data='choose_theme')],
            [types.InlineKeyboardButton(text='Изменить число изучаемых слов за сеанс', callback_data='update_quantity_words')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def change_level(self):
        buttons = [
            [types.InlineKeyboardButton(text='Назад 🔙', callback_data='back_to_settings')],
            [types.InlineKeyboardButton(text='Повысить уровень', callback_data='up_level')],
            [types.InlineKeyboardButton(text='Понизить уровень', callback_data='down_level')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def choose_theme(self):
        buttons = [
            [types.InlineKeyboardButton(text='Назад 🔙', callback_data='back_to_settings')],
            [types.InlineKeyboardButton(text='Сельское хозяйство', callback_data='agro')],
            [types.InlineKeyboardButton(text='Кибербезопасность', callback_data='cybersecurity')],
            [types.InlineKeyboardButton(text='IT', callback_data='IT')],
            # types.InlineKeyboardButton(text='Тема 4', callback_data='theme4')],
            # [types.InlineKeyboardButton(text='Тема 5', callback_data='theme5'),
            #  types.InlineKeyboardButton(text='Тема 6', callback_data='theme6')],
            [types.InlineKeyboardButton(text='Продолжить изучать слова текущего уровня', callback_data='continue_to_study_the_words')],
            [types.InlineKeyboardButton(text='Я просто хочу выучить 5000 слов', callback_data='5000')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard


class English_keyboards:

    def will_learn_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='🇷🇺 Русский', callback_data='rus')],
            # [types.InlineKeyboardButton(text='🇪🇸 Spanish', callback_data='spain')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def new_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='Back 🔙', callback_data='back_to_settings')],
            [types.InlineKeyboardButton(text='🇪🇸 Spanish', callback_data='new_lang_es')],
            [types.InlineKeyboardButton(text='🇩🇪 German', callback_data='new_lang_de')],
            [types.InlineKeyboardButton(text='🇫🇷 French', callback_data='new_lang_fr')],
            [types.InlineKeyboardButton(text='🇮🇹 Italian', callback_data='new_lang_it')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def show_translate_listening(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text='Show text translation', callback_data=f'stl_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def show_translate_essay_feedback(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text='Show the translation of the message', callback_data=f'ste_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def word(self):
        buttons = [
            [types.InlineKeyboardButton(text='Learn! 📚', callback_data='learn_word')],
            [types.InlineKeyboardButton(text='I know ✅', callback_data='know')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def repeat(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text="Let's go!", callback_data=f'repeat_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def text_and_translate(self, text=True, translate=True):
        buttons = []
        if text:
            buttons.append([types.InlineKeyboardButton(text="Response text", callback_data='voice_text')])
        if translate:
            buttons.append([types.InlineKeyboardButton(text="Translation of the response", callback_data='voice_translate')])
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def final_test(self):
        buttons = [
            [types.InlineKeyboardButton(text="Change", callback_data='change')],
            [types.InlineKeyboardButton(text="Keep previous", callback_data='back')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def ready_learn(self):
        buttons = [
            [types.InlineKeyboardButton(text="Let's go!", callback_data='ex_to_learn')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def dialog(self):
        buttons = [
            [types.InlineKeyboardButton(text="Back 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text="To correspond", callback_data='dialog_to_start')],
            [types.InlineKeyboardButton(text="To speak", callback_data='voice')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def menu(self, user):
        buttons = [
            [types.InlineKeyboardButton(text='Information ℹ️', callback_data='info_lang')],
            [types.InlineKeyboardButton(text='Settings ⚙️', callback_data='settings'),
             types.InlineKeyboardButton(text='My dictionary 📕', callback_data='my_dict')],
            [types.InlineKeyboardButton(text='Listening skills 🎧', callback_data='audio')],
            [types.InlineKeyboardButton(text='Working with text 📄', callback_data='writing_skills'),
             types.InlineKeyboardButton(text='Enter a dialogue 🎙', callback_data='dialog')],
            [types.InlineKeyboardButton(text='Start learning words! 📌', callback_data='start_learn')],
        ]
        # if user in (764124336,):
        #     buttons.append([types.InlineKeyboardButton(text="Админка 👀", callback_data='admin')])
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def writing_skills(self):
        buttons = [
            [types.InlineKeyboardButton(text="Back 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text='Text translation 📖', callback_data='translate_text')],
            [types.InlineKeyboardButton(text='Checking the essay 📝', callback_data='essay')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def essay(self):
        buttons = [
            [types.InlineKeyboardButton(text="Back 🔙", callback_data='writing_skills')],
            [types.InlineKeyboardButton(text='Start!', callback_data='essay_start')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def listening(self):
        buttons = [
            [types.InlineKeyboardButton(text="Back 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text="Start!", callback_data='audio_theme')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def listening_test(self):
        buttons = [
            [types.InlineKeyboardButton(text="Let's go!", callback_data='audio_test')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def text_symbols(self):
        buttons = [
            [types.InlineKeyboardButton(text='Back 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text="1️⃣0️⃣0️⃣", callback_data='symbols_100'),
             types.InlineKeyboardButton(text="2️⃣0️⃣0️⃣", callback_data='symbols_200')],
            [types.InlineKeyboardButton(text="5️⃣0️⃣0️⃣", callback_data='symbols_500'),
             types.InlineKeyboardButton(text="1️⃣0️⃣0️⃣0️⃣", callback_data='symbols_1000')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def my_dict(self):
        buttons = [
            [types.InlineKeyboardButton(text='Back 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Add a phrase 🖊', callback_data='add_word')],
            [types.InlineKeyboardButton(text='Print list to chat 📄', callback_data='print_my_words')],
            [types.InlineKeyboardButton(text='Learn my words', callback_data='learn_my_words')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def level(self, lang):
        available = ('en',)

        buttons = [
            [types.InlineKeyboardButton(text="I'm a beginner", callback_data='level_A1')],
            [types.InlineKeyboardButton(text='A1', callback_data='level_A1'),
             types.InlineKeyboardButton(text='A2', callback_data='level_A2')],
            [types.InlineKeyboardButton(text='B1', callback_data='level_B1'),
             types.InlineKeyboardButton(text='B2', callback_data='level_B2')],
            [types.InlineKeyboardButton(text='C1', callback_data='level_C1')]
            # types.InlineKeyboardButton(text='C2', callback_data='C2')]
        ]
        if lang in available:
            buttons.append([types.InlineKeyboardButton(text='Take a test', callback_data='test_lang')])

        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def test(self, lang, flag=False):
        available = ('en',)
        buttons = [
            [types.InlineKeyboardButton(text='Back 🔙', callback_data='back_to_settings')]
        ]
        if lang in available:
            buttons.extend(
                [[types.InlineKeyboardButton(text="Start quick test! (Vocabulary)", callback_data='start_test_1')],
                 [types.InlineKeyboardButton(text="Start deep test! (Vocabulary + Grammmar)", callback_data='start_test_0')]])
            if flag:
                buttons = [
                    [types.InlineKeyboardButton(text="Start test!", callback_data='start_test_1')]
                ]

        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def info_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='Back 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Level progress %', callback_data='info_level')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def back(self):
        buttons = [
            [types.InlineKeyboardButton(text='Back 🔙', callback_data='back')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def settings(self):
        buttons = [
            [types.InlineKeyboardButton(text='Back 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Change level', callback_data='change_level')],
            [types.InlineKeyboardButton(text='Language proficiency test', callback_data='test_lang')],
            [types.InlineKeyboardButton(text='Choose another language', callback_data='change_language')],
            [types.InlineKeyboardButton(text='Choose word theme', callback_data='choose_theme')],
            [types.InlineKeyboardButton(text='Change number of words per session', callback_data='update_quantity_words')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def change_level(self):
        buttons = [
            [types.InlineKeyboardButton(text='Back 🔙', callback_data='back_to_settings')],
            [types.InlineKeyboardButton(text='Increase level', callback_data='up_level')],
            [types.InlineKeyboardButton(text='Decrease level', callback_data='down_level')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def choose_theme(self):
        buttons = [
            [types.InlineKeyboardButton(text='Back 🔙', callback_data='back_to_settings')],
            [types.InlineKeyboardButton(text='Agriculture', callback_data='agro')],
            [types.InlineKeyboardButton(text='Cybersecurity', callback_data='cybersecurity')],
            [types.InlineKeyboardButton(text='IT', callback_data='IT')],
            # types.InlineKeyboardButton(text='Theme 4', callback_data='theme4')],
            # [types.InlineKeyboardButton(text='Theme 5', callback_data='theme5'),
            #  types.InlineKeyboardButton(text='Theme 6', callback_data='theme6')],
            [types.InlineKeyboardButton(text='Continue learning words at current level', callback_data='сontinue_to_study_the_words')],
            [types.InlineKeyboardButton(text='I just want to learn 5000 words', callback_data='5000')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

class Spanish_keyboards:

    def will_learn_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='🇺🇸 Inglés', callback_data='will_learn_usa')],
            # [types.InlineKeyboardButton(text='🇪🇸 Spanish', callback_data='spain')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def new_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='Atrás 🔙', callback_data='back_to_settings')],
            [types.InlineKeyboardButton(text='🇺🇸 English', callback_data='new_lang_en')],
            [types.InlineKeyboardButton(text='🇩🇪 German', callback_data='new_lang_de')],
            [types.InlineKeyboardButton(text='🇫🇷 French', callback_data='new_lang_fr')],
            [types.InlineKeyboardButton(text='🇮🇹 Italian', callback_data='new_lang_it')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def show_translate_listening(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text='Mostrar traducción del texto', callback_data=f'stl_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def show_translate_essay_feedback(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text='Mostrar traducción del mensaje', callback_data=f'ste_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def word(self):
        buttons = [
            [types.InlineKeyboardButton(text='¡Aprender! 📚', callback_data='learn_word')],
            [types.InlineKeyboardButton(text='Ya sé ✅', callback_data='know')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def repeat(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text="¡Vamos!", callback_data=f'repeat_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def text_and_translate(self, text=True, translate=True):
        buttons = []
        if text:
            buttons.append([types.InlineKeyboardButton(text="Texto de la respuesta", callback_data='voice_text')])
        if translate:
            buttons.append(
                [types.InlineKeyboardButton(text="Traducción de la respuesta", callback_data='voice_translate')])
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def level(self, lang):
        available = ('en',)

        buttons = [
            [types.InlineKeyboardButton(text="Soy un principiante", callback_data='level_A1')],
            [types.InlineKeyboardButton(text='A1', callback_data='level_A1'),
             types.InlineKeyboardButton(text='A2', callback_data='level_A2')],
            [types.InlineKeyboardButton(text='B1', callback_data='level_B1'),
             types.InlineKeyboardButton(text='B2', callback_data='level_B2')],
            [types.InlineKeyboardButton(text='C1', callback_data='level_C1')]
            # types.InlineKeyboardButton(text='C2', callback_data='C2')]
        ]
        if lang in available:
            buttons.append([types.InlineKeyboardButton(text='Hacer una prueba', callback_data='test_lang')])

        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def test(self, lang, flag=False):
        available = ('en',)
        buttons = [
            [types.InlineKeyboardButton(text='Atrás 🔙', callback_data='back_to_settings')]
        ]
        if lang in available:
            buttons.extend(
                [[types.InlineKeyboardButton(text="Comenzar prueba rápida! (20 preguntas)", callback_data='start_test_1')],
                 [types.InlineKeyboardButton(text="Comenzar prueba profunda! (50 preguntas)", callback_data='start_test_0')]])
            if flag:
                buttons = [
                    [types.InlineKeyboardButton(text="Comenzar prueba!", callback_data='start_test_1')]
                ]

        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def final_test(self):
        buttons = [
            [types.InlineKeyboardButton(text="Cambiar", callback_data='change')],
            [types.InlineKeyboardButton(text="Mantener anterior", callback_data='back')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def ready_learn(self):
        buttons = [
            [types.InlineKeyboardButton(text="¡Vamos!", callback_data='ex_to_learn')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def dialog(self):
        buttons = [
            [types.InlineKeyboardButton(text="Atrás 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text="Corresponder", callback_data='dialog_to_start')],
            [types.InlineKeyboardButton(text="Hablar", callback_data='voice')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def menu(self, user):
        buttons = [
            [types.InlineKeyboardButton(text='Información ℹ️', callback_data='info_lang')],
            [types.InlineKeyboardButton(text='Configuración ⚙️', callback_data='settings'),
             types.InlineKeyboardButton(text='Mi diccionario 📕', callback_data='my_dict')],
            [types.InlineKeyboardButton(text='Habilidades auditivas 🎧', callback_data='audio')],
            [types.InlineKeyboardButton(text='Trabajar con texto 📄', callback_data='writing_skills'),
             types.InlineKeyboardButton(text='Iniciar un diálogo 🎙', callback_data='dialog')],
            [types.InlineKeyboardButton(text='¡Comenzar a aprender palabras! 📌', callback_data='start_learn')],
        ]
        # if user in (764124336,):
        #     buttons.append([types.InlineKeyboardButton(text="Админка 👀", callback_data='admin')])
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def writing_skills(self):
        buttons = [
            [types.InlineKeyboardButton(text="Atrás 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text='Traducción de texto 📖', callback_data='translate_text')],
            [types.InlineKeyboardButton(text='Revisión de ensayo 📝', callback_data='essay')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def essay(self):
        buttons = [
            [types.InlineKeyboardButton(text="Atrás 🔙", callback_data='writing_skills')],
            [types.InlineKeyboardButton(text='Comenzar!', callback_data='essay_start')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def listening(self):
        buttons = [
            [types.InlineKeyboardButton(text="Atrás 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text="Comenzar!", callback_data='audio_theme')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def listening_test(self):
        buttons = [
            [types.InlineKeyboardButton(text="¡Vamos!", callback_data='audio_test')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def text_symbols(self):
        buttons = [
            [types.InlineKeyboardButton(text='Atrás 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text="1️⃣0️⃣0️⃣", callback_data='symbols_100'),
             types.InlineKeyboardButton(text="2️⃣0️⃣0️⃣", callback_data='symbols_200')],
            [types.InlineKeyboardButton(text="5️⃣0️⃣0️⃣", callback_data='symbols_500'),
             types.InlineKeyboardButton(text="1️⃣0️⃣0️⃣0️⃣", callback_data='symbols_1000')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def my_dict(self):
        buttons = [
            [types.InlineKeyboardButton(text='Atrás 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Añadir una frase 🖊', callback_data='add_word')],
            [types.InlineKeyboardButton(text='Imprimir lista en el chat 📄', callback_data='print_my_words')],
            [types.InlineKeyboardButton(text='Aprender mis palabras', callback_data='learn_my_words')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def info_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='Atrás 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Progreso del nivel %', callback_data='info_level')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def back(self):
        buttons = [
            [types.InlineKeyboardButton(text='Atrás 🔙', callback_data='back')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def settings(self):
        buttons = [
            [types.InlineKeyboardButton(text='Atrás 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Cambiar nivel', callback_data='change_level')],
            [types.InlineKeyboardButton(text='Prueba de dominio del idioma', callback_data='test_lang')],
            [types.InlineKeyboardButton(text='Elegir otro idioma', callback_data='change_language')],
            [types.InlineKeyboardButton(text='Elegir tema de palabras', callback_data='choose_theme')],
            [types.InlineKeyboardButton(text='Cambiar número de palabras por sesión',
                                        callback_data='update_quantity_words')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def change_level(self):
        buttons = [
            [types.InlineKeyboardButton(text='Atrás 🔙', callback_data='back_to_settings')],
            [types.InlineKeyboardButton(text='Subir de nivel', callback_data='up_level')],
            [types.InlineKeyboardButton(text='Bajar de nivel', callback_data='down_level')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def choose_theme(self):
        buttons = [
            [types.InlineKeyboardButton(text='Atrás 🔙', callback_data='back_to_settings')],
            # [types.InlineKeyboardButton(text='Agricultura', callback_data='agro')],
            # types.InlineKeyboardButton(text='Tema 2', callback_data='theme2')],
            # [types.InlineKeyboardButton(text='Tema 3', callback_data='theme3'),
            # types.InlineKeyboardButton(text='Tema 4', callback_data='theme4')],
            # [types.InlineKeyboardButton(text='Tema 5', callback_data='theme5'),
            #  types.InlineKeyboardButton(text='Tema 6', callback_data='theme6')],
            # [types.InlineKeyboardButton(text='Continuar estudiando palabras del nivel actual',
            #                             callback_data='сontinue_to_study_the_words')],
            # [types.InlineKeyboardButton(text='Solo quiero aprender 5000 palabras', callback_data='5000')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

class German_keyboards:

    def will_learn_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='🇺🇸 Englisch', callback_data='will_learn_en')],
            [types.InlineKeyboardButton(text='🇪🇸 Spanisch', callback_data='will_learn_es')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def new_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='Zurück 🔙', callback_data='back_to_settings')],
            [types.InlineKeyboardButton(text='🇺🇸 English', callback_data='new_lang_en')],
            [types.InlineKeyboardButton(text='🇪🇸 Spanish', callback_data='new_lang_es')],
            [types.InlineKeyboardButton(text='🇫🇷 French', callback_data='new_lang_fr')],
            [types.InlineKeyboardButton(text='🇮🇹 Italian', callback_data='new_lang_it')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def show_translate_listening(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text='Textübersetzung anzeigen', callback_data=f'stl_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def show_translate_essay_feedback(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text='Nachricht übersetzen anzeigen', callback_data=f'ste_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def word(self):
        buttons = [
            [types.InlineKeyboardButton(text='Lernen! 📚', callback_data='learn_word')],
            [types.InlineKeyboardButton(text='Ich kenne es ✅', callback_data='know')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def repeat(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text="Los geht's!", callback_data=f'repeat_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def text_and_translate(self, text=True, translate=True):
        buttons = []
        if text:
            buttons.append([types.InlineKeyboardButton(text="Antworttext", callback_data='voice_text')])
        if translate:
            buttons.append(
                [types.InlineKeyboardButton(text="Übersetzung der Antwort", callback_data='voice_translate')])
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def level(self, lang):
        available = ('en',)

        buttons = [
            [types.InlineKeyboardButton(text="Ich bin Anfänger", callback_data='level_A1')],
            [types.InlineKeyboardButton(text='A1', callback_data='level_A1'),
             types.InlineKeyboardButton(text='A2', callback_data='level_A2')],
            [types.InlineKeyboardButton(text='B1', callback_data='level_B1'),
             types.InlineKeyboardButton(text='B2', callback_data='level_B2')],
            [types.InlineKeyboardButton(text='C1', callback_data='level_C1')]
            # types.InlineKeyboardButton(text='C2', callback_data='C2')]
        ]
        if lang in available:
            buttons.append([types.InlineKeyboardButton(text='Einen Test machen', callback_data='test_lang')])

        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def test(self, lang, flag=False):
        available = ('en',)
        buttons = [
            [types.InlineKeyboardButton(text='Zurück 🔙', callback_data='back_to_settings')]
        ]
        if lang in available:
            buttons.extend(
                [[types.InlineKeyboardButton(text="Schnelltest starten! (20 Fragen)", callback_data='start_test_1')],
                 [types.InlineKeyboardButton(text="Gründlichkeitstest starten! (50 Fragen)", callback_data='start_test_0')]])
            if flag:
                buttons = [
                    [types.InlineKeyboardButton(text="Test starten!", callback_data='start_test_1')]
                ]

        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def final_test(self):
        buttons = [
            [types.InlineKeyboardButton(text="Ändern", callback_data='change')],
            [types.InlineKeyboardButton(text="Beibehalten", callback_data='back')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def ready_learn(self):
        buttons = [
            [types.InlineKeyboardButton(text="Los geht's!", callback_data='ex_to_learn')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def dialog(self):
        buttons = [
            [types.InlineKeyboardButton(text="Zurück 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text="Korrespondieren", callback_data='dialog_to_start')],
            [types.InlineKeyboardButton(text="Sprechen", callback_data='voice')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def menu(self, user):
        buttons = [
            [types.InlineKeyboardButton(text='Informationen ℹ️', callback_data='info_lang')],
            [types.InlineKeyboardButton(text='Einstellungen ⚙️', callback_data='settings'),
             types.InlineKeyboardButton(text='Mein Wörterbuch 📕', callback_data='my_dict')],
            [types.InlineKeyboardButton(text='Hörverständnis 🎧', callback_data='audio')],
            [types.InlineKeyboardButton(text='Mit Text arbeiten 📄', callback_data='writing_skills'),
             types.InlineKeyboardButton(text='Dialog starten 🎙', callback_data='dialog')],
            [types.InlineKeyboardButton(text='Wörter lernen beginnen! 📌', callback_data='start_learn')],
        ]
        # if user in (764124336,):
        #     buttons.append([types.InlineKeyboardButton(text="Админка 👀", callback_data='admin')])
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def writing_skills(self):
        buttons = [
            [types.InlineKeyboardButton(text="Zurück 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text='Textübersetzung 📖', callback_data='translate_text')],
            [types.InlineKeyboardButton(text='Essay überprüfen 📝', callback_data='essay')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def essay(self):
        buttons = [
            [types.InlineKeyboardButton(text="Zurück 🔙", callback_data='writing_skills')],
            [types.InlineKeyboardButton(text='Starten!', callback_data='essay_start')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def listening(self):
        buttons = [
            [types.InlineKeyboardButton(text="Zurück 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text="Starten!", callback_data='audio_theme')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def listening_test(self):
        buttons = [
            [types.InlineKeyboardButton(text="Los geht's!", callback_data='audio_test')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def text_symbols(self):
        buttons = [
            [types.InlineKeyboardButton(text='Zurück 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text="1️⃣0️⃣0️⃣", callback_data='symbols_100'),
             types.InlineKeyboardButton(text="2️⃣0️⃣0️⃣", callback_data='symbols_200')],
            [types.InlineKeyboardButton(text="5️⃣0️⃣0️⃣", callback_data='symbols_500'),
             types.InlineKeyboardButton(text="1️⃣0️⃣0️⃣0️⃣", callback_data='symbols_1000')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def my_dict(self):
        buttons = [
            [types.InlineKeyboardButton(text='Zurück 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Einen Ausdruck hinzufügen 🖊', callback_data='add_word')],
            [types.InlineKeyboardButton(text='Liste im Chat ausgeben 📄', callback_data='print_my_words')],
            [types.InlineKeyboardButton(text='Meine Wörter lernen', callback_data='learn_my_words')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def info_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='Zurück 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Fortschritt des Levels %', callback_data='info_level')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def back(self):
        buttons = [
            [types.InlineKeyboardButton(text='Zurück 🔙', callback_data='back')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def settings(self):
        buttons = [
            [types.InlineKeyboardButton(text='Zurück 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Level ändern', callback_data='change_level')],
            [types.InlineKeyboardButton(text='Sprachtest', callback_data='test_lang')],
            [types.InlineKeyboardButton(text='Anderen Sprache wählen', callback_data='change_language')],
            [types.InlineKeyboardButton(text='Wörterthema wählen', callback_data='choose_theme')],
            [types.InlineKeyboardButton(text='Anzahl der Wörter pro Sitzung ändern',
                                        callback_data='update_quantity_words')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def change_level(self):
        buttons = [
            [types.InlineKeyboardButton(text='Zurück 🔙', callback_data='back_to_settings')],
            [types.InlineKeyboardButton(text='Level erhöhen', callback_data='up_level')],
            [types.InlineKeyboardButton(text='Level senken', callback_data='down_level')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def choose_theme(self):
        buttons = [
            [types.InlineKeyboardButton(text='Zurück 🔙', callback_data='back_to_settings')],
            # [types.InlineKeyboardButton(text='Landwirtschaft', callback_data='agro')],
            # [types.InlineKeyboardButton(text='Thema 2', callback_data='theme2')],
            # [types.InlineKeyboardButton(text='Thema 3', callback_data='theme3'), types.InlineKeyboardButton(text='Thema 4', callback_data='theme4')],
            # [types.InlineKeyboardButton(text='Thema 5', callback_data='theme5'), types.InlineKeyboardButton(text='Thema 6', callback_data='theme6')],
            # [types.InlineKeyboardButton(text='Weiter mit aktuellen Wörtern lernen', callback_data='сontinue_to_study_the_words')],
            # [types.InlineKeyboardButton(text='Ich möchte einfach 5000 Wörter lernen', callback_data='5000')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

class French_keyboards:

    def will_learn_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='🇺🇸 Anglais', callback_data='will_learn_en')],
            [types.InlineKeyboardButton(text='🇪🇸 Espagnol', callback_data='will_learn_es')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def new_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='Retour 🔙', callback_data='back_to_settings')],
            [types.InlineKeyboardButton(text='🇺🇸 English', callback_data='new_lang_en')],
            [types.InlineKeyboardButton(text='🇪🇸 Spanish', callback_data='new_lang_es')],
            [types.InlineKeyboardButton(text='🇩🇪 German', callback_data='new_lang_de')],
            [types.InlineKeyboardButton(text='🇮🇹 Italian', callback_data='new_lang_it')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def show_translate_listening(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text='Afficher la traduction du texte', callback_data=f'stl_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def show_translate_essay_feedback(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text='Afficher la traduction du message', callback_data=f'ste_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def word(self):
        buttons = [
            [types.InlineKeyboardButton(text='Apprendre ! 📚', callback_data='learn_word')],
            [types.InlineKeyboardButton(text='Je connais ✅', callback_data='know')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def repeat(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text="C'est parti !", callback_data=f'repeat_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def text_and_translate(self, text=True, translate=True):
        buttons = []
        if text:
            buttons.append([types.InlineKeyboardButton(text="Texte de la réponse", callback_data='voice_text')])
        if translate:
            buttons.append(
                [types.InlineKeyboardButton(text="Traduction de la réponse", callback_data='voice_translate')])
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def level(self, lang):
        available = ('en',)

        buttons = [
            [types.InlineKeyboardButton(text="Je suis un débutant", callback_data='level_A1')],
            [types.InlineKeyboardButton(text='A1', callback_data='level_A1'),
             types.InlineKeyboardButton(text='A2', callback_data='level_A2')],
            [types.InlineKeyboardButton(text='B1', callback_data='level_B1'),
             types.InlineKeyboardButton(text='B2', callback_data='level_B2')],
            [types.InlineKeyboardButton(text='C1', callback_data='level_C1')]
            # types.InlineKeyboardButton(text='C2', callback_data='C2')]
        ]
        if lang in available:
            buttons.append([types.InlineKeyboardButton(text='Passer un test', callback_data='test_lang')])

        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def test(self, lang, flag=False):
        available = ('en',)
        buttons = [
            [types.InlineKeyboardButton(text='Retour 🔙', callback_data='back_to_settings')]
        ]
        if lang in available:
            buttons.extend(
                [[types.InlineKeyboardButton(text="Commencer le test rapide ! (20 questions)", callback_data='start_test_1')],
                 [types.InlineKeyboardButton(text="Commencer le test approfondi ! (50 questions)", callback_data='start_test_0')]])
            if flag:
                buttons = [
                    [types.InlineKeyboardButton(text="Commencer le test !", callback_data='start_test_1')]
                ]

        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def final_test(self):
        buttons = [
            [types.InlineKeyboardButton(text="Changer", callback_data='change')],
            [types.InlineKeyboardButton(text="Garder l'ancien", callback_data='back')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def ready_learn(self):
        buttons = [
            [types.InlineKeyboardButton(text="C'est parti !", callback_data='ex_to_learn')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def dialog(self):
        buttons = [
            [types.InlineKeyboardButton(text="Retour 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text="Correspondre", callback_data='dialog_to_start')],
            [types.InlineKeyboardButton(text="Parler", callback_data='voice')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def menu(self, user):
        buttons = [
            [types.InlineKeyboardButton(text='Informations ℹ️', callback_data='info_lang')],
            [types.InlineKeyboardButton(text='Paramètres ⚙️', callback_data='settings'),
             types.InlineKeyboardButton(text='Mon dictionnaire 📕', callback_data='my_dict')],
            [types.InlineKeyboardButton(text='Compétences d\'écoute 🎧', callback_data='audio')],
            [types.InlineKeyboardButton(text='Travail avec le texte 📄', callback_data='writing_skills'),
             types.InlineKeyboardButton(text='Entrer en dialogue 🎙', callback_data='dialog')],
            [types.InlineKeyboardButton(text='Commencer à apprendre les mots ! 📌', callback_data='start_learn')],
        ]
        # if user in (764124336,):
        #     buttons.append([types.InlineKeyboardButton(text="Админка 👀", callback_data='admin')])
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def writing_skills(self):
        buttons = [
            [types.InlineKeyboardButton(text="Retour 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text='Traduction de texte 📖', callback_data='translate_text')],
            [types.InlineKeyboardButton(text='Correction de l\'essai 📝', callback_data='essay')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def essay(self):
        buttons = [
            [types.InlineKeyboardButton(text="Retour 🔙", callback_data='writing_skills')],
            [types.InlineKeyboardButton(text='Commencer !', callback_data='essay_start')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def listening(self):
        buttons = [
            [types.InlineKeyboardButton(text="Retour 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text="Commencer !", callback_data='audio_theme')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def listening_test(self):
        buttons = [
            [types.InlineKeyboardButton(text="C'est parti !", callback_data='audio_test')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def text_symbols(self):
        buttons = [
            [types.InlineKeyboardButton(text='Retour 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text="1️⃣0️⃣0️⃣", callback_data='symbols_100'),
             types.InlineKeyboardButton(text="2️⃣0️⃣0️⃣", callback_data='symbols_200')],
            [types.InlineKeyboardButton(text="5️⃣0️⃣0️⃣", callback_data='symbols_500'),
             types.InlineKeyboardButton(text="1️⃣0️⃣0️⃣0️⃣", callback_data='symbols_1000')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def my_dict(self):
        buttons = [
            [types.InlineKeyboardButton(text='Retour 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Ajouter une phrase 🖊', callback_data='add_word')],
            [types.InlineKeyboardButton(text='Imprimer la liste dans le chat 📄', callback_data='print_my_words')],
            [types.InlineKeyboardButton(text='Apprendre mes mots', callback_data='learn_my_words')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def info_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='Retour 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Progression du niveau %', callback_data='info_level')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def back(self):
        buttons = [
            [types.InlineKeyboardButton(text='Retour 🔙', callback_data='back')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def settings(self):
        buttons = [
            [types.InlineKeyboardButton(text='Retour 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Changer de niveau', callback_data='change_level')],
            [types.InlineKeyboardButton(text='Test de niveau linguistique', callback_data='test_lang')],
            [types.InlineKeyboardButton(text='Choisir une autre langue', callback_data='change_language')],
            [types.InlineKeyboardButton(text='Choisir un thème de mots', callback_data='choose_theme')],
            [types.InlineKeyboardButton(text='Modifier le nombre de mots par session',
                                        callback_data='update_quantity_words')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def change_level(self):
        buttons = [
            [types.InlineKeyboardButton(text='Retour 🔙', callback_data='back_to_settings')],
            [types.InlineKeyboardButton(text='Augmenter le niveau', callback_data='up_level')],
            [types.InlineKeyboardButton(text='Diminuer le niveau', callback_data='down_level')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def choose_theme(self):
        buttons = [
            [types.InlineKeyboardButton(text='Retour 🔙', callback_data='back_to_settings')],
            # [types.InlineKeyboardButton(text='Agriculture', callback_data='agro')],
            # [types.InlineKeyboardButton(text='Thème 2', callback_data='theme2')],
            # [types.InlineKeyboardButton(text='Thème 3', callback_data='theme3'), types.InlineKeyboardButton(text='Thème 4', callback_data='theme4')],
            # [types.InlineKeyboardButton(text='Thème 5', callback_data='theme5'), types.InlineKeyboardButton(text='Thème 6', callback_data='theme6')],
            # [types.InlineKeyboardButton(text='Continuer à apprendre les mots du niveau actuel', callback_data='сontinue_to_study_the_words')],
            # [types.InlineKeyboardButton(text='Je veux juste apprendre 5000 mots', callback_data='5000')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

class Italian_keyboards:

    def will_learn_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='🇺🇸 Inglese', callback_data='will_learn_en')],
            [types.InlineKeyboardButton(text='🇪🇸 Spagnolo', callback_data='will_learn_es')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def new_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='Indietro 🔙', callback_data='back_to_settings')],
            [types.InlineKeyboardButton(text='🇺🇸 English', callback_data='new_lang_en')],
            [types.InlineKeyboardButton(text='🇪🇸 Spanish', callback_data='new_lang_es')],
            [types.InlineKeyboardButton(text='🇩🇪 German', callback_data='new_lang_de')],
            [types.InlineKeyboardButton(text='🇫🇷 French', callback_data='new_lang_fr')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def show_translate_listening(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text='Mostra traduzione del testo', callback_data=f'stl_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def show_translate_essay_feedback(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text='Mostra la traduzione del messaggio', callback_data=f'ste_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def word(self):
        buttons = [
            [types.InlineKeyboardButton(text='Impara! 📚', callback_data='learn_word')],
            [types.InlineKeyboardButton(text='Lo so ✅', callback_data='know')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def repeat(self, unique_id):
        buttons = [
            [types.InlineKeyboardButton(text="Andiamo!", callback_data=f'repeat_{unique_id}')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def text_and_translate(self, text=True, translate=True):
        buttons = []
        if text:
            buttons.append([types.InlineKeyboardButton(text="Testo della risposta", callback_data='voice_text')])
        if translate:
            buttons.append(
                [types.InlineKeyboardButton(text="Traduzione della risposta", callback_data='voice_translate')])
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def level(self, lang):
        available = ('en',)

        buttons = [
            [types.InlineKeyboardButton(text="Sono un principiante", callback_data='level_A1')],
            [types.InlineKeyboardButton(text='A1', callback_data='level_A1'),
             types.InlineKeyboardButton(text='A2', callback_data='level_A2')],
            [types.InlineKeyboardButton(text='B1', callback_data='level_B1'),
             types.InlineKeyboardButton(text='B2', callback_data='level_B2')],
            [types.InlineKeyboardButton(text='C1', callback_data='level_C1')]
            # types.InlineKeyboardButton(text='C2', callback_data='C2')]
        ]
        if lang in available:
            buttons.append([types.InlineKeyboardButton(text='Fai un test', callback_data='test_lang')])

        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def test(self, lang, flag=False):
        available = ('en',)
        buttons = [
            [types.InlineKeyboardButton(text='Indietro 🔙', callback_data='back_to_settings')]
        ]
        if lang in available:
            buttons.extend(
                [[types.InlineKeyboardButton(text="Inizia test veloce! (20 domande)", callback_data='start_test_1')],
                 [types.InlineKeyboardButton(text="Inizia test approfondito! (50 domande)", callback_data='start_test_0')]])
            if flag:
                buttons = [
                    [types.InlineKeyboardButton(text="Inizia il test!", callback_data='start_test_1')]
                ]

        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def final_test(self):
        buttons = [
            [types.InlineKeyboardButton(text="Cambia", callback_data='change')],
            [types.InlineKeyboardButton(text="Mantieni precedente", callback_data='back')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def ready_learn(self):
        buttons = [
            [types.InlineKeyboardButton(text="Andiamo!", callback_data='ex_to_learn')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def dialog(self):
        buttons = [
            [types.InlineKeyboardButton(text="Indietro 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text="Corrispondere", callback_data='dialog_to_start')],
            [types.InlineKeyboardButton(text="Parlare", callback_data='voice')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def menu(self, user):
        buttons = [
            [types.InlineKeyboardButton(text='Informazioni ℹ️', callback_data='info_lang')],
            [types.InlineKeyboardButton(text='Impostazioni ⚙️', callback_data='settings'),
             types.InlineKeyboardButton(text='Il mio dizionario 📕', callback_data='my_dict')],
            [types.InlineKeyboardButton(text='Abilità di ascolto 🎧', callback_data='audio')],
            [types.InlineKeyboardButton(text='Lavorare con il testo 📄', callback_data='writing_skills'),
             types.InlineKeyboardButton(text='Inizia un dialogo 🎙', callback_data='dialog')],
            [types.InlineKeyboardButton(text='Inizia a imparare le parole! 📌', callback_data='start_learn')],
        ]
        # if user in (764124336,):
        #     buttons.append([types.InlineKeyboardButton(text="Админка 👀", callback_data='admin')])
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def writing_skills(self):
        buttons = [
            [types.InlineKeyboardButton(text="Indietro 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text='Traduzione del testo 📖', callback_data='translate_text')],
            [types.InlineKeyboardButton(text='Correzione del tema 📝', callback_data='essay')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def essay(self):
        buttons = [
            [types.InlineKeyboardButton(text="Indietro 🔙", callback_data='writing_skills')],
            [types.InlineKeyboardButton(text='Inizia!', callback_data='essay_start')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def listening(self):
        buttons = [
            [types.InlineKeyboardButton(text="Indietro 🔙", callback_data='back')],
            [types.InlineKeyboardButton(text="Inizia!", callback_data='audio_theme')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def listening_test(self):
        buttons = [
            [types.InlineKeyboardButton(text="Andiamo!", callback_data='audio_test')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def text_symbols(self):
        buttons = [
            [types.InlineKeyboardButton(text='Indietro 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text="1️⃣0️⃣0️⃣", callback_data='symbols_100'),
             types.InlineKeyboardButton(text="2️⃣0️⃣0️⃣", callback_data='symbols_200')],
            [types.InlineKeyboardButton(text="5️⃣0️⃣0️⃣", callback_data='symbols_500'),
             types.InlineKeyboardButton(text="1️⃣0️⃣0️⃣0️⃣", callback_data='symbols_1000')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def my_dict(self):
        buttons = [
            [types.InlineKeyboardButton(text='Indietro 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Aggiungi una frase 🖊', callback_data='add_word')],
            [types.InlineKeyboardButton(text='Stampa lista nella chat 📄', callback_data='print_my_words')],
            [types.InlineKeyboardButton(text='Impara le mie parole', callback_data='learn_my_words')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def info_lang(self):
        buttons = [
            [types.InlineKeyboardButton(text='Indietro 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Progresso livello %', callback_data='info_level')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def back(self):
        buttons = [
            [types.InlineKeyboardButton(text='Indietro 🔙', callback_data='back')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def settings(self):
        buttons = [
            [types.InlineKeyboardButton(text='Indietro 🔙', callback_data='back')],
            [types.InlineKeyboardButton(text='Cambia livello', callback_data='change_level')],
            [types.InlineKeyboardButton(text='Test di conoscenza linguistica', callback_data='test_lang')],
            [types.InlineKeyboardButton(text='Scegli un\'altra lingua', callback_data='change_language')],
            [types.InlineKeyboardButton(text='Scegli l\'argomento delle parole', callback_data='choose_theme')],
            [types.InlineKeyboardButton(text='Cambia il numero di parole per sessione',
                                        callback_data='update_quantity_words')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def change_level(self):
        buttons = [
            [types.InlineKeyboardButton(text='Indietro 🔙', callback_data='back_to_settings')],
            [types.InlineKeyboardButton(text='Aumenta livello', callback_data='up_level')],
            [types.InlineKeyboardButton(text='Diminuisci livello', callback_data='down_level')],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def choose_theme(self):
        buttons = [
            [types.InlineKeyboardButton(text='Indietro 🔙', callback_data='back_to_settings')],
            # [types.InlineKeyboardButton(text='Agricoltura', callback_data='agro')],
            # [types.InlineKeyboardButton(text='Tema 2', callback_data='theme2')],
            # [types.InlineKeyboardButton(text='Tema 3', callback_data='theme3'), types.InlineKeyboardButton(text='Tema 4', callback_data='theme4')],
            # [types.InlineKeyboardButton(text='Tema 5', callback_data='theme5'), types.InlineKeyboardButton(text='Tema 6', callback_data='theme6')],
            # [types.InlineKeyboardButton(text='Continua ad apprendere le parole del livello attuale', callback_data='сontinue_to_study_the_words')],
            # [types.InlineKeyboardButton(text='Voglio solo imparare 5000 parole', callback_data='5000')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard