import datetime
import random
import pymorphy2
import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler,  CommandHandler, ConversationHandler
import time
from get_rifma import getRif
from random_world import get_random_world


# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

# TOKEN = '5393097474:AAGMz30ZHHuxB2Dwh8gG-xJsQTEHQd3Aqgg'
TOKEN = '5310503602:AAHULua2LC6Av3HhIQbt9lb5Mh8uLUWrFks'


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


# Напишем соответствующие функции.
# Их сигнатура и поведение аналогичны обработчикам текстовых сообщений.
def start(update, context):
    update.message.reply_text(
        """ привет)
        я твой помощник в поиске вдохновения и мыслей.
        в качестве знакомства я расскажу тебе о моих командах:
         /help - здесь ты можешь узнать причину недопонимания со мной
         /data - поможет при внезапной потери ощущения мира и времени
         /timee - если обрести себя в пространственном-временном континууме необходимо более точно
         /phraGen - генератор словосочетаний для рождения новых мыслей
         /rifma <твоё слово> - пару рифм для твоих чудесных стихотворений
         """)

    # reply_keyboard = [['Boy', 'Girl', 'Other']]
    # # Создаем простую клавиатуру для ответа
    # markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # # Начинаем разговор с вопроса
    # update.message.reply_text(
    #     'Меня зовут профессор Бот. Я проведу с вами беседу. '
    #     'Команда /cancel, чтобы прекратить разговор.\n\n'
    #     'Ты мальчик или девочка?',
    #     reply_markup=markup_key,)
    update.message.reply_text(
        " я Влад, кстати. А как тебя называют? или сам назовись")
    return 1


def help(update, context):
    update.message.reply_text(
        "пиши грамотно, чтобы я тебя понимал или просто страдай))")


def rifma(update, context):
    # update.message.reply_text(
    #     "введи слово для рифмы")
    word = context.args[0]
    rifms = getRif(word)

    if len(rifms) == 0:
        update.message.reply_text(
            "друг, я не смог найти рифму к этому слову...))")
    else:
        # lnr = 10 if len(rifms) > 10 else len(rifms)
        str_temp = ", ".join(rifms[:50])

        update.message.reply_text(
            " " + str_temp)

    # update.message.reply_text(
    #     f"{word}")


def phraGen(update, context):
    pfrasa = morf()
    update.message.reply_text(
        f"лови🎆: {pfrasa} ")


def timee(update, context):
    now = datetime.datetime.now()
    nh = now.hour
    hour = nh + 3
    minut = now.minute
    sec = now.second
    microsec = now.microsecond
    update.message.reply_text(
        '🕗: ' + str(hour)+': '+str(minut)+': '+str(sec)+': '+str(microsec)+'..')


def data(update, context):
    t = time.localtime()
    td = str(time.asctime(t))
    update.message.reply_text(td[:11] + td[19:])


def first(update, context):
    name = update.message.text

    update.message.reply_text(
        f"👋 приятно познакомиться, {name})")

    update.message.reply_text(
        "как дела?")
    return 2


def first_response(update, context):
    locality = update.message.text
    if locality == 'хорошо' or locality == 'прекрасно' or locality == 'чудесно' or locality == 'превосходно' or locality == 'отлично':
        update.message.reply_text(
            "☀️, я рад:) У меня всё тоже хорошо. настроение, как у Карлсона: хочу сладкого и пошалить.")
    elif locality == 'не плохо' or locality == 'норм' or locality == 'так себе' or locality == 'нормально':
        update.message.reply_text(
            """сочувствую) надеюсь, всё хорошо
               Бывает так хреново, что не знаешь: 
               03 — звонить или 0,5 — налить?..:)
               Проще сказать, что всё нормально, чем объяснять, почему так хреново. Да?
            """)
    elif locality == 'плохо' or locality == 'ужасно' or locality == 'отвратительно':
        update.message.reply_text(
            """Прежде чем диагностировать у себя депрессию и заниженную самооценку,
                убедись, что ты не окружен идиотами
             """)
    else:
        update.message.reply_text(
            """Все является только иллюзией, совершенным и простым,
            таким каким является на самом деле, нет ничего общего с «хорошим» или «плохим»,
             с «привязанностью» или «отталкиванием». Поэтому можно так же хорошо. Взорваться смехом.
             """)

    update.message.reply_text(
        "не хочешь вкусить аромат творчества?📖🖋")

    return 3


def second_response(update, context):

    locality1 = update.message.text

    if locality1 == 'ни капли' or locality1 == 'нет' or locality1 == 'отстань' or locality1 == 'неа' or locality1 == 'не':
        update.message.reply_text(
            "Лень, конечно, двигатель прогресса, но всё же))")
        update.message.reply_text(
            f" может воспользуешься /phraGen ?")
    elif locality1 == 'не знаю' or locality1 == 'пофиг' or locality1 == 'всё равно' or locality1 == 'безразницы':
        update.message.reply_text(
            "пофигизм — это безмятежная лёгкость бытия?")
        update.message.reply_text(
            f" напоминаю тебе о  /phraGen 📝")
    elif locality1 == 'да' or locality1 == 'можно' or locality1 == 'хочу':
        update.message.reply_text(
            "прекрасно)")
        update.message.reply_text(
            f"😝 если пока нет идей, то  /phraGen в помощь)")

    else:
        update.message.reply_text(
            "Эм?")
        update.message.reply_text(
            f" нажми  /phraGen !")
    return ConversationHandler.END


def stop(update, _):
    update.edit_message_text(text="Всего доброго😴")
    return ConversationHandler.END


def main():
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater(TOKEN)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            # Добавили user_data для сохранения ответа.
            1: [MessageHandler(Filters.text & ~Filters.command, first)],

            2: [MessageHandler(Filters.text & ~Filters.command, first_response)],
            # ...и для его использования.
            3: [MessageHandler(Filters.text & ~Filters.command, second_response)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    # Зарегистрируем их в диспетчере рядом
    # с регистрацией обработчиков текстовых сообщений.
    # Первым параметром конструктора CommandHandler я
    # вляется название команды.
    # dp.add_handler(CommandHandler("start", start))
    dp.add_handler(conv_handler)

    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(CommandHandler("phraGen", phraGen))

    dp.add_handler(CommandHandler("timee", timee))

    dp.add_handler(CommandHandler("data", data))

    dp.add_handler(CommandHandler("rifma", rifma))
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
