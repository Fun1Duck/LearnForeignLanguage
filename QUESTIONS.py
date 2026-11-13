import random
import en_questions
import es_questions
import de_questions
import fr_questions
import it_questions

langs = {'en': en_questions,
         'es': es_questions,
         'de': de_questions,
         'fr': fr_questions,
         'it': it_questions}

def drafting_easy_questions(lang):
    def select_random_questions(level_questions, count=20):
        return random.sample(level_questions, k=count)
    q_lang = langs[lang]

    QUESTIONS = {}

    QUESTIONS['A1'] = select_random_questions(q_lang.words_A1)
    QUESTIONS['A2'] = select_random_questions(q_lang.words_A2)
    QUESTIONS['B1'] = select_random_questions(q_lang.words_B1)
    QUESTIONS['B2'] = select_random_questions(q_lang.words_B2)
    QUESTIONS['C1'] = select_random_questions(q_lang.words_C1)

    return QUESTIONS

def drafting_deep_questions(lang):
    def select_random_questions(level_questions, count=25):
        return random.sample(level_questions, k=count)

    q_lang = langs[lang]

    QUESTIONS = {}

    QUESTIONS['A1'] = select_random_questions(q_lang.words_A1) + select_random_questions(q_lang.grammar_A1)
    random.shuffle(QUESTIONS['A1'])
    QUESTIONS['A2'] = select_random_questions(q_lang.words_A2) + select_random_questions(q_lang.grammar_A2)
    random.shuffle(QUESTIONS['A2'])
    QUESTIONS['B1'] = select_random_questions(q_lang.words_B1) + select_random_questions(q_lang.grammar_B1)
    random.shuffle(QUESTIONS['B1'])
    QUESTIONS['B2'] = select_random_questions(q_lang.words_B2) + select_random_questions(q_lang.grammar_B2)
    random.shuffle(QUESTIONS['B2'])
    QUESTIONS['C1'] = select_random_questions(q_lang.words_C1) + select_random_questions(q_lang.grammar_C1)
    random.shuffle(QUESTIONS['C1'])

    return QUESTIONS
