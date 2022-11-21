#    Daemon Project
#    Copyright (C) 2021-2022 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


# Config
spam_limit = 9999

# Locals
correct_use_spam = '❗Правильное использование: /спам <txt>//<count> (txt - текст, count - количество сообщений которое отправит бот (не больше  9999))'
error_msg = 'Ошибка при отправке сообщения'
spam_limit_msg = f'К сожалению в этой инстанции действует ограничение в {spam_limit} сообщение :('

@bot.on.chat_message(text='/спам <spam>//<count>')
async def spam(message: Message, spam, count):
    if await check_bl_wl(message) != False:
        if not await check(message, id=message.from_id):
            await message.reply(noadmin)
        else:
            ammount = int(count)
            if ammount < spam_limit:
                for i in range(ammount):
                    await message.answer(f'{spam}')
            else:
                await message.reply(spam_limit_msg)

@bot.on.chat_message(text='/спам <text>')
async def spam_error(message: Message, text):
    await message.reply(correct_use_spam)
    await update_stats(message)

@bot.on.chat_message(command='/спам')
async def spam(message: Message,):
    if await check_bl_wl(message) != False:
        await message.reply(correct_use_spam)
        await update_stats(message)
