import sqlite3
from collections import defaultdict
import asyncio
import aiosqlite
import os


class UsersDicts:
    name_db = 'users_dicts.db'

    @classmethod
    async def create_table(cls, user_id):
        table_name = f'table_{user_id}'
        async with aiosqlite.connect(cls.name_db) as db:
            await db.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    words TEXT
                )
            """)
            await db.commit()

    @classmethod
    async def add_word(cls, user_id, word):
        table_name = f'table_{user_id}'
        async with aiosqlite.connect(cls.name_db) as db:
            async with db.execute(f"SELECT words FROM {table_name} WHERE rowid = 1") as cursor:
                result = await cursor.fetchone()
                if result and result[0]:
                    parts = result[0].rstrip().split('\n')
                    if len(parts) >= 150:
                        parts = parts[1:]
                    words_str = '\n'.join(parts) + '\n'
                    await db.execute(
                        f"UPDATE {table_name} SET words = ? WHERE rowid = 1",
                        (words_str,)
                    )
                else:
                    words_str = ''

                await db.execute(
                    f"INSERT OR REPLACE INTO {table_name} (rowid, words) VALUES (1, ?)",
                    (words_str + word + '\n',)
                )
                await db.commit()

    @classmethod
    async def get_words(cls, user_id):
        table_name = f'table_{user_id}'
        async with aiosqlite.connect(cls.name_db) as db:
            async with db.execute(f"SELECT words FROM {table_name} WHERE rowid = 1") as cursor:
                result = await cursor.fetchone()
                await db.commit()
                return result[0].rstrip() if result else None


class UsersWords:
    name_db = 'users_words.db'

    @classmethod
    async def create_table(cls, user_id):
        table_name = f'table_{user_id}'
        async with aiosqlite.connect(cls.name_db) as db:
            await db.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    unique_id TEXT,
                    words TEXT,
                    timer INTEGER,
                    sent BOOLEAN DEFAULT FALSE
                )
            """)
            await db.commit()

    @classmethod
    async def add_user_info(cls, user_id, unique_id, words, timer):
        table_name = f'table_{user_id}'
        async with aiosqlite.connect(cls.name_db) as db:
            await db.execute(
                f"INSERT INTO {table_name} (unique_id, words, timer, sent) VALUES (?, ?, ?, ?)",
                (unique_id, words, timer, False)
            )
            await db.commit()

    @classmethod
    async def update_words(cls, user_id, unique_id, timer):
        table_name = f'table_{user_id}'
        async with aiosqlite.connect(cls.name_db) as db:
            await db.execute(
                f"UPDATE {table_name} SET timer = ?, sent = ? WHERE unique_id = ?",
                (timer, False, unique_id)
            )
            await db.commit()

    @classmethod
    async def get_words(cls, user_id, unique_id):
        table_name = f'table_{user_id}'
        async with aiosqlite.connect(cls.name_db) as db:
            async with db.execute(f"SELECT words, timer FROM {table_name} WHERE unique_id = ?", (unique_id,)) as cursor:
                result = await cursor.fetchone()
                await db.commit()
                return result

    @classmethod
    async def delete_info(cls, user_id, unique_id):
        table_name = f'table_{user_id}'
        async with aiosqlite.connect(cls.name_db) as db:
            await db.execute(
                f"DELETE FROM {table_name} WHERE unique_id = ?",
                (unique_id,)
            )
            await db.commit()

    @classmethod
    async def sent_True(cls, user_id, unique_id):
        table_name = f'table_{user_id}'
        async with aiosqlite.connect(cls.name_db) as db:
            await db.execute(
                f"UPDATE {table_name} SET sent = ? WHERE unique_id = ?",
                (True, unique_id)
            )
            await db.commit()

    @classmethod
    async def schedule_all_pending_repeats(cls):
        info = dict()
        async with aiosqlite.connect(UsersWords.name_db) as db:
            async with db.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'table_%'") as cursor:
                tables = await cursor.fetchall()
                await db.commit()

        for table_name in tables:
            table_name = table_name[0]
            user_id = int(table_name.split('_')[-1])
            async with aiosqlite.connect(UsersWords.name_db) as db:
                async with db.execute(
                        f"SELECT unique_id, timer FROM {table_name} WHERE sent = ?",
                        (False,)) as cursor:

                    rows = await cursor.fetchall()
                    info[user_id] = rows

        return info


class UsersTexts:
    name_db = 'users_texts.db'

    @classmethod
    async def create_table(cls, user_id):
        table_name = f'table_{user_id}'
        async with aiosqlite.connect(cls.name_db) as db:
            await db.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    unique_id TEXT,
                    text TEXT,
                    translation TEXT,
                    msg_id INTEGER
                )
            """)
            await db.commit()

    @classmethod
    async def add_user_text(cls, user_id, unique_id, text, translation, msg_id):
        table_name = f'table_{user_id}'
        async with aiosqlite.connect(cls.name_db) as db:
            await db.execute(
                f"INSERT INTO {table_name} (unique_id, text, translation, msg_id) VALUES (?, ?, ?, ?)",
                (unique_id, text, translation, msg_id)
            )
            await db.commit()

    @classmethod
    async def get_translation(cls, user_id, unique_id):
        table_name = f'table_{user_id}'
        async with aiosqlite.connect(cls.name_db) as db:
            cursor = await db.execute(
                f"SELECT text, translation, msg_id FROM {table_name} WHERE unique_id = ?",
                (unique_id,)
            )
            result = await cursor.fetchone()

            await db.execute(
                f"DELETE FROM {table_name} WHERE unique_id = ?",
                (unique_id,)
            )
            await db.commit()
        return result


class Users:
    name_db = 'users_bot_learn_language.db'

    def __init__(self, name):
        self.name = name
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS {} (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        user_id INTEGER,
                                        native_lang varchar(15),
                                        will_learn_lang varchar(15),
                                        level varchar(2),
                                        theme TEXT,
                                        quantity_words INTEGER,
                                        menu_id INTEGER
                                        )""".format(self.name))
            db.commit()

    async def add_user_info(self, user_id, data: dict):
        async with aiosqlite.connect(self.name_db) as db:
            await db.execute(
                f"INSERT INTO {self.name} (user_id, native_lang, will_learn_lang, level, quantity_words, menu_id) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (user_id, data['native_lang'], data['will_learn_lang'], data['level'], data['quantity_words'], data['menu_id'])
            )
            await db.commit()

    async def get_level(self, user_id):
        async with aiosqlite.connect(self.name_db) as db:
            async with db.execute(f"SELECT level FROM {self.name} WHERE user_id = ?", (user_id,)) as cursor:
                result = await cursor.fetchone()
                await db.commit()
                return result[0] if result else None

    async def get_menu_id(self, user_id):
        async with aiosqlite.connect(self.name_db) as db:
            async with db.execute(f"SELECT menu_id FROM {self.name} WHERE user_id = ?", (user_id,)) as cursor:
                result = await cursor.fetchone()
                await db.commit()
                return result[0] if result else None

    async def get_theme(self, user_id):
        async with aiosqlite.connect(self.name_db) as db:
            async with db.execute(f"SELECT theme FROM {self.name} WHERE user_id = ?", (user_id,)) as cursor:
                result = await cursor.fetchone()
                await db.commit()
                return result[0] if result else None

    async def get_users_ids(self):
        async with aiosqlite.connect(self.name_db) as db:
            async with db.execute(f"SELECT user_id FROM {self.name}") as cursor:
                result = await cursor.fetchall()
                await db.commit()
                if not result:
                    return tuple()
                return set([id_user[0] for id_user in result])

    async def get_quantity_words(self, user_id):
        async with aiosqlite.connect(self.name_db) as db:
            async with db.execute(f"SELECT quantity_words FROM {self.name} WHERE user_id = ?", (user_id,)) as cursor:
                result = await cursor.fetchone()
                await db.commit()
                return result[0] if result else None

    async def change_level(self, level, user_id):
        async with aiosqlite.connect(self.name_db) as db:
            await db.execute(
                f"UPDATE {self.name} SET level = ? WHERE user_id = ?",
                (level, user_id)
            )
            await db.commit()

    async def update_menu_id(self, user_id, new_menu_id=None):
        async with aiosqlite.connect(self.name_db) as db:
            await db.execute(
                f"UPDATE {self.name} SET menu_id = ? WHERE user_id = ?",
                (new_menu_id, user_id)
            )
            await db.commit()

    async def increase_level(self, user_id):
        levels = {'A1': 'A2', 'A2': 'B1', 'B1': 'B2', 'B2': 'C1', 'C1': 'C2'}
        async with aiosqlite.connect(self.name_db) as db:
            async with db.execute(f"SELECT level FROM {self.name} WHERE user_id = ?", (user_id,)) as cursor:
                result = await cursor.fetchone()
                current = result[0]
                new_level = levels.get(current, current)
                await db.execute(f"UPDATE {self.name} SET level = ? WHERE user_id = ?", (new_level, user_id))
                await db.commit()

    async def reduce_level(self, user_id):
        levels = {'A2': 'A1', 'B1': 'A2', 'B2': 'B1', 'C1': 'B2', 'C2': 'C1'}
        async with aiosqlite.connect(self.name_db) as db:
            async with db.execute(f"SELECT level FROM {self.name} WHERE user_id = ?", (user_id,)) as cursor:
                result = await cursor.fetchone()
                current = result[0]
                new_level = levels.get(current, current)
                await db.execute(f"UPDATE {self.name} SET level = ? WHERE user_id = ?", (new_level, user_id))
                await db.commit()

    async def get_learn_lang(self, user_id):
        async with aiosqlite.connect(self.name_db) as db:
            async with db.execute(f"SELECT will_learn_lang FROM {self.name} WHERE user_id = ?", (user_id,)) as cursor:
                result = await cursor.fetchone()
                await db.commit()
                return result[0] if result else None

    async def get_native_lang(self, user_id):
        async with aiosqlite.connect(self.name_db) as db:
            async with db.execute(f"SELECT native_lang FROM {self.name} WHERE user_id = ?", (user_id,)) as cursor:
                result = await cursor.fetchone()
                await db.commit()
                return result[0] if result else None

    async def new_quantity_words(self, user_id, num):
        async with aiosqlite.connect(self.name_db) as db:
            await db.execute(f"UPDATE {self.name} SET quantity_words = ? WHERE user_id = ?", (num, user_id))
            await db.commit()

    async def update_info(self, user_id, data):
        async with aiosqlite.connect(self.name_db) as db:
            await db.execute(f"UPDATE {self.name} SET will_learn_lang = ?, level = ?, quantity_words = ?, menu_id = ? WHERE user_id = ?", (data['will_learn_lang'], data['level'], data['quantity_words'], data['menu_id'], user_id))
            await db.commit()

class DataBaseWordsLanguage:
    name_db = 'words.db'

    def __init__(self, name):
        self.name = name
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS {} (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            level varchar(2),
                                            words TEXT
                                            )""".format(self.name))
            if self.name == 'en':
                for level in ('A1', 'A2', 'B1', 'cybersecurity', 'IT', '5000', 'B2', 'C1', 'agro'):
                    c.execute(f"SELECT COUNT(*) FROM {self.name} WHERE level = ?", (level,))
                    result = c.fetchone()[0]
                    if result == 0:
                        filename = os.path.join('langs', 'en', f'en_{level}.txt')
                        with open(filename, encoding='utf-8') as f:
                            words = f.read()
                            c.execute(
                                f"INSERT INTO {self.name} (level, words) VALUES (?, ?)",
                                (level, words))
            if self.name == 'rus':
                for level in ('A1', 'A2', 'B1', 'B2', 'C1'):
                    c.execute(f"SELECT COUNT(*) FROM {self.name} WHERE level = ?", (level,))
                    result = c.fetchone()[0]
                    if result == 0:
                        filename = os.path.join('langs', 'rus', f'rus_{level}.txt')
                        with open(filename, encoding='utf-8') as f:
                            words = f.read()
                            c.execute(
                                f"INSERT INTO {self.name} (level, words) VALUES (?, ?)",
                                (level, words))
            if self.name == 'es':
                for level in ('A1', 'A2', 'B1', 'B2', 'C1'):
                    c.execute(f"SELECT COUNT(*) FROM {self.name} WHERE level = ?", (level,))
                    result = c.fetchone()[0]
                    if result == 0:
                        filename = os.path.join('langs', 'es', f'es_{level}.txt')
                        with open(filename, encoding='utf-8') as f:
                            words = f.read()
                            c.execute(
                                f"INSERT INTO {self.name} (level, words) VALUES (?, ?)",
                                (level, words))
            if self.name == 'de':
                for level in ('A1', 'A2', 'B1', 'B2', 'C1'):
                    c.execute(f"SELECT COUNT(*) FROM {self.name} WHERE level = ?", (level,))
                    result = c.fetchone()[0]
                    if result == 0:
                        filename = os.path.join('langs', 'de', f'de_{level}.txt')
                        with open(filename, encoding='utf-8') as f:
                            words = f.read()
                            c.execute(
                                f"INSERT INTO {self.name} (level, words) VALUES (?, ?)",
                                (level, words))
            if self.name == 'fr':
                for level in ('A1', 'A2', 'B1', 'B2', 'C1'):
                    c.execute(f"SELECT COUNT(*) FROM {self.name} WHERE level = ?", (level,))
                    result = c.fetchone()[0]
                    if result == 0:
                        filename = os.path.join('langs', 'fr', f'fr_{level}.txt')
                        with open(filename, encoding='utf-8') as f:
                            words = f.read()
                            c.execute(
                                f"INSERT INTO {self.name} (level, words) VALUES (?, ?)",
                                (level, words))
            if self.name == 'it':
                for level in ('A1', 'A2', 'B1', 'B2', 'C1'):
                    c.execute(f"SELECT COUNT(*) FROM {self.name} WHERE level = ?", (level,))
                    result = c.fetchone()[0]
                    if result == 0:
                        filename = os.path.join('langs', 'it', f'it_{level}.txt')
                        with open(filename, encoding='utf-8') as f:
                            words = f.read()
                            c.execute(
                                f"INSERT INTO {self.name} (level, words) VALUES (?, ?)",
                                (level, words))
            db.commit()

    async def get_words_level(self, level):
        async with aiosqlite.connect(self.name_db) as db:
            async with db.execute(f"SELECT words FROM {self.name} WHERE level = ?", (level,)) as cursor:
                result = await cursor.fetchone()
                await db.commit()
                return result[0] if result else None


class UserStudyWords:
    name_db = 'users_bot_learn_language.db'

    def __init__(self, name):
        self.name = name
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS {} (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        user_id INTEGER,
                                        words_study_level TEXT,
                                        learnt_words TEXT
                                        )""".format(self.name))
            db.commit()

    async def add_user(self, user_id):
        async with aiosqlite.connect(self.name_db) as db:
            await db.execute(
                f"INSERT INTO {self.name} (user_id) VALUES (?)",
                (user_id,)
            )
            await db.commit()

    async def update_words_study_level(self, user_id, words, theme):
        async with aiosqlite.connect(self.name_db) as db:
            await db.execute(
                f"UPDATE {self.name} SET words_study_level = ? WHERE user_id = ?",
                (words, user_id)
            )
            await db.execute(
                f"UPDATE users SET theme = ? WHERE user_id = ?",
                (theme, user_id)
            )
            await db.commit()

    async def get_percent_of_level(self, user_id):
        async with aiosqlite.connect(self.name_db) as db:
            async with db.execute(f"SELECT learnt_words, words_study_level FROM {self.name} WHERE user_id = ?", (user_id,)) as cursor:
                res = await cursor.fetchone()
                if not res or not res[1]:
                    return 0.0
                words_study_level = res[1].split('\n')
                if not res[0]:
                    return 0.0
                learnt_words = res[0].split('\n')
                not_learnt = set(words_study_level) - set(learnt_words)
                percent = round(100 - (len(not_learnt) / len(words_study_level)) * 100, 2)
                await db.commit()
                return percent

    async def get_words(self, user_id):
        async with aiosqlite.connect(self.name_db) as db:
            async with db.execute(f"SELECT words_study_level FROM {self.name} WHERE user_id = ?", (user_id,)) as cursor:
                res = (await cursor.fetchone())[0]
            async with db.execute(f"SELECT learnt_words FROM {self.name} WHERE user_id = ?", (user_id,)) as cursor:
                res1 = (await cursor.fetchone())[0]
            await db.commit()
        table_name = f'table_{user_id}'
        words_from_table = []
        try:
            async with aiosqlite.connect(UsersWords.name_db) as db_words:
                async with db_words.execute(f"SELECT words FROM {table_name}") as cursor:
                    rows = await cursor.fetchall()
                    res2 = '\n'.join([row[0] for row in rows])
        except Exception as e:
            print(f"[Ошибка при получении слов из UsersWords]: {e}")

        words = res.split('\n')
        if not res1 and not res2:
            return words
        elif not res2:
            return list(set(words) - set(res1.split('\n')))
        elif not res1:
            return list(set(words) - set(res2.split('\n')))
        else:
            return list(set(words) - set(res1.split('\n')) - set(res2.split('\n')))

    async def add_learnt_word(self, user_id, word):
        async with aiosqlite.connect(self.name_db) as db:
            await db.execute(
                f"UPDATE {self.name} SET learnt_words = COALESCE(learnt_words, '') || ? WHERE user_id = ?",
                (word + '\n', user_id)
            )
            await db.commit()