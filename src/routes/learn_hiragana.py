from vkbottle.bot import BotLabeler, Message

bl = BotLabeler()

@bl.message(text=["Дай карточку"])
async def greeting(message: Message):
    await message.answer("Вот держи!")