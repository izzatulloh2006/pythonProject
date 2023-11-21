import asyncio
import logging
import sys
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram import Bot ,Dispatcher
from  aiogram.filters.command import Command
from pythonProject.avtoserviz_bot import tugmalar



TOKEN = '6560118733:AAEYKRJBeuYhYU2iIJ49Uv64pcfC3I13Cp4'

dp = Dispatcher()

@dp.message(Command('start'))
async def start_hander(msg : Message):
    await msg.answer("ASSALOMU ALAYKUM ! 🚘🚖🚙🛻🔧🪛 BIZNING AVTOSERVIZ BOTIMIZGA  XUSH KELIBSIZ! " )
    await msg.answer(reply_markup=tugmalar())

@dp.message(lambda msg: msg.text == '🔧 XIZLATLAR')
async def one_hander(msg: Message):
    await msg.answer('🔧 XIZLATLAR')
    # await msg.answer(reply_markup=tugmalar)







async def main() -> None:
     bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
     await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
