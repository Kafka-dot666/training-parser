# bot.py
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils import executor
from parser import parse_data  # Импорт функции из парсера

API_TOKEN = 'YOUR_API_TOKEN'  # Замените на ваш токен

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Напишите 'get', чтобы получить данные.")

@dp.message_handler(lambda message: message.text.lower() == 'get')
async def get_data(message: types.Message):
    await message.reply("Начинаем сбор данных...")
    
    # Получение данных из парсера
    try:
        data = parse_data()  # Получить данные
        if data:
            response = "Собранные данные:\n" + "\n".join([f"Value: {item['value']}, Text: {item['text']}" for item in data])
            await message.reply(response)
        else:
            await message.reply("Нет данных для отображения.")
    except Exception as e:
        await message.reply(f"Ошибка при получении данных: {e}")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Доступные команды:\n/start - начальное сообщение\n/get - получить данные")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
