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
#    along with this program.  If not, see <https://www.gnu.org/licenses/

# Locals
probability_word = 'Веротность'
willhappen_verb = 'произойдёт'
what_word = 'что'

@bot.on.message(command='орелилирешка')
async def flip(message: Message):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        flip = ['Орёл!', 'Решка!']
        await message.reply(random.choice(flip))

@bot.on.message(text='/шанс <text>')
async def chance_command(message: Message, text):
    procent = random.randint(0, 100)
    await message.reply(f'{probability_word} {what_word} {text} {willhappen_verb} {procent}%')
    await update_stats(message)
