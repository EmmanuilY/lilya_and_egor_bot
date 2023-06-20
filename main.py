from aiogram import Bot, Dispatcher, types # импортируем функции из библиотки
from aiogram import executor

bot = Bot(token='6015696878:AAFn5mZ8CyssDC_syAa-SrVsHLqxbUdjltI') # создаем бота
dp = Dispatcher(bot) #настраиваем сервер

# пишем список покупок. Здесь я реализовал это в виде строки для простоты
party_in_nature = """Бутылка водки: 3
Пакет пива: 2
Бутылка вина: 2
Шашлык: 5 кг
Хлеб: 5 буханок
Вода: 10 бутылок
Уголь для мангала: 1 пакет
"""
# второй список покупок
party_at_home = """Бутылка водки: 2
Пакет пива: 3
Бутылка вина: 3
Чипсы: 5 пакетов
Пицца: 3 штуки
Кола: 5 бутылок
"""

#тут пишем логику если боту отправят /start или /help
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Напиши 'бухаем на природе' или 'бухаем на хате', чтобы я помог с покупками.")

#тут логика для бухаем на природе. Бот будет откликаться только на 'бухаем на природе'
@dp.message_handler(lambda message: message.text == 'бухаем на природе') # обратите внимание на @, это пока для вас магия :)
async def party_nature(message: types.Message): # async значит асинхронный, но об этом потом. def - это объявление функции, а party_nature название функции
    await message.reply(party_in_nature) #

#тоже самое для хаты
@dp.message_handler(lambda message: message.text == 'бухаем на хате')
async def party_home(message: types.Message):
    await message.reply(party_at_home)


if __name__ == '__main__':
    """
    выше базовая конструкция, которая говорит что если мы запускаем именно этот скрипт через терминал, 
    то он начинает исполнять код который ниже.
    Кстати, ваш скрипт необязательно должен называться main.py, он может называться gavno.py и все-равно будет запускаться без изменения кода
    
    п.с. обратите внимание. Комментарии можно оставлять и через #, но это штука только для одной строки. 
    А эта штука удобнее и её чаще юзают
    """
    executor.start_polling(dp, skip_updates=True) # тут мы запускаем сервер, который постоянно проверяет, написали нам или нет
