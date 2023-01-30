#! /usr/bin/env python

import random
import pymorphy2
import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler,  CommandHandler, ConversationHandler
import time
from get_rifma import getRif
from words_game import get_put_words
from random_world import get_random_world
from get_jokes import get_jok
import datetime


# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5310503602:AAHULua2LC6Av3HhIQbt9lb5Mh8uLUWrFks'


commands_text = """
    ---------------------------------------------------------------
    🆘 /help - здесь ты можешь узнать причину недопонимания со мной
    ---------------------------------------------------------------
    🔻 /data - поможет при внезапной потери ощущения мира и времени
    ---------------------------------------------------------------
    🔺 /timee - если обрести себя в пространственном-временном континууме необходимо более точно
    ---------------------------------------------------------------
    🟥 /phraGen - генератор словосочетаний для рождения новых мыслей
    ---------------------------------------------------------------
    🔴 /rifma слово - пару рифм для чудесных стихотворений к твоему слову
    ---------------------------------------------------------------
    ♦️/game - игра в слова (где на  последнюю букву слова другого игрока нужно назвать своё слово
    ---------------------------------------------------------------
    ❤ /joke - маленькая искра для твоей улыбки
    """


def start(update, _):
    update.message.reply_text("😏 привет)")
    update.message.reply_text(
        "Я твой помощник в поиске вдохновения и мыслей 💬")
    update.message.reply_text(
        "В качестве знакомства я расскажу тебе о моих командах: ")
    update.message.reply_text(commands_text)

    update.message.reply_text(
        "Я Влад, кстати. А как тебя называют? или сам назовись")
    return 1


def first(update, _):
    name = update.message.text

    update.message.reply_text(
        f"👋 Приятно познакомиться, {name})")

    update.message.reply_text(
        "Как дела?")
    return 2


def first_response(update, _):
    locality = update.message.text
    locality = locality.lower()
    if locality == 'хорошо' or locality == 'прекрасно' or locality == 'чудесно' or locality == 'превосходно' or locality == 'отлично':
        update.message.reply_text(
            "☀️, я рад:) У меня всё тоже хорошо. настроение, как у Карлсона: хочу сладкого и пошалить.")
    elif locality == 'не плохо' or locality == 'норм' or locality == 'так себе' or locality == 'нормально':
        update.message.reply_text(
            """
            Сочувствую) надеюсь, всё хорошо... Бывает так хреново, что не знаешь: 03 — звонить или 0,5 — налить?..:) Проще сказать, что всё нормально, чем объяснять, почему так хреново. Да?
            """)
    elif locality == 'плохо' or locality == 'ужасно' or locality == 'отвратительно':
        update.message.reply_text(
            """Прежде чем диагностировать у себя депрессию и заниженную самооценку, убедись, что ты не окружен идиотами))
             """)
    else:
        update.message.reply_text(
            """Все является только иллюзией, совершенным и простым, таким каким является на самом деле, нет ничего общего с «хорошим» или «плохим», с «привязанностью» или «отталкиванием». Поэтому можно так же хорошо. Взорваться смехом.
             """)

    update.message.reply_text(
        "Не хочешь вкусить аромат творчества?📖🖋")
    return 3


def second_response(update, _):

    locality1 = update.message.text
    locality1 = locality1.lower()
    if locality1 == 'ни капли' or locality1 == 'нет' or locality1 == 'отстань' or locality1 == 'неа' or locality1 == 'не':
        update.message.reply_text(
            "Лень, конечно, двигатель прогресса, но всё же))")
        update.message.reply_text(
            u" может воспользуешься /phraGen ?")
    elif locality1 == 'не знаю' or locality1 == 'пофиг' or locality1 == 'всё равно' or locality1 == 'безразницы':
        update.message.reply_text(
            "пофигизм — это безмятежная лёгкость бытия?")
        update.message.reply_text(
            u" напоминаю тебе о  /phraGen 📝")
    elif locality1 == 'да' or locality1 == 'можно' or locality1 == 'хочу':
        update.message.reply_text(
            "прекрасно)")
        update.message.reply_text(
            u"😝 если пока нет идей, то  /phraGen в помощь)")

    else:
        update.message.reply_text(
            "Эм?")
        update.message.reply_text(
            u" нажми  /phraGen !")
    return ConversationHandler.END


def commands(update, _):
    update.message.reply_text(commands_text)


def help(update, _):
    update.message.reply_text(
        """😉 мои способности /commands (вызов списка команд)

😳 контакты моего разработчика: @regennur

😕 если не понял, как работает 
/rifma : пример для поиска рифмы к слову 'барабака" --- нужно написать в сообщении "/rifma барабака"

😶 и наконец, ответ на ВСЕ твои 
В❔ПР❔СЫ:

Если вторая производная мысли меньше нуля, но имеет выгнутую форму, стоит вспомнить о существовании пояса
Койпера. 
Если вследствие квантовой гравитации графены расширяют электромагнитное излучение фундаментальных взаимодействий, следует сравнить длину интеграла отрицательного дискриминанта кубической производной  с вектором асимптоты. Если и это не помогло, то пренебречь сингулярность.

Ну или просто попробуй ещё раз""")


def rifma(update, context):
    # update.message.reply_text("")
    word = context.args[0]
    rifms = getRif(word)

    if len(rifms) == 0:
        update.message.reply_text(
            "друг, я не смог найти рифму к этому слову...(")
    else:
        str_temp = ", ".join(rifms[:50])

        update.message.reply_text(
            " " + str_temp)


def morf():
    morf_arr = get_random_world()
    adf = morf_arr['adf']
    non = morf_arr['non']
    veb = morf_arr['veb']

    morph = pymorphy2.MorphAnalyzer()
    res = morph.parse(non)[0]
    gender = res.tag.gender
    ADJF = morph.parse(adf)[0].inflect({gender}).word
    VERB = morph.parse(veb)[0].inflect({gender}).word
    phrasGEN = str(ADJF) + ' ' + str(non) + ' ' + str(VERB)
    return phrasGEN


def joke(update, _):
    text = get_jok()
    joki = text['joke']
    update.message.reply_text(joki)


def phraGen(update, _):
    pfrasa = morf()
    update.message.reply_text(
        f"лови💥: {pfrasa} ")


def timee(update, _):
    now = datetime.datetime.now()
    nh = now.hour
    hour = nh + 3
    minut = now.minute
    sec = now.second
    microsec = now.microsecond
    update.message.reply_text(
        '🕗 ' + str(hour)+':'+str(minut)+':'+str(sec)+':'+str(microsec)+'.. ')
    if hour > 21:
        update.message.reply_text('Уютной вдохновенной ночи😴')
    elif hour > 4 and hour < 9:
        update.message.reply_text('Чудесного утра 🤗')
    elif hour < 4:
        update.message.reply_text('Зайка, ты чего не спишь? 🥱')
    elif hour > 12 and hour < 16:
        update.message.reply_text('Хорошего дня☺️')
    elif hour > 17 and hour < 22:
        update.message.reply_text('Теплого вечера')
        update.message.reply_text('✨')


def data(update, _):
    t = time.localtime()
    td = str(time.asctime(t))
    if 'Nov' in td:
        l1 = '🍁'
        l2 = '🌧️'
        l3 = '🍂'
    elif 'Sep' in td:
        l1 = '🍁'
        l2 = '🌧️'
        l3 = '🍂'
    elif 'Oct' in td:
        l1 = '🍁'
        l2 = '🌧️'
        l3 = '🍂'
    elif 'Dec' in td:
        l1 = '❄️'
        l2 = '🌨️'
        l3 = '⛄'
    elif 'Jan' in td:
        l1 = '❄️'
        l2 = '🌨️'
        l3 = '⛄'
    elif 'Feb' in td:
        l1 = '❄️'
        l2 = '🌨️'
        l3 = '⛄'
    elif 'Mar' in td:
        l1 = '🌱'
        l2 = '🌸'
        l3 = '🌷'
    elif 'Apr' in td:
        l1 = '🌱'
        l2 = '🌸'
        l3 = '🌷'
    elif 'May' in td:
        l1 = '🌱'
        l2 = '🌸'
        l3 = '🌷'
    else:
        l1 = '🏖️'
        l2 = '😎'
        l3 = '🍉'
    update.message.reply_text(
        l1 + td[8:10] + ' ' + td[4:7] + ' ' + td[20:]+','+l2+'  ' + td[:3]+l3)


def stop(update, _):
    update.edit_message_text(text="Всего доброго😴")
    return ConversationHandler.END


def game(update, _):
    update.message.reply_text(
        "Привет:) Это игра в слова. Каждый игрок называет слово на последнюю букву предыдущего игрока. Начинай!")

    return 1


wh_flag = ''
wh_listInput = []


def word_hand(update, context):
    word = update.message.text
    # update.message.reply_text(word)
    wh_listInput = context.user_data.get('wh_listInput', [])
    wh_flag = context.user_data.get('wh_flag', '')
    ga = get_put_words(word, wh_listInput, wh_flag)

    update.message.reply_text(ga[1])
    # update.message.reply_text("Тебе на "+ga[3])

    context.user_data['wh_listInput'] = ga[2]
    context.user_data['wh_flag'] = ga[3]

    return 1


# def error(update, context):
#     update.message.reply_text('an error occured')


def main():
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater(TOKEN, use_context=True)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    start_handler = CommandHandler('start', start)

    # https://docs.python-telegram-bot.org/en/latest/telegram.ext.conversationhandler.html
    conv_handler = ConversationHandler(
        name="StartHandler",
        entry_points=[start_handler],
        states={
            # Добавили user_data для сохранения ответа.
            1: [MessageHandler(Filters.text & ~Filters.command, first)],
            2: [MessageHandler(Filters.text & ~Filters.command, first_response)],
            3: [MessageHandler(Filters.text & ~Filters.command, second_response)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    conv_handler_GAME = ConversationHandler(
        name="GameHandler",
        entry_points=[CommandHandler('game', game)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, word_hand)],
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    # Зарегистрируем их в диспетчере рядом
    # с регистрацией обработчиков текстовых сообщений.
    # Первым параметром конструктора CommandHandler я
    # вляется название команды.
    # dp.add_handler(CommandHandler("start", start))
    dp.add_handler(conv_handler)
    dp.add_handler(conv_handler_GAME)
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("phraGen", phraGen))
    dp.add_handler(CommandHandler("joke", joke))
    dp.add_handler(CommandHandler("timee", timee))
    dp.add_handler(CommandHandler("data", data))
    dp.add_handler(CommandHandler("commands", commands))
    dp.add_handler(CommandHandler("rifma", rifma))

    # dp.add_error_handler(error)
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
