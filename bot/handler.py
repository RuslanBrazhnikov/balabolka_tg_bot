from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup
from random import randrange


async def on_startup(_):
    print('Я запустился!')


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> - <em>эт список команд</em>
<b>/start</b> - <em>эт работа с ботом</em>
<b>/give</b> - <em>эт смешной котик</em>
<b>/photo</b> - <em>получи картинку</em>
<b>/video</b> - <em>смотреть видосы</em>
<b>/description</b> - <em>описание нашего Бота</em>
<b>/random</b> - <em>рандомная точка на карте</em>
<b>/links</b> - <em>перейти к картинкам</em>
<b>/search</b> - <em>поиск информации</em>
<b>/music</b> - <em>слушать музыку</em>
"""


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(
        '<em>Привет! <b>Добро пожаловать</b> в наш Бот! Введи <b>/help</b> для просмотра списка команд.</em>',
        parse_mode="HTML", reply_markup=kb)


@dp.message_handler(commands=['description'])
async def description(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Наш бот просто прикольный!', parse_mode="HTML")


@dp.message_handler(commands=['music'])
async def send_stick_cat(message: types.Message):
    await bot.send_audio(chat_id=message.from_user.id, audio='https://t.me/music_muzyka/14852')
    await bot.send_audio(chat_id=message.from_user.id, audio='https://t.me/music_muzyka/14855')
    await bot.send_audio(chat_id=message.from_user.id, audio='https://t.me/music_muzyka/14877')
    await bot.send_audio(chat_id=message.from_user.id, audio='https://t.me/music_muzyka/14879')
    await bot.send_audio(chat_id=message.from_user.id, audio='https://t.me/music_muzyka/14886')
    await bot.send_audio(chat_id=message.from_user.id, audio='https://t.me/music_muzyka/14891')
    await bot.send_audio(chat_id=message.from_user.id, audio='https://t.me/music_muzyka/15165')


@dp.message_handler(commands=['search'])
async def search_inf(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Выбери поисковик...либо картинку', reply_markup=ikb)


@dp.message_handler(commands=['random'])
async def send_random(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id, latitude=randrange(1, 100), longitude=randrange(1, 100))


@dp.message_handler(commands=['photo'])
async def send_image(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo='https://avatars.mds.yandex.net/i?id=b7ef3175e2c995dffb4375572d0ce3addcce373f-8159483'
                               '-images-thumbs&n=13')


@dp.message_handler(commands=['links'])
async def links_command(message: types.Message):
    await message.answer(text='Выберите картинку...', reply_markup=ikb)


@dp.message_handler(commands=['video'])
async def location(message: types.Message):
    await bot.send_video(chat_id=message.from_user.id, video='https://t.me/anegdot2023/1400')
    await bot.send_video(chat_id=message.from_user.id, video='https://t.me/anegdot2023/1398')
    await bot.send_video(chat_id=message.from_user.id, video='https://t.me/anegdot2023/1397')
    await bot.send_video(chat_id=message.from_user.id, video='https://t.me/anegdot2023/1396')
    await bot.send_video(chat_id=message.from_user.id, video='https://t.me/anegdot2023/1391')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND, parse_mode='HTML')


@dp.message_handler(commands=['give'])
async def send_sticker(message: types.Message):
    await message.answer('Смотри какой смешной котик ❤️ ')
    await bot.send_sticker(message.from_user.id,
                           sticker='CAACAgIAAxkBAAEHeBpj08Qmf6pQY7uD7QXYOSdWhjhE9QAC8AADyUpYAAGPK97jaKKyES0E')
