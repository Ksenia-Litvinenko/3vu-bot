from aiogram import Bot, Dispatcher, F  
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, Message
from aiogram.filters import Command
from random import choice
import asyncio


bot = Bot(token="")
dp = Dispatcher()

kd = ReplyKeyboardMarkup(
    Keyboard=[
        [KeyboardButton(text="Меркурий")],
        [KeyboardButton(text="Венера")],
        [KeyboardButton(text="Земля")],
        [KeyboardButton(text="Марс")],
        [KeyboardButton(text="Юпитер")],
        [KeyboardButton(text="Сатурн")],
        [KeyboardButton(text="Уран ")],
        [KeyboardButton(text="Нептун")]
        
        
    ],
    resize_keyboard=True
) 


mercisr = ["Меркурій найменша та найшвидша планета Сонячної системи","Меркурій розташований найближче до Сонця"," Поверхня Меркурія вкрита кратерами і схожа на Місяць"]



@dp.message(F.text == "Меркурий")
async def on(message: Message):
    await message.answer(choice(mercisr))


vvv = ["найгарячіша планета Сонячної системи ","Венера обертається навколо своєї осі у зворотному напрямку "]

@dp.message(F.text == "Венера")
async def on(message: Message):
    await message.answer(choice(vvv))



zamza = ["71% поверхні Землі вкрито водою, але лише 3% з неї — прісна","Земля утворилася приблизно 4,54 мільярда років тому","Маса планети Земля становить приблизно 5,9722  кілограмів"]




@dp.message(F.text == "Земля")
async def on(message: Message):
    await message.answer(choice(zamza))



mmm = ["На Марсі розташована гора Олімп це найвища гора Сонячної системи","Свій червоний колір планета має через високий вміст оксиду заліза (іржі) у ґрунті, який вкриває її поверхню.","Марсіанська доба  Марсіанська доба (її називають «сол») триває 24 години 39 хвилин і 35 секунд"]


@dp.message(F.text == "Марс")
async def on(message: Message):
    await message.answer(choice(mmm))



jpj = ["Юпитер в 11 раз шире Земли по диаметру ","Юпитер состоит преимущественно из водорода и гелия"," На Юпитере уже более 350 лет бушует колоссальный шторм, известный как Большое красное пятно, размер которого превышает размеры Земли"]


@dp.message(F.text == "Юпитер")
async def on(message: Message):
    await message.answer(choice(jpj))

scs = ["Знаменитые кольца Сатурна состоят в основном из водяного льда, пыли и камней.","Сатурн — единственная планета в Солнечной системе, средняя плотность которой меньше плотности воды","Сатурн невероятно быстро вращается вокруг своей оси. Один оборот занимает всего около 10,7 земных часов"]

@dp.message(F.text == "Сатурн")
async def on(message: Message):
    await message.answer(choice(scs))




uren = ["Ось вращения Урана наклонена на рекордные 98 градусов","Хотя Урана это газовый гигант, температура в его верхних слоях атмосферы опускается до -224 градусов "]



@dp.message(F.text == "Уран")
async def on(message: Message):
    await message.answer(choice(uren))



npt = ["Один оберт навколо Сонця Нептун робить за 165 земних років","На Нептуні дмуть найпотужніші вітри в усій Сонячній системі. Швидкість ураганів сягає колосальних 2100 км/год "]



@dp.message(F.text == "Нептун")
async def on(message: Message):
    await message.answer(choice(npt))



async def main():
    await dp.start_polling(bot)
    
asyncio.run(main())

