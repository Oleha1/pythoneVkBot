import config

from vkbottle.bot import Bot, Message

import keyBoardUtils

bot = Bot(token=config.get("bot", "token"))


@bot.on.private_message(text="Начать")
@bot.on.private_message(payload={"cmd": "menu"})
async def main(message: Message):
    await message.answer("Меню", keyboard=keyBoardUtils.getMainMenu())


@bot.on.private_message(payload={"cmd": "info"})
async def info(message: Message):
    await message.answer("Компания «БизнесАвто» существует с 2013 г. Основное направление деятельности компании "
                         "продажа запасных частей и аксессуаров для автомобилей марки КАМАЗ. Компания работает с "
                         "поставщиками и дилерами Камского автозавода, поэтому гарантирует оригинальность продаваемых "
                         "запчастей.", keyboard=keyBoardUtils.getBackMenu())


@bot.on.private_message(payload={"cmd": "items"})
async def items(message: Message):
    await message.answer("В наш ассортимент входя:\n"
                         "автозапчасти, различный расходники, аксессуары, прицепы",
                         keyboard=keyBoardUtils.getBackMenu())


@bot.on.private_message(payload={"cmd": "delivery"})
async def delivery(message: Message):
    await message.answer("Есть 2 способа доставки:\n"
                         " Доставка транспортной службой магазина — 350 руб. по г. Курган\n"
                         " Доставка транспортной компанией",
                         keyboard=keyBoardUtils.getBackMenu())


@bot.on.private_message(payload={"cmd": "contacts"})
async def contacts(message: Message):
    await message.answer("Пункт выдачи: г. Курган, ул. Дзержинского, д. 68\n"
                         "Электронная почта: bizauto@inbox.ru\n"
                         "Телефон: \n+7 3522-55-86-86 \n+7-912-835-86-86 (WhatsApp, Viber, Telegram)\n"
                         "Обработка заказов производится с 8:30 до 18:30 с понедельника по пятницу.",
                         keyboard=keyBoardUtils.getBackMenu())


bot.run_forever()
