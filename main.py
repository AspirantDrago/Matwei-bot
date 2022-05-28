import telebot
from telebot import types
from random import choices
import time
from mysql import *
from admin_panel import *
from blackspisock import *

token = '5318630722:AAETDHnbZMkhXmSdGzs3O-r8D5Q2JaZGZXE'

bot=telebot.TeleBot(token)

ls = []

check_erors = False

str_erors = ''


promo = {}



try:
    @bot.message_handler(commands=['start'])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Пройти регистрацию")
        btn2 = types.KeyboardButton('Уйти')
        btn3 = types.KeyboardButton('Почему я не могу пользоваться другими командами?')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Привет! Пройди пожалйста регстрацию!".format(message.from_user), reply_markup=markup)








    @bot.message_handler(content_types='text')
    def message_reply(message):

            if message.text=="Пройти регистрацию":

               markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
               item1=types.KeyboardButton("abcd")
               markup.add(item1)
               bot.send_message(message.chat.id,'Напиши в чат символы: abcd',reply_markup=markup)

            elif message.text=="abcd":
                if not proverka(message.from_user.id):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item1 = types.KeyboardButton("Главное меню")
                    markup.add(item1)
                    bot.send_message(message.chat.id, 'Вы успешно зарегистрировались', reply_markup=markup)
                    ls.append(message.from_user.id)
                    add(message.from_user.id)

                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item1 = types.KeyboardButton("Главное меню")
                    markup.add(item1)
                    bot.send_message(message.chat.id, 'Вы уже зарегистрированы!', reply_markup=markup)





            elif message.text == 'Главное меню' and  proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Автобусы")
                item2 = types.KeyboardButton("Сколько стоит проезд?")
                item3 = types.KeyboardButton("Маршрутки")
                item4 = types.KeyboardButton("Трамваи")
                markup.add(item1, item2, item3, item4)
                bot.send_message(message.chat.id, 'Ты в главном меню!', reply_markup=markup)

            elif message.text == 'Автобусы' and  proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item2 = types.KeyboardButton("Сколько стоит проезд?")
                item3 = types.KeyboardButton("Узанать путь автобуса")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item2, item3, item4)
                bot.send_message(message.chat.id, 'Ты в главном автобусов!', reply_markup=markup)

            elif message.text == 'Маршрутки' and  proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item2 = types.KeyboardButton("Сколько стоит проезд?")
                item3 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item2, item3, item4)
                bot.send_message(message.chat.id, 'Ты в главном маршруток!', reply_markup=markup)


            elif message.text == 'Сколько стоит проезд?' and  proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Автобус")
                item2 = types.KeyboardButton("Трамвай")
                item3 = types.KeyboardButton("Маршрутка")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item2, item3, item4)
                bot.send_message(message.chat.id, 'Нажми на главное меню что бы вернутся в начало!', reply_markup=markup)



            elif message.text == 'Автобус' and  proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item3 = types.KeyboardButton("Сколько стоит проезд?")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item3, item4)
                bot.send_message(message.chat.id, 'Проезд на автобусе стоит: 22 рублей', reply_markup=markup)

            elif message.text == 'Трамвай' and  proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item3 = types.KeyboardButton("Сколько стоит проезд?")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item3, item4)
                bot.send_message(message.chat.id, 'Проезд на трамвае стоит: 20 рублей', reply_markup=markup)

            elif message.text == 'Маршрутка' and  proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item3 = types.KeyboardButton("Сколько стоит проезд?")
                item4 = types.KeyboardButton("Главное меню")
                item5 = types.KeyboardButton("Узанать путь маршрутки")
                markup.add(item3, item5, item4)
                bot.send_message(message.chat.id, 'Проезд на трамвае стоит: 30 рублей', reply_markup=markup)



            elif message.text == 'Узанать путь маршрутки' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("3")
                item2 = types.KeyboardButton("5")
                item3 = types.KeyboardButton("5а")
                item4 = types.KeyboardButton("6а")
                item5 = types.KeyboardButton("6")
                item6 = types.KeyboardButton("11")
                item7 = types.KeyboardButton("14а")
                item8 = types.KeyboardButton("14")
                item9 = types.KeyboardButton("15")
                item10 = types.KeyboardButton("15а")
                item11 = types.KeyboardButton("16с")
                item12 = types.KeyboardButton("16")
                item13 = types.KeyboardButton("17")
                item14 = types.KeyboardButton("21")
                item15 = types.KeyboardButton("24а")
                item16 = types.KeyboardButton("24")
                item17 = types.KeyboardButton("27")
                item18 = types.KeyboardButton("33")
                item20 = types.KeyboardButton("40б")
                item19 = types.KeyboardButton("Главное меню")
                markup.add(item1, item2, item3, item5, item4, item6, item7, item8, item9, item10, item11, item12, item13,
                           item14, item15, item16, item17, item18, item20 , item19 )
                bot.send_message(message.chat.id, 'Ты находишся в меню маршруток!', reply_markup=markup)




            elif message.text == '3' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'улица Генерала Карбышева - улица 40 лет Победы - улица Дружбы - бульвар Профсоюзов - улица Генерала Карбышева - улица Молодогвардейцев - проспект Ленина - Шоссейная улица - Грейдерная улица - Дамбовая улица', reply_markup=markup)



            elif message.text == '5' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'Коммунистическая улица - проспект Ленина - улица Молодогвардейцев - улица Генерала Карбышева - бульвар Профсоюзов - улица Мира - Оломоуцкая улица - улица Дружбы - улица 40 лет Победы - улица Генерала Карбышева',reply_markup=markup)








            elif message.text == '5а' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'Коммунистическая улица - проспект Ленина - улица Молодогвардейцев - улица Генерала Карбышева - бульвар Профсоюзов - улица Мира - Оломоуцкая улица - улица Дружбы', reply_markup=markup)








            elif message.text == '6а' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'улица Генерала Карбышева - улица 40 лет Победы - улица Дружбы - Оломоуцкая улица - улица Мира - бульвар Профсоюзов - улица Карбышева - улица Молодогвардейцев - проспект Ленина - Шоссейная улица - Западная улица - улица Гидростроителей', reply_markup=markup)








            elif message.text == '6' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'Улица Мира - бульвар Профсоюзов - улица Карбышева - улица Молодогвардейцев - проспект Ленина - Шоссейная улица - Западная улица - улица Гидростроителей', reply_markup=markup)








            elif message.text == '11' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'улица Карбышева - улица 40 лет Победы - улица Дружбы - бульвар Профсоюзов (обратно: улица Александрова) - улица Карбышева - улица Фридриха Энгельса - проспект Ленина - Коммунистическая улица - улица Карла Маркса', reply_markup=markup)








            elif message.text == '14а' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'Улица Пушкина - улица 40 лет Победы - улица Мира - улица Химиков - улица Энгельса - проспект Ленина - Шоссейная улица - Западная улица', reply_markup=markup)








            elif message.text == '14' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'Проспект Ленина - улица Энгельса - улица Химиков - улица Мира', reply_markup=markup)








            elif message.text == '15' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'Улица Горького - проспект Ленина - улица Энгельса - улица Химиков - улица Мира - Оломоуцкая улица - улица Дружбы - улица 40 лет Победы - улица Генерала Карбышева', reply_markup=markup)








            elif message.text == '15а' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'Улица Горького - проспект Ленина - улица Энгельса - улица Машиностроителей - бульвар Профсоюзов - улица Мира - Оломоуцкая улица - улица Дружбы - улица 40 лет Победы - улица Генерала Карбышева', reply_markup=markup)








            elif message.text == '16с' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'улица Генерала Карбышева - улица 40 лет Победы - улица Дружбы - Оломоуцкая улица - улица Мира - улица Александрова - проспект Ленина - Шоссейная улица - Дамбовая улица', reply_markup=markup)








            elif message.text == '16' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'Улица Медведева - улица Пушкина - улица Волжской Военной Флотилии - улица Мира - улица Александрова - проспект Ленина - Коммунистическая улица - улица Кирова (обратно: улица Горького) - улица Логинова', reply_markup=markup)








            elif message.text == '17' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'Проспект Ленина - улица Свердлова - улица Генерала Карбышева - бульвар Профсоюзов - улица Мира - Оломоуцкая улица - улица Дружбы', reply_markup=markup)








            elif message.text == '21' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'улица Пушкина - Пионерская улица - улица Мира - улица Химиков - улица Энгельса - проспект Ленина - Шоссейная улица - Западная улица - улица Гидростроителей', reply_markup=markup)








            elif message.text == '24а' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'улица Пушкина - Оломоуцкая улица - улица Мира - улица Генерала Карбышева - улица Свердлова - улица Кирова - улица Горького (только в обратном направлении) - Коммунистическая улица (только в обратном направлении)', reply_markup=markup)








            elif message.text == '24' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'улица Мира - улица Пионерская - улица Дружбы - улица Генерала Карбышева - улица Свердлова - улица Коммунистическая (только в обратном направлении) - улица Кирова (только в прямом направлении)', reply_markup=markup)








            elif message.text == '27' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'улица Пушкина - Пионерская улица - улица Дружбы - бульвар Профсоюзов - улица Генерала Карбышева - улица Молодогвардейцев - проспект Ленина', reply_markup=markup)








            elif message.text == '33' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'улица Пушкина - Пионерская улица - улица Дружбы - бульвар Профсоюзов - улица Генерала Карбышева - улица Молодогвардейцев - проспект Ленина', reply_markup=markup)








            elif message.text == '40б' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь маршрутки")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item1, item4)
                bot.send_message(message.chat.id, 'улица Генерал Карбышева - улица 40 лет Победы - улица Дружбы - улица Оломоуцкая - улица Мира - улица Химиков - улица Энгельса - проспект Ленина - улица Логинова - Автодорога № 6 - Заволжская улица - Паромная улица - Ленинская улица - улица Олега Кошевого - улица Панфилова - улица Энтузиастов - улица Калинина - Ташкентская улица - улица Олега Кошевого - улица Щорса', reply_markup=markup)










            #автобусы
            elif message.text == 'Узанать путь автобуса' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("№ 1")
                item2 = types.KeyboardButton("№ 2")
                item3 = types.KeyboardButton("№ 2у")
                item4 = types.KeyboardButton("№ 3")
                item5 = types.KeyboardButton("№ 4")
                item6 = types.KeyboardButton("№ 5")
                item7 = types.KeyboardButton("№ 11")
                item8 = types.KeyboardButton("№ 14")
                item9 = types.KeyboardButton("№ 15")
                item10 = types.KeyboardButton("№ 21")
                item11 = types.KeyboardButton("№ 27")
                item12 = types.KeyboardButton("№ 30")
                item13 = types.KeyboardButton("№ 34")
                item14 = types.KeyboardButton("№ 35")
                item15 = types.KeyboardButton("№ 41")
                item16 = types.KeyboardButton("№ 42")
                item17 = types.KeyboardButton("№ 51")
                item18 = types.KeyboardButton("№ 40к")
                item19 = types.KeyboardButton("Главное меню")


                markup.add(item1, item2, item3, item5, item4, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19)
                bot.send_message(message.chat.id, 'Ты в главном меню!', reply_markup=markup)


            elif message.text == '№ 1' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id, '32 м/р - ул.40 лет Победы - 25 м/р - 23 м/р - АТС-9 - Торговый центр - ул.Пионерская - "Юность" - Городская стоматологическая поликлиника - Уронефрологический центр - Поликлиника - ул.Королева - Центральный рынок - Парк - Выставочный бульвар - пл. им. В.И.Ленина - ул.Молодежная - ул.Космонавтов - пл.Свердлова - Больничный городок - ул.Горького - ЖДВ', reply_markup=markup)

            elif message.text == '№ 2' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 'пл. Свердлова - Больничный городок - ДК ВГС - пл. Строителей - Мост - Гавань (по требованию) - п.Экскаваторный - п.Шоферов - о.Зеленый-1 - о.Зеленый-2',
                                 reply_markup=markup)


            elif message.text == '№ 2у' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 '37 м/р - ул.Мира - ул. 87 Гвардейской дивизии - 32 м/р - ул.40 лет Победы (Университет) - 26 м/р - Гипермаркет "Магнит" - 28 м/р - ул.Александрова - 19 м/р - 12 м/р - По требованию - Уронефрологический центр - Поликлиника - ул.Королева - Центральный рынок - Парк - Выставочный бульвар - пл. им. В.И.Ленина - ул.Молодежная - ул.Космонавтов - пл.Свердлова - ДК ВГС - пл.Строителей - Гипермаркет "Магнит"',
                                 reply_markup=markup)

            elif message.text == '№ 3' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 'Парк - Выставочный бульвар - пл.им. В.И.Ленина - ул.Молодежная - ул.Космонавтов - пл.Свердлова - Больничный городок - ДК ВГС - пл.Строителей - Мост - Гавань (по требованию) - п.Эскаваторный - Первая - Вторая - Третья - Четвертая - Пятая - о.Зеленый (дамба)',
                                 reply_markup=markup)


            elif message.text == '№ 4' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 'Парк - Выставочный бульвар - пл.им. В.И.Ленина - ул.Молодежная - ул.Космонавтов - пл.Свердлова - Больничный городок - ДК ВГС - пл.Строителей - ул.Логинова - Мебельная фабрика - Завод Стальных конструкций - Поворот - 2-ой подъем - СНТ "Заканалье" - Пост ГиБДД - Городское кладбище №2 - Грузовой двор - МТФ - По требованию - Поворот - п.Паромный - ул.Калининская - СНТ "Цведущий сад"',
                                 reply_markup=markup)

            elif message.text == '№ 5' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 'пл.Свердлова - ДК ВГС - пл.Строителей - ул.Логинова - Мебельная фабрика - Грузовой порт - завод им.Макарова',
                                 reply_markup=markup)

            elif message.text == '№ 7' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 'пл.Строителей - ДК ВГС - пл.Свердлова - ул.Космонавтов - пл.им. В.И.Ленина - ул.Советская - Профучилище №3 - Волжский политех - ВПЗ (центральная проходная) - ВТЗ - ТПЦ-2 - Трамвайное депо - ТЭЦ-1 - Эктос-Волга - Гостиничный комплекс "Арт-Волжский" - Волжский механический завод - Сибур-Волжский',
                                 reply_markup=markup)

            elif message.text == '№ 11' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 'Площадь Труда - 10 м/р - ВПЗ - ВПЗ (центральная проходная) - ВТЗ - ТПЦ-2 - БЦ "Регион" - Ветеран-1 - Ветеран-2 - 2-ой подъем - СНТ "Заканалье" - Пост ГИБДД - Городское кладбище №2 Грузовой двор - МТФ - По требованию - Поворот - По требованию - База УПТК - СНТ "Заря" - По требованию - Новостройка - Башня - Школа (ЛПК) - По требованию - ВСО - Энергоцентр - ЖБИ - По требованию (Гаражи) - Пожарное депо - Микрорайон - По требованию - Частный поселок - Первая - Вторая - Третья - Конечная - СНТ "Лилия" (разворот)',
                                 reply_markup=markup)

            elif message.text == '№ 14' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 '37 м/р - Центр развития "Талисман" - Храм Серафима Саровского - 24 м/р - 22 микрорайон - ТРЦ "ВолгаМолл" - Поликлиника №4 - ул.Наримана Нариманова - ул.Пионерская - Магазин "Стимул" - ТЦ "Идея" - 10 м/р - ВПЗ - Оптовая база - 8 м/р - пл.Карбышева - ул.Советская - пл. им. В.И.Ленина - ул.Молодежная - ул.Космонавтов - пл.Свердлова - ДК ВГС - пл.Строителей - Гипермаркет "Магнит"',
                                 reply_markup=markup)
            elif message.text == '№ 15' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 'Парк - Выставочный бульвар - пл.им. В.И.Ленина - ул.Молодежная - ул.Космонавтов - пл.Свердлова - Больничный городок - ДК ВГС - пл.Строителей - ЦРМЗ - Шлюзы - Первая - Вторая - Третья - Четвертая - Пятая - Дачи ДОК',
                                 reply_markup=markup)

            elif message.text == '№ 21' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 '32 м/р - ул.40 лет Победы - ул. 40 лет Победы (университет) - 26 м/р - Аптека "Витафарм" - 23 м/р - АТС-9 - Торговый центр - ул.Пионерская - б-р Профсоюзов - ТЦ "Идея" - 10 м/р - ВПЗ - ВПЗ (центральная проходная) - ВТЗ - Трамвайное депо - ТЭЦ-1 - Эктос-Волга - Гостиничный комплекс "Арт-Волжский" - Волжский механический завод - Сибур-Волжский',
                                 reply_markup=markup)

            elif message.text == '№ 24' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 'Магазин "Стимул" - ул. Пионерская - "Юность" - Городская стоматологическая поликлиника - ТЦ "Простор" - ул. Королева - Завод Энерготехмаш - пл.Карбышева - ул.Молодежная - пл.Свердлова - Больничный городок - ул.Горького - ЖДВ г.Волжский',
                                 reply_markup=markup)

            elif message.text == '№ 27' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 'ул.Медведева - ул.87 Гвардейской дивизии - 30 м/р - 24 м/р - 22 м/р - 21 м/р - Школа - ул.Наримана Нариманова - Детская поликлиника - 10 м/р - ВПЗ',
                                 reply_markup=markup)

            elif message.text == '№ 30' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 '37 м/р - ТЦ "Нюран" - 24 м/р - 22 м/р - ТРЦ "ВолгаМолл" - 21 м/р - ул.Пушкина - РМЦ-2 - ЭНЦ-1 - ЭСПЦ - Сибур-Волжский - Волжский механический завод - Волтайр-Пром - Эктос-Волга - ТЭЦ-1',
                                 reply_markup=markup)

            elif message.text == '№ 34' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 'ЖДВ - ул.Горького - Больничный городок - пл.Свердлова - ДК ВГС - пл.Строителей - ул.Логинова - Мебельная фабрика - Завод Стальных конструкций - Поворот - 2-ой подъем - СНТ "Заканалье" - Пост ГиБДД - Городское кладбище №2 - Грузовой двор - МТФ - По требованию - Поворот - По требованию - База УПТК - СНТ "Заря" - По требованию - Новостройка - Башня - Школа - По требованию - ВСО - Энергоцентр - ЖБИ-4 - По требованию - Пожарное депо - Управление ЛПК - ул.Энтузиастов - Магазин - Поворот - ЛПК',
                                 reply_markup=markup)

            elif message.text == '№ 35' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 'ЛПК - Поворот - Магазин - ул.Энтузиастов - Управление ЛПК - Пожарное депо - По требованию - ЖБИ-4 - Энергоцентр - ВСО - Школа - Башня - Новостройка - По требованию - База УПТК - По требованию - Поворот - По требованию - МТФ - Городское кладбище №2 - Пост ГиБДД - СНТ "Заканалье" - 2-ой подъем - Поворот - Абразивный завод - ЛЭС - Нефтебаза - Трамвайное депо - ТЭЦ-1 - Эктос-Волга - Гостиничный комплекс "Арт-Волжский" - Волжский механический завод - Сибур-Волжский\n Обратный путь\n Сибур-Волжский - Волжский механический завод - Волтайр-Пром - Эктос-Волга - ТЭЦ-1 - Трамвайное депо - БЦ "Регион" - Нефтебаза - ЛЭС - Абразивный завод - Поворот - 2-ой подъем - СНТ "Заканалье" - Пост ГиБДД - Городское кладбище №2 - Грузовой двор - МТФ - По требованию - Поворот - По требованию - База УПТК - По требованию - Новостройка - Башня Школа - ВСО - Энергоцентр - ЖБИ-4 - По требованию - Пожарное депо - Управление ЛПК - ул.Энтузиастов - Магазин - Поворот - ЛПК',
                                 reply_markup=markup)

            elif message.text == '№ 41' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 '37 м/р - ТЦ "Нюран" - 24 м/р - ТРЦ "ВолгаМолл" - Поликлиника №4 - ул. Н.Нариманова - ул.Пионерская - Магазин "Стимул" - ТЦ "Идея" - 10 м/р - ВПЗ (центральная проходная) - ВТЗ - ТПЦ-2 - БЦ "Регион" - Ветеран-1 - Ветеран-2 - 2-ой подъем - СНТ "Заканалье" - Пост ГиБДД - Городское кладбище №2 - Грузовой двор - МТФ - По требованию - Поворот - СНТ "Волга" - СНТ "Трубник " - СНТ "Досуг" - СНТ "Взморье" (конечная)\n Обратный путь\n СНТ "Взморье" (конечная) - СНТ "Досуг" - СНТ "Трубник" - СНТ "Волга" - Поворот - По требованию - МТФ - Городское кладбище №2 - Пост ГиБДД - СНТ "Заканалье" - 2-ой подъем - Ветеран-2 - Ветеран-1 - ТПЦ-2 - ВТЗ - ВПЗ (центральная проходная) - Магазин - ТЦ "Идея" - Магазин "Стимул" - Рынок 10/16 - Центр занятости - ТРЦ "ВолгаМолл" - 25 м/р - 31 м/р - 38 м/р',
                                 reply_markup=markup)

            elif message.text == '№ 42' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 '37 м/р - ТЦ "Нюран" - 24 м/р - ТРЦ "ВолгаМолл" - Поликлиника №4 - ул. Н.Нариманова - ул.Пионерская - Магазин "Стимул" - ТЦ "Идея" - 10 м/р - ВПЗ - ВПЗ (центральная проходная) - ВТЗ - ТПЦ-2 - БЦ "Регион" - Ветеран-1 - Ветеран-2 - 2-ой подъем - СНТ "Заканалье" - Пост ГиБДД - Городское кладбище №2 - Грузовой двор - МТФ - По требованию - Поворот - п. Паромный - Правление - ул. Калининская - СНТ "Цветущий сад"\n Обратный путь\n СНТ "Цветущий сад" - ул. Калининская - Правление - п. Паромный - Поворот - По требованию - Грузовой двор - МТФ - Городское кладбище №2 - Пост ГиБДД - СНТ "Заканалье" - 2-ой подъем - Ветеран-2 - Ветеран-1 - ТПЦ-2 - ВТЗ - ВПЗ (центральная проходная) - ВПЗ - Магазин - ТЦ "Идея" - Магазин "Стимул" - Рынок 10/16 - Центр занятости - ТРЦ "ВолгаМолл" - 25 м/р - Центр развития "Талисман" (31 м/р) - ул. В.В. Флотилии - 38 м/р',
                                 reply_markup=markup)

            elif message.text == '№ 51' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 '37 м/р - Центр развития "Талисман" (30 м/р) - 24 м/р - 22 микрорайон - ТРЦ "ВолгаМолл" - Поликлиника №4 - ул.Наримана Нариманова - Рынок 10/16 - Магазин "Стимул" - "Юность" - Городская стоматологическая поликлиника - Уронефрологический центр - ул.Королева - Центральный рынок - Парк - "Выставочный бульвар" - пл.им. В.И.Ленина - ул.Молодежная - ул.Космонавтов - пл.Свердлова - Больничный городок - ДК ВГС - пл.Строителей - ул.Логинова - Мебельная фабрика - Завод стальных конструкций - Поворот - 2-ой подъем - СНТ "Заканалье" - Пост ГИБДД - Городское кладбище № 2\n обратный путь\n СНТ "Исток" - Городское кладбище №2 - Пост ГИБДД - СНТ "Заканалье" - 2-ой подъем - Поворот - Завод стальных конструкций - Мебельная фабрика - ул.Логинова - пл.Строителей - ДК ВГС - ул. Комсомольская - Больничный городок - Городской роддом - ул.Космонавтов - пл.им. В.И.Ленина - гостиница "Ахтуба" - Выставочный бульвар - Парк - Центральный рынок - ул.Королева - Городская стоматологическая поликлиника - "Юность" - Магазин "Стимул" - Рынок 10/16 - Центр занятости - ТРЦ "ВолгаМолл" - Магазин "Заря" - 25 м/р - Центр развития "Талисман" (31 м/р) - ул. В.В.Флотилии',
                                 reply_markup=markup)

            elif message.text == '№ 40к' and proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Узанать путь автобуса")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 'ПЛ.СТРОИТЕЛЕЙ - ГОРОДСКОЙ ПЛЯЖ',
                                 reply_markup=markup)


            elif message.text == 'promo' and proverka(message.from_user.id) and promo[message.from_user.id] == 'promo123':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Главное меню")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 'Поздравляю ты нашел секретный промокод! Что бы его активировать введи: promo123',
                                 reply_markup=markup)

            elif message.text == 'promo123' and message.from_user.id in ls and promo[message.from_user.id] == 'promo123':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Главное меню")
                markup.add(item1)
                bot.send_message(message.chat.id,
                                 "Вот код всего бота:",
                                 reply_markup=markup)



            elif message.text == 'Трамваи' and  proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item3 = types.KeyboardButton("Узнать путь трамвая!")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item3, item4)
                bot.send_message(message.chat.id, 'Ты в главном меню трамваев!', reply_markup=markup)

            elif message.text == 'Узнать путь трамвая!' and  proverka(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item3 = types.KeyboardButton("promo")
                markup.add(item3)
                bot.send_message(message.chat.id, 'Путь трамваев для меня еще не известен вот тебе за это промокод', reply_markup=markup)
                promo[message.from_user.id] = 'promo123'



            elif message.text == 'админ' and  proverka(message.from_user.id)  and proverka_admin(message.from_user.id):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item3 = types.KeyboardButton("добавить в черный список")
                item4 = types.KeyboardButton("Главное меню")
                markup.add(item3, item4)
                bot.send_message(message.chat.id, 'Ты в главном меню админов!', reply_markup=markup)



            elif message.text == 'даун' or message.text == 'Даун':
                bot.send_message(message.chat.id, 'Ты попал в черный список')
                add_black(message.from_user.id)







            else:
                if proverka(message.from_user.id):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item1 = types.KeyboardButton("Главное меню")
                    markup.add(item1)
                    bot.send_message(message.chat.id, 'Такой команды нет!', reply_markup=markup)

                elif black_spisok(message.from_user.id):
                    bot.send_message(message.chat.id, 'Ты в черном списке')
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    btn1 = types.KeyboardButton("Пройти регистрацию")
                    btn2 = types.KeyboardButton('Уйти')
                    btn3 = types.KeyboardButton('Почему я не могу пользоваться другими командами?')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, text="Люди которые не зарегестрированны не могут пользоваться всеми командами бота! ".format(message.from_user),
                                     reply_markup=markup)


















    # АДМИНИСТРАЦИЯ

    #   else:

    #       @bot.message_handler(content_types='text')
    #       def message_reply(message):
    #           if message.text=="Добавить в черный список пользователя":
    #               markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    #               item1=types.KeyboardButton("abcd")
    #               markup.add(item1)
    #               bot.send_message(message.chat.id,'Напиши в чат символы: abcd',reply_markup=markup)


























    #функции
    def quit():
        exit()

    def writing():
        with open('юзеры.txt', 'a') as f:
            for i in ls:
                i = str(i)
                print(i, file=f)



    bot.polling(none_stop=True)
    bot.infinity_polling()

except BaseException as erors:
    writing()
    check_erors = True
    print(erors)
    quit()\



# -textmode -nosound -nopreloadel -console -nojoy -noipx -nocrashdialog -sw -noborder