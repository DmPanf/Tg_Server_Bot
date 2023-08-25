from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsReply(BoundFilter):
    """Checks if message is reply to another message"""

    async def check(self, message: types.Message):
        myMsg = 'ID: <b>' + str(message.chat.id) + '</b>'
#        await message.answer(myMsg, parse_mode=ParseMode.MARKDOWN)
#        await bot.send_message(ID[0], myMsg, parse_mode=ParseMode.MARKDOWN) # Main Dim1 (Mi8)
#        await bot.send_message(ID[1], myMsg, parse_mode=ParseMode.MARKDOWN) # Main Dim2 (MiMax)
#        await bot.send_message(ID[2], myMsg, parse_mode=ParseMode.MARKDOWN) # Teplomonitor (vti-monitor)
#        return message.reply_to_message
        return message.answer(myMsg)
