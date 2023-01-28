from handler import *

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/give')
b3 = KeyboardButton('/photo')
b4 = KeyboardButton('/video')
b5 = KeyboardButton('/description')
b6 = KeyboardButton('/music')
b7 = KeyboardButton('/random')
b8 = KeyboardButton('/links')
b9 = KeyboardButton('/search')
kb.add(b1).insert(b2).insert(b3).insert(b4).insert(b5).insert(b6).insert(b7).insert(b8).insert(b9)

ikb = InlineKeyboardMarkup(row_width=2)

ik1 = InlineKeyboardButton(text="Морской котик",
                           url='https://avatars.mds.yandex.net/i?id=f285710e2696de8d2179b30a50fc11f9e51eea60-7467285'
                               '-images-thumbs&n=13')
ik2 = InlineKeyboardButton(text="Зебры",
                           url="https://avatars.mds.yandex.net/i?id=dbbcbf018dbd647d12f58b01ab3a8a9954bc25be-6898416"
                               "-images-thumbs&n=13")
ik3 = InlineKeyboardButton(text='Google', url='https://www.google.ru/')
ik4 = InlineKeyboardButton(text='Яндекс', url='https://ya.ru/?utm_referrer=https%3A%2F%2Fyandex.ru%2F')
ikb.add(ik1).add(ik2).add(ik3).add(ik4)
