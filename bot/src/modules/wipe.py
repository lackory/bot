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

# Locals
yes_text = 'Да'
no_text = 'Нет'
successfully_wipe = '🧹 Вы успешно очистили беседу.'
wipe_check_msg = 'Вы уверены что хотите выполнить сброс всей бд этого чата? Это действие НЕЛЬЗЯ отменить'
cancel_msg = 'Успешно отменено'

# Config
wipe_buttons = Keyboard(inline=True)
wipe_buttons.add(Text(no_text, {"cmd": "no"}), color=KeyboardButtonColor.POSITIVE)
wipe_buttons.add(Text(yes_text, {"cmd": "yes"}), color=KeyboardButtonColor.NEGATIVE)
wipe_buttons = wipe_buttons.get_json()

@bot.on.chat_message(command='очистить')
async def wipe(message: Message):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        if not await check(message, id=message.from_id):
            await message.reply(noadmin)
        else:
            await message.reply(wipe_check_msg, keyboard=wipe_buttons)
            await update_stats(message)

@bot.on.message(payload={"cmd": "нет"})
async def no_reply(message: Message):
    if await check(message, id=message.from_id):
        await message.reply(cancel_msg)
        await update_stats(message)
    else:
        await message.reply(noadmin)

@bot.on.message(payload={"cmd": "да"})
async def yes_action(message: Message):
    if await check(message, id=message.from_id):
        q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
        result = q.fetchall()
        kolvo = result[0][2]
        q.execute(f"UPDATE players SET kolvo = '0' WHERE id = '{message.peer_id}'")
        connection.commit()
        f = open(f'{dir_to_txt}{message.peer_id}.txt', 'w', encoding='utf8')
        f.write('')
        f.close()
        f = open(f'{dir_to_pic}{message.peer_id}.txt', 'w', encoding='utf8')
        f.write('')
        f.close()
        await message.reply(successfully_wipe)
        await update_stats(message)
    else:
        await message.reply(noadmin)
