import random
import asyncio

essay_topics_by_level = {
    "A1": [
        "Describe your daily routine.",
        "Write about your favorite food and why you like it.",
        "What do you usually do on weekends?",
        "Describe your family.",
        "My best friend.",
        "Why I like learning English.",
        "My favorite season of the year.",
        "A trip I went on recently.",
        "What I want to do in the future.",
        "My favorite hobby."
    ],
    "A2": [
        "Describe your daily routine.",
        "Write about your favorite food and why you like it.",
        "What do you usually do on weekends?",
        "Describe your family.",
        "My best friend.",
        "Why I like learning English.",
        "My favorite season of the year.",
        "A trip I went on recently.",
        "What I want to do in the future.",
        "My favorite hobby."
    ],
    "B1": [
        "Should students wear school uniforms?",
        "The importance of learning foreign languages.",
        "Is technology making people lazier?",
        "Describe a memorable day in your life.",
        "What would you change in your hometown?",
        "The role of parents in a child’s education.",
        "Advantages and disadvantages of online education.",
        "Should smoking be banned in public places?",
        "What makes a good teacher?",
        "If I could live anywhere in the world..."
    ],
    "B2": [
        "The impact of social media on society.",
        "Are robots replacing human jobs?",
        "Should university education be free?",
        "The effects of climate change on modern life.",
        "Should fast food be taxed more heavily?",
        "Can money buy happiness?",
        "Should exams be abolished in schools?",
        "The influence of celebrities on young people.",
        "Is travel the best way to learn about other cultures?",
        "What are the advantages and disadvantages of working from home?"
    ],
    "C1": [
        "Art is only for the elite. To what extent do you agree?",
        "Should prisoners have the right to vote?",
        "Is artificial intelligence a threat or a benefit?",
        "Should all cars be electric in the future?",
        "The effects of overpopulation on the planet.",
        "Should failure be part of the educational process?",
        "Should there be stricter gun control laws?",
        "Can violent video games affect children's behavior?",
        "Should graffiti be considered as art?",
        "Is advertising aimed at children ethical?"
    ]
}

prompts_for_analyze_essay = {
    "A1": """
You are an {lang} teacher helping a beginner-level student improve their writing skills.
Please evaluate the following essay written by a student at A1–A2 level.

Give feedback in simple {lang} on:
- Spelling and grammar
- Vocabulary used
- Clarity of ideas

Also, suggest one or two small improvements they can make.

Essay:
{essay_text}
""",
    "A2": """
You are an {lang} teacher helping a beginner-level student improve their writing skills.
Please evaluate the following essay written by a student at A1–A2 level.

Give feedback in simple {lang} on:
- Spelling and grammar
- Vocabulary used
- Clarity of ideas

Also, suggest one or two small improvements they can make.

Essay:
{essay_text}
""",
    "B1": """
You are an {lang} teacher helping a student at B1 level improve their writing.
Please evaluate the following essay and provide clear and helpful feedback in {lang}.

Focus on:
- Grammar and sentence structure
- Vocabulary choice and range
- Organization of ideas and coherence
- Relevance to the topic

Give a score from 1 to 9 (like in IELTS).
Suggest 2–3 ways to improve the essay.

Essay:
{essay_text}
""",
    "B2": """
You are an {lang} teacher evaluating an essay written by a B2 level student.
Use the IELTS criteria for assessment: Task Response, Coherence and Cohesion, Lexical Resource, Grammatical Range and Accuracy.

Score each criterion from 1 to 9, then give an overall band score.
Provide detailed feedback in {lang}, highlighting strengths and areas for improvement.

Essay:
{essay_text}
""",
    "C1": """
You are an experienced {lang} teacher assessing an essay written by a C1 level student.
Evaluate the essay using advanced writing criteria such as:
- Argumentation and depth of analysis
- Coherence and logical flow
- Range and precision of vocabulary
- Complex grammatical structures
- Formal tone and style

Give a score from 1 to 9 (like in IELTS) and detailed feedback.
Offer specific suggestions for improvement.

Essay:
{essay_text}
"""
}


async def get_random_topic(level):
    return random.choice(essay_topics_by_level[level])

async def get_promt_to_essay(level):
    return prompts_for_analyze_essay[level]