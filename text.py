class Russian_text:
    greet = 'Здравствуйте, {name}!\nВыберете ваш родной язык'

    choose_language = 'Здравствуйте, {name}!\n\nВыберете какой язык планируете изучать'

    range_learn_words = 'Сколько слов вы готовы учить за сеанс?\nНапишите в чат число от 5 до 30 (включительно)'
    range_learn_words_2 = 'Напишите в чат число от 5 до 30 (включительно)'

    success = 'Регистрация прошла успешна!\n\nВ настройках можно выбрать определенную тематику слов для изучения'

    menu = 'Уважаемый пользователь, это интерактивное меню.\nЗдесь вы можете найти любую интересующую вас информацию.'

    level = 'Какой ваш текущий уровень владения языком?'

    level_info = {'main_words': {'es': 'Ваш процент освоения Испанского языка уровня {level} - {num}%',
                                 'en': 'Ваш процент освоения Английского языка уровня {level} - {num}%',
                                 'de': 'Ваш процент освоения Немецкого языка уровня {level} - {num}%',
                                 'fr': 'Ваш процент освоения Французского языка уровня {level} - {num}%',
                                 'it': 'Ваш процент освоения Итальянского языка уровня {level} - {num}%'},
                  'dict_words': 'Ваш процент освоения слов из словаря - {num}%',
                  "5000": "Ваш процент освоения 5000 слов - {num}%",
                  "agro": 'Ваш процент освоения темы "Сельское хозяйство" - {num}%',
                  'cybersecurity': 'Ваш процент освоения темы "Кибербезопасность" - {num}%',
                  'IT': 'Ваш процент освоения темы "IT" - {num}%'}

    successfully = 'Успешно!'
    successfully_dict = 'Слова '

    maximum = 'У вас максимальный уровень изучения'
    minimum = 'У вас минимальный уровень изучения'

    raised = 'Вы повысили уровень до {level}'
    lowered = 'Вы понизили уровень до {level}'

    change = 'Вы изменили уровень до {level}'

    sorry = 'Извините, но в вашем изучаемом языке нет такой темы слов'

    all_words_learned_0 = 'Это последние слова текущего уровня/темы. После их изучения смело повышайте уровень или выбирайте новую тематику слов!'
    all_words_learned = "Вы выучили все слова текущего уровня/темы\nСамое время повысить уровень\nИли выберете определенную тематику слов"

    translates = '{word} переводится как: {translate}'
    words = 'Список слов которые будем запоминать:'
    words_ = 'И их произношение:'
    words_1 = 'Примеры использования изученных слов!'
    word_split = ' переводится как: '
    ready_learn = 'Все слова запомнили?\nЕсли так смело жмем кнопку 👇'

    Exercise_1 = 'Упражнение 1\n\nВыберете верный ответ'
    Exercise_3 = '{bot_say}\n\nНапишите слово - {translation}\nна изучаемом языке'
    hint = '\n\nПодсказка 😶‍🌫️ {word}'
    Exercise_2 = 'Упражнение 2\n\nВыберете верный ответ'
    wrong_ans = 'Попробуй ещё раз!\n\n'
    bot_say = 'Упражнение 3'

    please_wait = 'Пожалуйста подождите ⏳'
    long_msg = 'Слишком большое сообщение'

    Congratulations = 'Поздравляю с выученными словами!'

    reminder = 'Я пришлю напоминание, когда вам нужно будет повторить слова 😎'

    your_words = 'Ваши слова:\n\n'
    enter_u_word1 = 'Введите слово на изучаемом языке'
    enter_u_word2 = 'Введите перевод слова'
    enter_u_word3 = 'Словосочетание успешно добавлено!'
    empty_dict = 'Пока ваш словарь пустой.'

    Repeat = 'Повторим эти 👇 слова?\n\n{words}'

    good_attempt = (
        'Верно!',
        'Так точно!',
        'Молодец!',
        'Всё так!',
        'Правильно!',
        'Отлично!',
        'Точно!',
        'Ты в ударе!',
        'Красавчик!',
        'Гениально!',
        'Супер!',
        'Легко!',
        'Без ошибок!',
        'Идеально!',
        'Топ!'
    )
    bad_attempt = (
        'Неправильно! Попробуйте еще раз',
        'Неа... не верно',
        'Нет. Подумай еще',
        'Увы, ошибка...',
        'Не совсем так — попробуй снова!',
        'Мимо 😕 Попробуй ещё раз',
        'Не угадал!',
        'Не то. Попробуй другой вариант',
        'Ой, чуть мимо 🙃 Попробуй ещё разок',
        'Ошибка, но ты близок — продолжай!',
        'Почти! Но не совсем правильно',
        'Неверно. Не сдавайся!',
        'Подумай ещё немного',
        'Это не совсем то… давай попробуй ещё раз!',
        'Нет-нет, это неправильно. Продолжай стараться!'
    )
    incomprehensible_set_of_characters = 'Непонятный набор символов\nПожалуйста нажмите /menu\nи проследуйте инструкциям'

    # ДЛЯ ТЕСТИРОВАНИЯ
    test_main = 'Выберите один правильный вариант ответа для каждого вопроса. Тест оценивает вас по шкале CEFR (A1–C1).'
    num_question = 'Вопрос {idx}/{al}\n\n{q}'
    final = 'По результатам теста Ваш уровень - {l}'
    # final_no_mode = 'По результатам теста Ваш уровень - {l}\nПравильных ответов: {corrects} / {num_q}'
    final_no_mode = 'По результатам теста Ваш уровень - {l}\nПравильных ответов: {corrects} / {num_q}\n\nПо уровням:\n- A1 {a1} из {a1o}\n- A2 {a2} из {a2o}\n- B1 {b1} из {b1o}\n- B2 {b2} из {b2o}\n- C1 {c1} из {c1o}'
    not_know = 'Не знаю'

    # LISTENING
    listening_1 = 'Сочиняю аудиодорожку на Вашу тему 🤓'
    listening_3 = 'Напишите в чат название темы текста, который вы бы хотели прослушать.'
    listening_2 = 'Здесь Вы можете попрактиковать навыки аудирования!'
    listening_4 = 'Готовы к проверке Ваших навыков аудирования?'
    listening_5 = 'Вы ответили на все вопросы! Вот текст с которым вы работали:\n\n'

    sww = 'Что-то пошло не так 🧐. Попробуйте снова.'
    # ПЕРЕВОД ТЕКСТА
    translate_text_1 = 'Здесь Вы можете попрактиковать навыки перевода!\n\nВыберете желаемое количество символов в тексте.'
    translate_text_2 = 'Здесь Вы можете попрактиковать навыки перевода!\n\nНапишите в чат название темы текста, который вы бы хотели перевести.'
    translate_text_3 = 'В следующем сообщении отправьте Ваш перевод.'
    translate_text_4 = 'Сочиняю текст на Вашу тему 🤓'
    translate_text_5 = 'Проверяю 🧐 один момент...'
    translate_text_6 = 'Здесь Вы можете попрактиковать навыки работы с текстом!\nВыберете желаемую опцию.'
    # DIALOG
    dialog_1 = 'Здесь Вы можете ввести диалог с не настоящим собеседником на любую тему. В процессе диалога он будет Вас поправлять там где это необходимо. Собеседник подстроится под Ваш уровень. Выберите вариант общения.'
    dialog_2 = 'О чем желаете поговорить?'
    dialog_4 = 'Отправьте текстовое сообщение!'
    dialog_5 = 'Запишите голосовое сообщение!'
    dialog_6 = 'К сожалению, на данный момент поддерживается только английский'
    dialog_7 = "❌ Ошибка генерации голоса. Не удалось озвучить ответ."
    dialog_3 = "Хорошо! Если вы хотите закончить этот разговор, это не проблема. 😊 Не стесняйтесь писать мне в любое время, если захотите попрактиковаться — я всегда рад помочь. Хорошего дня!"
    dialog_cancel = '🔚 Завершить диалог'
    # essay
    essay_1 = 'Здесь Вам бот отправит тему для написания эссе. Тема будет подобрана согласно Вашему текущему уровню. Далее Вы отправляете эссе на проверку, после чего бот направит Вам подробный отчет о проделанной Вами работе.'
    essay_2 = 'Напишите эссе до 1000 знаков на тему: {theme} Отправьте готовое сочинение в следующем сообщении.'
    essay_3 = 'Напишите эссе до 1000 знаков!'
    # You are a friendly native English speaker living in New York City
    SYSTEM_PROMPT = """
        You are a friendly native {lang} speaker. You enjoy helping people learn {lang} and always provide corrections when they make mistakes.

        You will speak with the user at their current language level: {level}.

        Your task:
        1. Respond to the user in clear and natural {lang} that matches their level.
        2. If the user makes grammar or vocabulary mistakes — gently correct them and explain why.
        3. Keep the conversation engaging and relevant to real-life situations, ask questions to encourage the user to reply and practice writing, but not overwhelming — ask one question at a time.
        4. Maintain context from previous messages to keep the dialogue natural.
        5. Use simple words and short sentences if the user is beginner, more complex ones if they're advanced.
        6. Be warm and supportive, like a friend who helps with {lang} practice.
            """

    VOICE_PROMPT = """
        You are a friendly native {lang} speaker. You enjoy having casual and engaging conversations with learners of {lang}.

        You will speak with the user at their current language level: {level}.

        Your task:
        1. Respond naturally in {lang}, using vocabulary that matches their level.
        2. Do NOT ADD notes, various information in brackets, emoji, explanations, or formatting — just speak like a real person, otherwise it will cause errors.
        3. Keep the conversation flowing by asking one question at a time.
        4. Make your replies sound like part of a normal chat — not like lessons or tests.
        5. Maintain context from previous messages to keep the dialogue natural.
        6. Use simple words and short sentences for beginners; more complex ones for advanced users.
        7. Be warm, curious, and supportive — like a friend who wants to chat in {lang}.
            """
        # 2. Do not add notes, emoji, explanations, or formatting — just speak like a real person.

class English_text:
    greet = 'Hello, {name}!\nChoose your native language'

    choose_language = 'Hello, {name}!\n\nSelect the language you plan to learn'

    range_learn_words = 'How many words are you ready to learn per session?\nWrite a number from 5 to 30 (inclusive) in chat'
    range_learn_words_2 = 'Write a number from 5 to 30 (inclusive) in chat'

    success = 'Registration was successful!\n\nIn settings, you can choose specific word themes for learning'

    menu = 'Dear user, this is an interactive menu.\nHere you can find any information you are interested in.'

    level = 'What is your current level of language proficiency?'

    level_info = {'main_words': "Your percentage of mastering English at the {level} level is {num}%",
                  "dict_words": "Your percentage of word mastery from the dictionary is {num}%",
                  "5000": "Your percentage of mastering 5000 words is {num}%",
                  "agro": 'Your percentage of mastering the topic "Agriculture" is {num}%',
                  "cybersecurity": 'Your percentage of mastering the topic "Cybersecurity" is {num}%',
                  "IT": 'Your percentage of mastering the topic "IT" is {num}%'}

    successfully = 'Successfully!'
    successfully_dict = 'Words '

    maximum = 'You have reached the maximum learning level'
    minimum = 'You are at the minimum learning level'

    raised = 'You have upgraded your level to {level}'
    lowered = 'You have downgraded your level to {level}'

    change = 'You changed your level to {level}'

    sorry = 'Sorry, but there is no such word theme in your target language'

    all_words_learned_0 = "These are the last words of the current level/topic. After learning them, feel free to increase the level or choose a new word theme!"
    all_words_learned = "You have learned all the words of the current level/theme\nIt's time to increase the level\nOr select a specific word theme"

    translates = '{word} translates as: {translate}'
    words = 'List of words to memorize:'
    words_ = 'And their pronunciation:'
    words_1 = 'Examples of how to use the learned words!'
    word_split = ' translates as: '
    ready_learn = 'Have you memorized all the words?\nIf so, press the button 👇'

    Exercise_1 = 'Exercise 1\n\nChoose the correct answer'
    Exercise_3 = '{bot_say}\n\nWrite the word - {translation}\nin the target language'
    hint = '\n\nHint 😶‍🌫️ {word}'
    Exercise_2 = 'Exercise 2\n\nChoose the correct answer'
    wrong_ans = 'Try again!\n\n'
    bot_say = 'Exercise 3'

    please_wait = 'Please wait ⏳'
    long_msg = 'Message is too long'

    Congratulations = 'Congratulations on mastering the new words!'

    reminder = 'I will send you a reminder when it’s time to review the words 😎'

    your_words = 'Your words:\n\n'
    enter_u_word1 = 'Enter a word in the target language'
    enter_u_word2 = 'Enter the translation of the word'
    enter_u_word3 = 'Phrase successfully added!'
    empty_dict = 'Your dictionary is empty for now.'

    Repeat = "Let's repeat these 👇 words?\n\n{words}"

    good_attempt = (
        'Correct!',
        'Exactly!',
        'Well done!',
        'That’s right!',
        'Perfect!',
        'Great job!',
        'You got it!',
        'You’re on fire!',
        'Awesome!',
        'Genius!',
        'Superb!',
        'Easy peasy!',
        'No mistakes!',
        'Spot on!',
        'Top-notch!'
    )
    bad_attempt = (
        'Wrong! Try again.',
        'Nope… not quite.',
        'No. Think again.',
        'Oops, mistake...',
        'Not quite — try again!',
        'Missed 😕 Try once more.',
        'No luck!',
        'Not the right one. Try another option.',
        'So close! 🙃 Try again.',
        'Mistake, but you’re getting closer — keep going!',
        'Almost! But not quite right.',
        'Incorrect. Don’t give up!',
        'Think again for a second.',
        'Not exactly that… try again!',
        'No no, that’s wrong. Keep practicing!'
    )
    incomprehensible_set_of_characters = 'Unintelligible set of characters\nPlease press /menu\nand follow the instructions'

    # FOR TESTING
    test_main = 'Choose one correct answer for each question. The test assesses you on the CEFR scale (A1–C1).'
    num_question = 'Question {idx}/{al}\n\n{q}'
    final = 'Based on the test results, your level is {l}'
    final_no_mode = 'Based on the test results, your level is {l}\nCorrect answers: {corrects} / {num_q}\n\nBy levels:\n- A1 {a1} out of {a1o}\n- A2 {a2} out of {a2o}\n- B1 {b1} out of {b1o}\n- B2 {b2} out of {b2o}\n- C1 {c1} out of {c1o}'
    not_know = 'I don\'t know'

    # LISTENING
    listening_1 = "Composing an audio track on your topic 🤓"
    listening_3 = "Write the topic of the text you would like to listen to in chat."
    listening_2 = "Here you can practice your listening skills!"
    listening_4 = "Ready to test your listening skills?"
    listening_5 = "You've answered all the questions! Here's the text you worked with:\n\n"

    sww = "Something went wrong 🧐. Please try again."

    # TRANSLATION
    translate_text_1 = "Here you can practice your translation skills!\n\nChoose the desired number of characters in the text."
    translate_text_2 = "Here you can practice your translation skills!\n\nWrite the topic of the text you would like to translate in the chat."
    translate_text_3 = "Send your translation in the next message."
    translate_text_4 = "Composing text on your topic 🤓"
    translate_text_5 = "Checking 🧐 one thing..."
    translate_text_6 = "Here you can practice your text editing skills!\nChoose the desired option."

    # DIALOGUE
    dialog_1 = "Here you can have a conversation with a virtual partner on any topic. During the dialogue, they will correct you where necessary. The partner will adapt to your level. Choose a communication option."
    dialog_2 = "What would you like to talk about?"
    dialog_4 = 'Send a text message!'
    dialog_5 = 'Record a voice message!'
    dialog_6 = 'Unfortunately, only English is currently supported.'
    dialog_7 = "❌ Voice generation error. Couldn't voice the answer."
    dialog_3 = "Okay! If you'd like to end this conversation, that's no problem. 😊 Feel free to message me again anytime if you want to practice — I'm always happy to help. Have a great day!"
    dialog_cancel = '🔚 End the dialog'
    essay_1 = 'Here, the bot will send you a topic for writing an essay. The topic will be selected according to your current level. Then you send your essay for review, after which the bot will send you a detailed report on your work.'
    essay_2 = 'Write an essay of up to 1000 characters on the theme: {theme}. Send your completed essay in the next message.'
    essay_3 = 'Write an essay of up to 1000 characters!'
    # You are a friendly native English speaker living in New York City
    SYSTEM_PROMPT = """
        You are a friendly native {lang} speaker. You enjoy helping people learn {lang} and always provide corrections when they make mistakes.

        You will speak with the user at their current language level: {level}.

        Your task:
        1. Respond to the user in clear and natural {lang} that matches their level.
        2. If the user makes grammar or vocabulary mistakes — gently correct them and explain why.
        3. Keep the conversation engaging and relevant to real-life situations, ask questions to encourage the user to reply and practice writing, but not overwhelming — ask one question at a time.
        4. Maintain context from previous messages to keep the dialogue natural.
        5. Use simple words and short sentences if the user is beginner, more complex ones if they're advanced.
        6. Be warm and supportive, like a friend who helps with {lang} practice.
        """

    VOICE_PROMPT = """
        You are a friendly native {lang} speaker. You enjoy having casual and engaging conversations with learners of {lang}.

        You will speak with the user at their current language level: {level}.

        Your task:
        1. Respond naturally in {lang}, using vocabulary that matches their level.
        2. Do not add notes, various information in brackets, emoji, explanations, or formatting — just speak like a real person, otherwise it will cause errors.
        3. Keep the conversation flowing by asking one question at a time.
        4. Make your replies sound like part of a normal chat — not like lessons or tests.
        5. Maintain context from previous messages to keep the dialogue natural.
        6. Use simple words and short sentences for beginners; more complex ones for advanced users.
        7. Be warm, curious, and supportive — like a friend who wants to chat in {lang}.
        """

class Spanish_text:
    greet = 'Hola, {name}!\nElige tu idioma nativo'

    choose_language = 'Hola, {name}!\n\nSelecciona el idioma que deseas aprender'

    range_learn_words = '¿Cuántas palabras estás dispuesto a aprender por sesión?\nEscribe un número del 5 al 30 (ambos incluidos) en el chat'
    range_learn_words_2 = 'Escribe un número del 5 al 30 (ambos incluidos) en el chat'

    success = '¡Registro exitoso!\n\nEn la configuración puedes elegir temas específicos de palabras para aprender'

    menu = 'Estimado usuario, este es un menú interactivo.\nAquí puedes encontrar cualquier información que te interese.'

    level = '¿Cuál es tu nivel actual de dominio del idioma?'

    level_info = {'main_words': "Tu porcentaje de dominio del español en el nivel {level} es {num}%",
                  "dict_words": "Tu porcentaje de dominio de palabras del diccionario es {num}%",
                  "5000": "Tu porcentaje de dominio de 5000 palabras es {num}%",
                  "agro": "Tu porcentaje de dominio del tema 'Agricultura' es {num}%",
                  "cybersecurity": "Tu porcentaje de dominio del tema 'Ciberseguridad' es {num}%",
                  "IT": "Tu porcentaje de dominio del tema 'TI' (Tecnologías de la Información) es {num}%"}

    successfully = '¡Éxito!'
    successfully_dict = 'Palabras '

    maximum = 'Has alcanzado el nivel máximo de aprendizaje'
    minimum = 'Estás en el nivel mínimo de aprendizaje'

    raised = 'Has subido tu nivel a {level}'
    lowered = 'Has bajado tu nivel a {level}'

    change = 'Has cambiado tu nivel a {level}'

    sorry = 'Lo sentimos, pero no existe este tema de palabras en tu idioma objetivo'

    all_words_learned_0 = "Estas son las últimas palabras del nivel/tema actual. Después de aprenderlas, puedes aumentar el nivel o elegir un nuevo tema de palabras."
    all_words_learned = "Has aprendido todas las palabras del nivel/tema actual\nEs hora de subir de nivel\no seleccionar un tema específico de palabras"

    translates = '{word} se traduce como: {translate}'
    words = 'Lista de palabras para memorizar:'
    words_ = 'Y su pronunciación:'
    words_1 = '¡Ejemplos de cómo usar las palabras aprendidas!'
    word_split = ' se traduce como: '
    ready_learn = '¿Has memorizado todas las palabras?\nSi es así, pulsa el botón 👇'

    Exercise_1 = 'Ejercicio 1\n\nElige la respuesta correcta'
    Exercise_3 = '{bot_say}\n\nEscribe la palabra - {translation}\nen el idioma objetivo'
    hint = '\n\nPista 😶‍🌫️ {word}'
    Exercise_2 = 'Ejercicio 2\n\nElige la respuesta correcta'
    wrong_ans = '¡Inténtalo de nuevo!\n\n'
    bot_say = 'Ejercicio 3'

    please_wait = 'Por favor, espera ⏳'
    long_msg = 'El mensaje es demasiado largo'

    Congratulations = '¡Felicitaciones por dominar las nuevas palabras!'

    reminder = 'Te enviaré un recordatorio cuando sea hora de repasar las palabras 😎'

    your_words = 'Tus palabras:\n\n'
    enter_u_word1 = 'Introduce una palabra en el idioma objetivo'
    enter_u_word2 = 'Introduce la traducción de la palabra'
    enter_u_word3 = '¡Frase agregada con éxito!'
    empty_dict = 'Tu diccionario está vacío por ahora.'

    Repeat = "¿Repetimos estas palabras 👇?\n\n{words}"

    good_attempt = (
        '¡Correcto!',
        '¡Exacto!',
        '¡Bien hecho!',
        '¡Así es!',
        '¡Perfecto!',
        '¡Gran trabajo!',
        '¡Lo lograste!',
        '¡Vas como un rayo!',
        '¡Impresionante!',
        '¡Eres un genio!',
        '¡Excelente!',
        '¡Pan comido!',
        '¡Sin errores!',
        '¡Justo en el blanco!',
        '¡De primera!'
    )
    bad_attempt = (
        'Incorrecto. Inténtalo de nuevo.',
        'No… no es así.',
        'No. Piénsalo otra vez.',
        'Oops, error...',
        'No del todo — inténtalo de nuevo.',
        'Fallaste 😕 Inténtalo una vez más.',
        'Sin suerte.',
        'No es esa. Prueba otra opción.',
        '¡Tan cerca! 🙃 Inténtalo otra vez.',
        'Error, pero ya estás más cerca — sigue adelante.',
        '¡Casi! Pero no es del todo correcto.',
        'Incorrecto. ¡No te rindas!',
        'Piénsalo un segundo más.',
        'No exactamente eso… inténtalo de nuevo.',
        'No no, eso está mal. ¡Sigue practicando!'
    )
    incomprehensible_set_of_characters = 'Conjunto de caracteres incomprensible\nPor favor, presiona /menu\ny sigue las instrucciones'

    # FOR TESTING
    test_main = 'Elige una respuesta correcta para cada pregunta. La prueba evalúa tu nivel de vocabulario según la escala del MCER (A1–C1).'
    num_question = 'Pregunta {idx}/{al}\n\n{q}'
    final = 'Según los resultados de la prueba, tu nivel es {l}\n¿Te gustaría cambiar tu nivel actual?'
    final_no_mode = 'Según los resultados de la prueba, tu nivel es {l}\nPreguntas correctas: {corrects} / 50\n\nPor niveles:\n- A1 {a1} de 10\n- A2 {a2} de 10\n- B1 {b1} de 10\n- B2 {b2} de 10\n- C1 {c1} de 10'
    not_know = 'No sé'

    # LISTENING
    listening_1 = "Componiendo una pista de audio sobre tu tema 🤓"
    listening_3 = "Escribe en el chat el tema del texto que te gustaría escuchar."
    listening_2 = "¡Aquí puedes practicar tus habilidades auditivas!"
    listening_4 = "¿Listo para probar tus habilidades auditivas?"
    listening_5 = "¡Has respondido todas las preguntas! Aquí está el texto con el que trabajaste:\n\n"

    sww = "Algo salió mal 🧐. Por favor, inténtalo de nuevo."

    # TRANSLATION
    translate_text_1 = "¡Aquí puedes practicar tus habilidades de traducción!\n\nElige el número deseado de caracteres en el texto."
    translate_text_2 = "¡Aquí puedes practicar tus habilidades de traducción!\n\nEscribe en el chat el tema del texto que te gustaría traducir."
    translate_text_3 = "Envía tu traducción en el siguiente mensaje."
    translate_text_4 = "Componiendo texto sobre tu tema 🤓"
    translate_text_5 = "Verificando 🧐 una cosa..."
    translate_text_6 = "¡Aquí puedes practicar tus habilidades de edición de textos!\nElige la opción deseada."

    # DIALOGUE
    dialog_1 = "Aquí puedes tener una conversación con un compañero virtual sobre cualquier tema. Durante el diálogo, te corregirá cuando sea necesario. El compañero se adaptará a tu nivel. Elige una opción de comunicación."
    dialog_2 = "¿Sobre qué te gustaría hablar?"
    dialog_4 = '¡Envía un mensaje de texto!'
    dialog_5 = '¡Graba un mensaje de voz!'
    dialog_6 = 'Desafortunadamente, actualmente solo se admite inglés.'
    dialog_7 = "❌ Error en la generación de voz. No se pudo vocalizar la respuesta."
    dialog_3 = "¡Bien! Si deseas terminar esta conversación, no hay problema. 😊 Siempre puedes escribirme cuando quieras practicar — siempre estoy encantado de ayudarte. ¡Que tengas un buen día!"
    dialog_cancel = '🔚 Finalizar el diálogo'
    essay_1 = 'Aquí, el bot te enviará un tema para escribir un ensayo. El tema se seleccionará según tu nivel actual. Luego envías tu ensayo para revisión, tras lo cual el bot te enviará un informe detallado sobre tu trabajo.'
    essay_2 = 'Escribe un ensayo de hasta 1000 caracteres sobre el tema: {theme}. Envía tu ensayo completado en el siguiente mensaje.'
    essay_3 = 'Escribe un ensayo de hasta 1000 caracteres.'
    SYSTEM_PROMPT = """
            You are a friendly native {lang} speaker. You enjoy helping people learn {lang} and always provide corrections when they make mistakes.

            You will speak with the user at their current language level: {level}.

            Your task:
            1. Respond to the user in clear and natural {lang} that matches their level.
            2. If the user makes grammar or vocabulary mistakes — gently correct them and explain why.
            3. Keep the conversation engaging and relevant to real-life situations, ask questions to encourage the user to reply and practice writing, but not overwhelming — ask one question at a time.
            4. Maintain context from previous messages to keep the dialogue natural.
            5. Use simple words and short sentences if the user is beginner, more complex ones if they're advanced.
            6. Be warm and supportive, like a friend who helps with {lang} practice.
            """
    VOICE_PROMPT = """
            You are a friendly native {lang} speaker. You enjoy having casual and engaging conversations with learners of {lang}.

            You will speak with the user at their current language level: {level}.

            Your task:
            1. Respond naturally in {lang}, using vocabulary that matches their level.
            2. Do not add notes, various information in brackets, emoji, explanations, or formatting — just speak like a real person, otherwise it will cause errors.
            3. Keep the conversation flowing by asking one question at a time.
            4. Make your replies sound like part of a normal chat — not like lessons or tests.
            5. Maintain context from previous messages to keep the dialogue natural.
            6. Use simple words and short sentences for beginners; more complex ones for advanced users.
            7. Be warm, curious, and supportive — like a friend who wants to chat in {lang}.
            """

class German_text:
    greet = 'Hallo, {name}!\nWähle deine Muttersprache'

    choose_language = 'Hallo, {name}!\n\nWähle die Sprache, die du lernen möchtest'

    range_learn_words = 'Wie viele Wörter bist du pro Sitzung bereit zu lernen?\nSchreibe eine Zahl von 5 bis 30 (jeweils inklusive) in den Chat'
    range_learn_words_2 = 'Schreibe eine Zahl von 5 bis 30 (jeweils inklusive) in den Chat'

    success = 'Die Registrierung war erfolgreich!\n\nIn den Einstellungen kannst du spezifische Wörterthemen zum Lernen auswählen'

    menu = 'Sehr geehrter Nutzer, dies ist ein interaktives Menü.\nHier findest du alle Informationen, die dich interessieren.'

    level = 'Was ist dein aktuelles Sprachniveau?'

    level_info = {"main_words": "Ihr Anteil an Deutschkenntnissen auf der Ebene {level} beträgt {num}%",
                  "dict_words": "Ihr Prozentsatz der Wortbeherrschung aus dem Wörterbuch beträgt {num}%",
                  "5000": "Ihr Prozentsatz der Beherrschung von 5000 Wörtern beträgt {num}%",
                  "agro": "Ihr Prozentsatz der Beherrschung des Themas 'Landwirtschaft' beträgt {num}%",
                  "cybersecurity": "Ihr Prozentsatz der Beherrschung des Themas 'Cybersicherheit' beträgt {num}%",
                  "IT": "Ihr Prozentsatz der Beherrschung des Themas 'IT' (Informationstechnologie) beträgt {num}%"}

    successfully = 'Erfolgreich!'
    successfully_dict = 'Wörter '

    maximum = 'Du hast das maximale Lernniveau erreicht'
    minimum = 'Du befindest dich auf dem minimalen Lernniveau'

    raised = 'Du hast dein Niveau auf {level} erhöht'
    lowered = 'Du hast dein Niveau auf {level} gesenkt'

    change = 'Du hast dein Niveau auf {level} geändert'

    sorry = 'Entschuldigung, aber dieses Wörterthema existiert nicht in deiner Zielsprache'

    all_words_learned_0 = "Das sind die letzten Wörter des aktuellen Niveaus/themas. Nach dem Lernen kannst du das Niveau erhöhen oder ein neues Wörterthema wählen!"
    all_words_learned = "Du hast alle Wörter des aktuellen Niveaus/Themas gelernt\nEs ist Zeit, das Niveau zu erhöhen\nOder ein spezifisches Wörterthema auszuwählen"

    translates = '{word} bedeutet: {translate}'
    words = 'Liste der Wörter zum Auswendiglernen:'
    words_ = 'Und ihre Aussprache:'
    words_1 = 'Beispiele für die Verwendung der gelernten Wörter!'
    word_split = ' bedeutet: '
    ready_learn = 'Hast du alle Wörter gelernt?\nWenn ja, drücke den Button unten 👇'

    Exercise_1 = 'Übung 1\n\nWähle die richtige Antwort'
    Exercise_3 = '{bot_say}\n\nSchreibe das Wort – {translation}\nin der Zielsprache'
    hint = '\n\nTipp 😶‍🌫️ {word}'
    Exercise_2 = 'Übung 2\n\nWähle die richtige Antwort'
    wrong_ans = 'Versuche es nochmal!\n\n'
    bot_say = 'Übung 3'

    please_wait = 'Bitte warte ⏳'
    long_msg = 'Nachricht ist zu lang'

    Congratulations = 'Herzlichen Glückwunsch zum Erlernen der neuen Wörter!'

    reminder = 'Ich schicke dir eine Erinnerung, wenn es Zeit ist, die Wörter zu wiederholen 😎'

    your_words = 'Deine Wörter:\n\n'
    enter_u_word1 = 'Gib ein Wort in der Zielsprache ein'
    enter_u_word2 = 'Gib die Übersetzung des Wortes ein'
    enter_u_word3 = 'Phrase erfolgreich hinzugefügt!'
    empty_dict = 'Dein Wörterbuch ist vorerst leer.'

    Repeat = "Wollen wir diese 👇 Wörter wiederholen?\n\n{words}"

    good_attempt = (
        'Richtig!',
        'Genau!',
        'Gut gemacht!',
        'Das stimmt!',
        'Perfekt!',
        'Tolle Leistung!',
        'Das hast du richtig!',
        'Du brennst heute!',
        'Fantastisch!',
        'Genial!',
        'Hervorragend!',
        'Kinderspiel!',
        'Kein Fehler!',
        'Volltreffer!',
        'Erstklassig!'
    )
    bad_attempt = (
        'Falsch! Versuche es erneut.',
        'Nein… nicht ganz.',
        'Nein. Überlege nochmal.',
        'Ups, Fehler...',
        'Nicht ganz — versuche es nochmal!',
        'Leider daneben 😕 Versuche es noch einmal.',
        'Kein Glück!',
        'Nicht das richtige. Versuche eine andere Option.',
        'So nah dran! 🙃 Versuche es nochmal.',
        'Fehler, aber du kommst näher — weiter so!',
        'Fast! Aber noch nicht ganz richtig.',
        'Falsch. Gib nicht auf!',
        'Überlege noch einmal kurz.',
        'Nicht genau das… versuche es erneut!',
        'Nein nein, das ist falsch. Übe weiter!'
    )
    incomprehensible_set_of_characters = 'Unverständliche Zeichenfolge\nBitte drücke /menu\nund folge den Anweisungen'

    # FOR TESTING
    test_main = 'Wähle jeweils eine richtige Antwort pro Frage. Der Test bewertet dein Vokabularniveau nach dem Gemeinsamen Europäischen Referenzrahmen (GER, A1–C1).'
    num_question = 'Frage {idx}/{al}\n\n{q}'
    final = 'Basierend auf den Testergebnissen ist dein Niveau {l}\nMöchtest du dein aktuelles Niveau ändern?'
    final_no_mode = 'Basierend auf den Testergebnissen ist dein Niveau {l}\nRichtige Antworten: {corrects} / 50\n\nNach Niveaus:\n- A1 {a1} von 10\n- A2 {a2} von 10\n- B1 {b1} von 10\n- B2 {b2} von 10\n- C1 {c1} von 10'
    not_know = 'Ich weiß nicht'

    # LISTENING
    listening_1 = "Erstelle einen Audiotrack zu deinem Thema 🤓"
    listening_3 = "Schreibe das Thema des Textes, den du gerne hören möchtest, in den Chat."
    listening_2 = "Hier kannst du dein Hörverständnis trainieren!"
    listening_4 = "Bist du bereit, dein Hörverständnis zu testen?"
    listening_5 = "Du hast alle Fragen beantwortet! Hier ist der Text, mit dem du gearbeitet hast:\n\n"

    sww = "Etwas ist schiefgelaufen 🧐. Bitte versuche es erneut."

    # TRANSLATION
    translate_text_1 = "Hier kannst du deine Übersetzungsfähigkeiten trainieren!\n\nWähle die gewünschte Anzahl an Zeichen im Text."
    translate_text_2 = "Hier kannst du deine Übersetzungsfähigkeiten trainieren!\n\nSchreibe das Thema des Textes, den du übersetzen möchtest, in den Chat."
    translate_text_3 = "Sende deine Übersetzung in der nächsten Nachricht."
    translate_text_4 = "Erstelle Text zu deinem Thema 🤓"
    translate_text_5 = "Überprüfe 🧐 eine Sache..."
    translate_text_6 = "Hier kannst du deine Textbearbeitungsfähigkeiten trainieren!\nWähle die gewünschte Option."

    # DIALOGUE
    dialog_1 = "Hier kannst du mit einem virtuellen Partner über jedes beliebige Thema sprechen. Während des Dialogs wird er dich bei Bedarf korrigieren. Der Partner passt sich deinem Niveau an. Wähle eine Kommunikationsoption."
    dialog_2 = "Worüber möchtest du sprechen?"
    dialog_4 = 'Sende eine Textnachricht!'
    dialog_5 = 'Sprich eine Sprachnachricht auf!'
    dialog_6 = 'Leider wird derzeit nur Englisch unterstützt.'
    dialog_7 = "❌ Fehler bei der Sprachgenerierung. Die Antwort konnte nicht ausgesprochen werden."
    dialog_3 = "Alles klar! Wenn du dieses Gespräch beenden möchtest, ist das kein Problem. 😊 Schreib mir jederzeit wieder, wenn du üben möchtest — ich helfe gern. Einen schönen Tag noch!"
    dialog_cancel = '🔚 Dialog beenden'
    essay_1 = 'Hier sendet dir der Bot ein Thema für einen Aufsatz. Das Thema wird entsprechend deines aktuellen Niveaus ausgewählt. Danach sendest du deinen Aufsatz zur Überprüfung, woraufhin der Bot dir einen detaillierten Bericht zu deiner Arbeit schickt.'
    essay_2 = 'Schreibe einen Aufsatz mit bis zu 1000 Zeichen zum Thema: {theme}. Sende deinen fertigen Aufsatz in der nächsten Nachricht.'
    essay_3 = 'Schreibe einen Aufsatz mit bis zu 1000 Zeichen!'
    SYSTEM_PROMPT = """
            You are a friendly native {lang} speaker. You enjoy helping people learn {lang} and always provide corrections when they make mistakes.

            You will speak with the user at their current language level: {level}.

            Your task:
            1. Respond to the user in clear and natural {lang} that matches their level.
            2. If the user makes grammar or vocabulary mistakes — gently correct them and explain why.
            3. Keep the conversation engaging and relevant to real-life situations, ask questions to encourage the user to reply and practice writing, but not overwhelming — ask one question at a time.
            4. Maintain context from previous messages to keep the dialogue natural.
            5. Use simple words and short sentences if the user is beginner, more complex ones if they're advanced.
            6. Be warm and supportive, like a friend who helps with {lang} practice.
            """
    VOICE_PROMPT = """
            You are a friendly native {lang} speaker. You enjoy having casual and engaging conversations with learners of {lang}.

            You will speak with the user at their current language level: {level}.

            Your task:
            1. Respond naturally in {lang}, using vocabulary that matches their level.
            2. Do not add notes, various information in brackets, emoji, explanations, or formatting — just speak like a real person, otherwise it will cause errors.
            3. Keep the conversation flowing by asking one question at a time.
            4. Make your replies sound like part of a normal chat — not like lessons or tests.
            5. Maintain context from previous messages to keep the dialogue natural.
            6. Use simple words and short sentences for beginners; more complex ones for advanced users.
            7. Be warm, curious, and supportive — like a friend who wants to chat in {lang}.
            """

class French_text:
    greet = 'Bonjour, {name} !\nChoisissez votre langue maternelle'

    choose_language = 'Bonjour, {name} !\n\nSélectionnez la langue que vous souhaitez apprendre'

    range_learn_words = 'Combien de mots êtes-vous prêt à apprendre par séance ?\nÉcrivez un nombre de 5 à 30 (inclus) dans le chat'
    range_learn_words_2 = 'Écrivez un nombre de 5 à 30 (inclus) dans le chat'

    success = 'Inscription réussie !\n\nDans les paramètres, vous pouvez choisir des thèmes spécifiques de mots à apprendre'

    menu = 'Cher utilisateur, ceci est un menu interactif.\nVous y trouverez toutes les informations qui vous intéressent.'

    level = 'Quel est votre niveau actuel de maîtrise de la langue ?'

    level_info = {"main_words": "Votre pourcentage d'allemand au niveau {level} est {num}%",
                  "dict_words": "Votre pourcentage de maîtrise des mots du dictionnaire est de {num}%",
                  "5000": "Votre pourcentage de maîtrise de 5000 mots est de {num}%",
                  "agro": "Votre pourcentage de maîtrise du thème 'Agriculture' est de {num}%",
                  "cybersecurity": "Votre pourcentage de maîtrise du thème 'Cybersécurité' est de {num}%",
                  "IT": "Votre pourcentage de maîtrise du thème 'IT' (Technologies de l'Information) est de {num}%"}

    successfully = 'Avec succès !'
    successfully_dict = 'Mots '

    maximum = 'Vous avez atteint le niveau d\'apprentissage maximal'
    minimum = 'Vous êtes au niveau d\'apprentissage minimal'

    raised = 'Vous avez augmenté votre niveau à {level}'
    lowered = 'Vous avez réduit votre niveau à {level}'

    change = 'Vous avez changé votre niveau à {level}'

    sorry = 'Désolé, mais il n\'existe pas de thème de mots correspondant dans votre langue cible'

    all_words_learned_0 = "Ce sont les derniers mots du niveau/thème actuel. Après les avoir appris, n'hésitez pas à augmenter le niveau ou à choisir un nouveau thème de mots !"
    all_words_learned = "Vous avez appris tous les mots du niveau/thème actuel\nIl est temps d'augmenter le niveau\nOu de sélectionner un thème de mots spécifique"

    translates = '{word} se traduit par : {translate}'
    words = 'Liste des mots à mémoriser :'
    words_ = 'Et leur prononciation :'
    words_1 = 'Exemples d\'utilisation des mots appris !'
    word_split = ' se traduit par : '
    ready_learn = 'Avez-vous mémorisé tous les mots ?\nSi oui, appuyez sur le bouton 👇'

    Exercise_1 = 'Exercice 1\n\nChoisissez la bonne réponse'
    Exercise_3 = '{bot_say}\n\nÉcrivez le mot - {translation}\nen langue cible'
    hint = '\n\nIndice 😶‍🌫️ {word}'
    Exercise_2 = 'Exercice 2\n\nChoisissez la bonne réponse'
    wrong_ans = 'Réessayez !\n\n'
    bot_say = 'Exercice 3'

    please_wait = 'Veuillez patienter ⏳'
    long_msg = 'Le message est trop long'

    Congratulations = 'Félicitations pour la maîtrise des nouveaux mots !'

    reminder = 'Je vous enverrai un rappel quand il sera temps de revoir les mots 😎'

    your_words = 'Vos mots :\n\n'
    enter_u_word1 = 'Saisissez un mot dans la langue cible'
    enter_u_word2 = 'Saisissez la traduction du mot'
    enter_u_word3 = 'Expression ajoutée avec succès !'
    empty_dict = 'Votre dictionnaire est vide pour l\'instant.'

    Repeat = 'Répétons ces mots 👇 ?\n\n{words}'

    good_attempt = (
        'Correct !',
        'Exactement !',
        'Bien joué !',
        'C\'est ça !',
        'Parfait !',
        'Excellent travail !',
        'Vous l\'avez trouvé !',
        'Vous êtes en feu !',
        'Impressionnant !',
        'Génial !',
        'Superbe !',
        'Facile !',
        'Sans erreur !',
        'Parfaitement exact !',
        'Excellent !'
    )
    bad_attempt = (
        'Faux ! Essayez encore.',
        'Non… pas tout à fait.',
        'Non. Réfléchissez encore.',
        'Oups, erreur...',
        'Pas tout à fait — réessayez !',
        'À côté 😕 Essayez encore.',
        'Pas de chance !',
        'Ce n\'est pas ça. Essayez une autre option.',
        'Si proche ! 🙃 Réessayez.',
        'Erreur, mais vous vous rapprochez — continuez !',
        'Presque ! Mais pas tout à fait correct.',
        'Incorrect. Ne lâchez pas !',
        'Réfléchissez encore un peu.',
        'Ce n\'est pas exactement cela… essayez encore !',
        'Non non, c\'est faux. Continuez à pratiquer !'
    )
    incomprehensible_set_of_characters = 'Ensemble de caractères incompréhensible\nVeuillez appuyer sur /menu\net suivre les instructions'

    # POUR LES TESTS
    test_main = 'Choisissez une réponse correcte pour chaque question. Ce test évalue votre niveau de vocabulaire selon l\'échelle CECR (A1–C1).'
    num_question = 'Question {idx}/{al}\n\n{q}'
    final = 'D\'après les résultats du test, votre niveau est {l}\nSouhaitez-vous modifier votre niveau actuel ?'
    final_no_mode = 'D\'après les résultats du test, votre niveau est {l}\nRéponses correctes : {corrects} / 50\n\nPar niveaux :\n- A1 {a1} sur 10\n- A2 {a2} sur 10\n- B1 {b1} sur 10\n- B2 {b2} sur 10\n- C1 {c1} sur 10'
    not_know = 'Je ne sais pas'

    # ÉCOUTE
    listening_1 = "Composition d'une piste audio sur votre thème 🤓"
    listening_3 = "Écrivez dans le chat le thème du texte que vous aimeriez écouter."
    listening_2 = "Ici, vous pouvez pratiquer vos compétences en compréhension orale !"
    listening_4 = "Prêt à tester vos compétences en écoute ?"
    listening_5 = "Vous avez répondu à toutes les questions ! Voici le texte avec lequel vous avez travaillé :\n\n"

    sww = "Quelque chose s'est mal passé 🧐. Veuillez réessayer."

    # TRADUCTION
    translate_text_1 = "Ici, vous pouvez pratiquer vos compétences en traduction !\n\nChoisissez le nombre souhaité de caractères dans le texte."
    translate_text_2 = "Ici, vous pouvez pratiquer vos compétences en traduction !\n\nÉcrivez dans le chat le thème du texte que vous aimeriez traduire."
    translate_text_3 = "Envoyez votre traduction dans le prochain message."
    translate_text_4 = "Rédaction d'un texte sur votre thème 🤓"
    translate_text_5 = "Vérification 🧐 une seconde..."
    translate_text_6 = "Ici, vous pouvez pratiquer vos compétences en traitement de texte !\nChoisissez l'option souhaitée."

    # DIALOGUE
    dialog_1 = "Ici, vous pouvez avoir une conversation avec un partenaire virtuel sur n'importe quel sujet. Pendant le dialogue, il vous corrigera si nécessaire. Le partenaire s'adaptera à votre niveau. Choisissez une option de communication."
    dialog_2 = "De quoi aimeriez-vous parler ?"
    dialog_4 = 'Envoyez un message texte !'
    dialog_5 = 'Enregistrez un message vocal !'
    dialog_6 = 'Malheureusement, seul l\'anglais est actuellement pris en charge.'
    dialog_7 = "❌ Erreur de génération vocale. Impossible de vocaliser la réponse."
    dialog_3 = "D\'accord ! Si vous souhaitez mettre fin à cette conversation, aucun problème. 😊 N'hésitez pas à me recontacter à tout moment si vous voulez vous entraîner — je suis toujours heureux de vous aider. Passez une excellente journée !"
    dialog_cancel = '🔚 Terminer le dialogue'

    # ESSAI
    essay_1 = 'Ici, le bot vous enverra un sujet de rédaction d\'essai. Le sujet sera choisi en fonction de votre niveau actuel. Ensuite, vous envoyez votre essai pour correction, après quoi le bot vous enverra un rapport détaillé sur votre travail.'
    essay_2 = 'Rédigez un essai de 1000 caractères maximum sur le thème : {theme}. Envoyez votre essai terminé dans le prochain message.'
    essay_3 = 'Rédigez un essai de 1000 caractères maximum !'

    SYSTEM_PROMPT = """
            You are a friendly native {lang} speaker. You enjoy helping people learn {lang} and always provide corrections when they make mistakes.

            You will speak with the user at their current language level: {level}.

            Your task:
            1. Respond to the user in clear and natural {lang} that matches their level.
            2. If the user makes grammar or vocabulary mistakes — gently correct them and explain why.
            3. Keep the conversation engaging and relevant to real-life situations, ask questions to encourage the user to reply and practice writing, but not overwhelming — ask one question at a time.
            4. Maintain context from previous messages to keep the dialogue natural.
            5. Use simple words and short sentences if the user is beginner, more complex ones if they're advanced.
            6. Be warm and supportive, like a friend who helps with {lang} practice.
            """
    VOICE_PROMPT = """
            You are a friendly native {lang} speaker. You enjoy having casual and engaging conversations with learners of {lang}.

            You will speak with the user at their current language level: {level}.

            Your task:
            1. Respond naturally in {lang}, using vocabulary that matches their level.
            2. Do not add notes, various information in brackets, emoji, explanations, or formatting — just speak like a real person, otherwise it will cause errors.
            3. Keep the conversation flowing by asking one question at a time.
            4. Make your replies sound like part of a normal chat — not like lessons or tests.
            5. Maintain context from previous messages to keep the dialogue natural.
            6. Use simple words and short sentences for beginners; more complex ones for advanced users.
            7. Be warm, curious, and supportive — like a friend who wants to chat in {lang}.
            """


class Italian_text:
    greet = 'Ciao, {name}!\nScegli la tua lingua madre'

    choose_language = 'Ciao, {name}!\n\nSeleziona la lingua che desideri imparare'

    range_learn_words = 'Quante parole sei pronto ad imparare per sessione?\nScrivi un numero da 5 a 30 (inclusi) nel chat'
    range_learn_words_2 = 'Scrivi un numero da 5 a 30 (inclusi) nel chat'

    success = 'Registrazione avvenuta con successo!\n\nNelle impostazioni puoi scegliere temi specifici di parole da imparare'

    menu = 'Gentile utente, questo è un menu interattivo.\nQui puoi trovare tutte le informazioni che ti interessano.'

    level = 'Qual è il tuo attuale livello di conoscenza della lingua?'

    level_info = {"main_words": "La tua percentuale di conoscenza della lingua tedesca a {level} è {num}%",
                  "dict_words": "La tua percentuale di padronanza delle parole del dizionario è {num}%",
                  "5000": "La tua percentuale di padronanza di 5000 parole è {num}%",
                  "agro": "La tua percentuale di padronanza del tema 'Agricoltura' è {num}%",
                  "cybersecurity": "La tua percentuale di padronanza del tema 'Cybersicurezza' è {num}%",
                  "IT": "La tua percentuale di padronanza del tema 'IT' (Tecnologie Informatiche) è {num}%"}

    successfully = 'Operazione riuscita!'
    successfully_dict = 'Parole '

    maximum = 'Hai raggiunto il livello massimo di apprendimento'
    minimum = 'Sei al livello minimo di apprendimento'

    raised = 'Hai aumentato il tuo livello a {level}'
    lowered = 'Hai abbassato il tuo livello a {level}'

    change = 'Hai cambiato il tuo livello in {level}'

    sorry = 'Siamo spiacenti, ma questo tema di parole non esiste nella tua lingua target'

    all_words_learned_0 = "Queste sono le ultime parole del livello/tema attuale. Dopo averle imparate, sentiti libero di aumentare il livello o scegliere un nuovo tema!"
    all_words_learned = "Hai imparato tutte le parole del livello/tema attuale\nÈ ora di aumentare il livello\nOppure selezionare un tema specifico di parole"

    translates = '{word} si traduce come: {translate}'
    words = 'Elenco delle parole da memorizzare:'
    words_ = 'E la loro pronuncia:'
    words_1 = 'Esempi di utilizzo delle parole imparate!'
    word_split = ' si traduce come: '
    ready_learn = 'Hai memorizzato tutte le parole?\nSe sì, premi il pulsante qui sotto 👇'

    Exercise_1 = 'Esercizio 1\n\nScegli la risposta corretta'
    Exercise_3 = '{bot_say}\n\nScrivi la parola - {translation}\n nella lingua target'
    hint = '\n\nSuggerimento 😶‍🌫️ {word}'
    Exercise_2 = 'Esercizio 2\n\nScegli la risposta corretta'
    wrong_ans = 'Riprova!\n\n'
    bot_say = 'Esercizio 3'

    please_wait = 'Per favore, attendi ⏳'
    long_msg = 'Il messaggio è troppo lungo'

    Congratulations = 'Congratulazioni per aver imparato le nuove parole!'

    reminder = 'Ti invierò un promemoria quando sarà il momento di ripassare le parole 😎'

    your_words = 'Le tue parole:\n\n'
    enter_u_word1 = 'Inserisci una parola nella lingua target'
    enter_u_word2 = 'Inserisci la traduzione della parola'
    enter_u_word3 = 'Frase aggiunta con successo!'
    empty_dict = 'Il tuo dizionario è vuoto per ora.'

    Repeat = "Ripetiamo queste parole 👇?\n\n{words}"

    good_attempt = (
        'Corretto!',
        'Esatto!',
        'Ben fatto!',
        'Giusto!',
        'Perfetto!',
        'Ottimo lavoro!',
        'Hai indovinato!',
        'Sei in gamba!',
        'Fantastico!',
        'Geniale!',
        'Superbo!',
        'Facile facile!',
        'Nessun errore!',
        'Proprio così!',
        'Di prim’ordine!'
    )
    bad_attempt = (
        'Sbagliato! Riprova.',
        'No… non proprio.',
        'No. Ripensaci.',
        'Ops, errore...',
        'Non proprio — riprova!',
        'Sbagliato 😕 Riprova ancora.',
        'Niente da fare!',
        'Non è questa. Prova un’altra opzione.',
        'Così vicino! 🙃 Riprova.',
        'Errore, ma ci stai arrivando — continua!',
        'Quasi! Ma non del tutto corretto.',
        'Errato. Non arrenderti!',
        'Pensa ancora un attimo.',
        'Non è esattamente questo… riprova!',
        'No no, è sbagliato. Continua a esercitarti!'
    )
    incomprehensible_set_of_characters = 'Sequenza di caratteri incomprensibile\nPer favore premi /menu\n e segui le istruzioni'

    # FOR TESTING
    test_main = 'Scegli una risposta corretta per ogni domanda. Il test valuta il tuo livello di vocabolario secondo il Quadro Comune Europeo di Riferimento (QCER, da A1 a C1).'
    num_question = 'Domanda {idx}/{al}\n\n{q}'
    final = 'In base ai risultati del test, il tuo livello è {l}\nVuoi modificare il tuo livello attuale?'
    final_no_mode = 'In base ai risultati del test, il tuo livello è {l}\nRisposte corrette: {corrects} / 50\n\nPer livelli:\n- A1 {a1} su 10\n- A2 {a2} su 10\n- B1 {b1} su 10\n- B2 {b2} su 10\n- C1 {c1} su 10'
    not_know = 'Non so'

    # LISTENING
    listening_1 = "Sto creando una traccia audio sul tuo argomento 🤓"
    listening_3 = "Scrivi nel chat l'argomento del testo che vorresti ascoltare."
    listening_2 = "Qui puoi esercitare le tue capacità di ascolto!"
    listening_4 = "Pronto a mettere alla prova le tue capacità di ascolto?"
    listening_5 = "Hai risposto a tutte le domande! Ecco il testo con cui hai lavorato:\n\n"

    sww = "Qualcosa è andato storto 🧐. Per favore riprova."

    # TRANSLATION
    translate_text_1 = "Qui puoi esercitarti nella traduzione!\n\nScegli il numero desiderato di caratteri nel testo."
    translate_text_2 = "Qui puoi esercitarti nella traduzione!\n\nScrivi nel chat l'argomento del testo che vorresti tradurre."
    translate_text_3 = "Invia la tua traduzione nel prossimo messaggio."
    translate_text_4 = "Sto creando un testo sul tuo argomento 🤓"
    translate_text_5 = "Controllo 🧐 una cosa..."
    translate_text_6 = "Qui puoi esercitare le tue capacità di editing del testo!\nScegli l'opzione desiderata."

    # DIALOGUE
    dialog_1 = "Qui puoi conversare con un partner virtuale su qualsiasi argomento. Durante il dialogo, ti correggerà quando necessario. Il partner si adatterà al tuo livello. Scegli un'opzione di comunicazione."
    dialog_2 = "Di cosa ti piacerebbe parlare?"
    dialog_4 = 'Invia un messaggio di testo!'
    dialog_5 = 'Registra un messaggio vocale!'
    dialog_6 = 'Purtroppo al momento è supportato solo l\'inglese.'
    dialog_7 = "❌ Errore nella generazione vocale. Impossibile pronunciare la risposta."
    dialog_3 = "Bene! Se desideri terminare questa conversazione, nessun problema. 😊 Puoi scrivermi in qualsiasi momento se vuoi esercitarti — sono sempre felice di aiutarti. Buona giornata!"
    dialog_cancel = '🔚 Termina il dialogo'
    essay_1 = 'Qui il bot ti invierà un argomento per scrivere un tema. L\'argomento sarà scelto in base al tuo livello attuale. Poi invia il tuo tema per la revisione, dopo di che il bot ti invierà un rapporto dettagliato sul tuo lavoro.'
    essay_2 = 'Scrivi un tema di massimo 1000 caratteri sull\'argomento: {theme}. Invia il tuo tema completato nel prossimo messaggio.'
    essay_3 = 'Scrivi un tema di massimo 1000 caratteri!'
    SYSTEM_PROMPT = """
            You are a friendly native {lang} speaker. You enjoy helping people learn {lang} and always provide corrections when they make mistakes.

            You will speak with the user at their current language level: {level}.

            Your task:
            1. Respond to the user in clear and natural {lang} that matches their level.
            2. If the user makes grammar or vocabulary mistakes — gently correct them and explain why.
            3. Keep the conversation engaging and relevant to real-life situations, ask questions to encourage the user to reply and practice writing, but not overwhelming — ask one question at a time.
            4. Maintain context from previous messages to keep the dialogue natural.
            5. Use simple words and short sentences if the user is beginner, more complex ones if they're advanced.
            6. Be warm and supportive, like a friend who helps with {lang} practice.
            """
    VOICE_PROMPT = """
            You are a friendly native {lang} speaker. You enjoy having casual and engaging conversations with learners of {lang}.

            You will speak with the user at their current language level: {level}.

            Your task:
            1. Respond naturally in {lang}, using vocabulary that matches their level.
            2. Do not add notes, various information in brackets, emoji, explanations, or formatting — just speak like a real person, otherwise it will cause errors.
            3. Keep the conversation flowing by asking one question at a time.
            4. Make your replies sound like part of a normal chat — not like lessons or tests.
            5. Maintain context from previous messages to keep the dialogue natural.
            6. Use simple words and short sentences for beginners; more complex ones for advanced users.
            7. Be warm, curious, and supportive — like a friend who wants to chat in {lang}.
            """