from aiogram import Bot, Dispatcher, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from random import choice
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found!")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

kd = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Меркурий")],
        [KeyboardButton(text="Венера")],
        [KeyboardButton(text="Земля")],
        [KeyboardButton(text="Марс")],
        [KeyboardButton(text="Юпитер")],
        [KeyboardButton(text="Сатурн")],
        [KeyboardButton(text="Уран")],
        [KeyboardButton(text="Нептун")]
    ],
    resize_keyboard=True
)

mercisr = [
    "Меркурій — найменша та найшвидша планета Сонячної системи",
    "Меркурій розташований найближче до Сонця",
    "Поверхня Меркурія вкрита кратерами і схожа на Місяць"
]

vvv = [
    "Венера — найгарячіша планета Сонячної системи",
    "Венера обертається навколо своєї осі у зворотному напрямку"
]

zamza = [
    "71% поверхні Землі вкрито водою, але лише 3% з неї — прісна",
    "Земля утворилася приблизно 4,54 мільярда років тому",
    "Маса планети Земля становить приблизно 5,9722 × 10²⁴ кг"
]

mmm = [
    "На Марсі розташована гора Олімп — це найвища гора Сонячної системи",
    "Червоний колір Марса пояснюється великою кількістю оксиду заліза",
    "Марсіанська доба триває 24 години 39 хвилин і 35 секунд"
]

jpj = [
    "Юпітер у 11 разів ширший за Землю",
    "Юпітер складається переважно з водню та гелію",
    "На Юпітері понад 350 років вирує Велика червона пляма"
]

scs = [
    "Кільця Сатурна складаються переважно з льоду, пилу та каміння",
    "Сатурн має меншу густину, ніж вода",
    "Один оберт Сатурна триває приблизно 10,7 години"
]

uren = [
    "Вісь обертання Урана нахилена на 98 градусів",
    "Температура атмосфери Урана може опускатися до −224°C"
]

npt = [
    "Нептун робить один оберт навколо Сонця за 165 років",
    "На Нептуні найсильніші вітри у Сонячній системі"
]


@dp.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer(
        "Оберіть планету:",
        reply_markup=kd
    )


@dp.message(F.text == "Меркурий")
async def mercury_handler(message: Message):
    await message.answer(choice(mercisr))


@dp.message(F.text == "Венера")
async def venus_handler(message: Message):
    await message.answer(choice(vvv))


@dp.message(F.text == "Земля")
async def earth_handler(message: Message):
    await message.answer(choice(zamza))


@dp.message(F.text == "Марс")
async def mars_handler(message: Message):
    await message.answer(choice(mmm))


@dp.message(F.text == "Юпитер")
async def jupiter_handler(message: Message):
    await message.answer(choice(jpj))


@dp.message(F.text == "Сатурн")
async def saturn_handler(message: Message):
    await message.answer(choice(scs))


@dp.message(F.text == "Уран")
async def uranus_handler(message: Message):
    await message.answer(choice(uren))


@dp.message(F.text == "Нептун")
async def neptune_handler(message: Message):
    await message.answer(choice(npt))


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
