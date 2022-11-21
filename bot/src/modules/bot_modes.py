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
bad_arg_in_gen = 'Можно только /дем и текст'
gen_mod = f'Теперь я снова генерирую без остановок'
now_i_only_learn = f'Теперь я только обучаюсь'
gen_only_dem_mod = f'Теперь я генерирую демотиваторы!'
gen_only_msg = f'Теперь я буду генерировать фразы'
correct_use_dst_arg = 'Правильное использование: с дст true or false'
correct_use_arr_arg = 'Правильное использование: аргумент true or false'
correct_use_dem_arg = 'Правильное использование: c ген dem/text'
correct_use_learn_arg= 'Правильное использование: читать true/false'
please_set_amount_words = 'Укажите количество слов'
please_set_amount_photo = 'Укажите количество фотографий'
mininal_message_to_gen = 'Минимальное кол-во слов для генерации: 3'
minimal_photo_amount = 'Минимальное кол-во фотографий для генерации: 1'
new_ammount_msg = 'Новое значение'

@bot.on.chat_message(text=['/с ген', 'с ген'])
async def sgennoarg(message: Message):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        await message.reply(bad_arg_in_gen)

@bot.on.chat_message(text=['/с ген <st>', 'с ген <st>'])
async def sgenset(message: Message, st):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        if not await check(message, id=message.from_id):
            await message.reply(noadmin)
        else:
            if st == 'text':
                q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
                result = q.fetchall()
                status = result[0][1]
                q.execute(f"UPDATE players SET status = '1' WHERE id = '{message.peer_id}'")
                connection.commit()
                await message.reply(gen_only_msg)
            elif st == 'dem':
                q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
                result = q.fetchall()
                status = result[0][1]
                q.execute(f"UPDATE players SET status = '0' WHERE id = '{message.peer_id}'")
                connection.commit()
                await message.reply(gen_only_dem_mod)
            else:
                await message.reply(correct_use_dem_arg)
            await update_stats(message)

# Mode
@bot.on.chat_message(text=['/читать', 'читать'])
async def s_learn_noarg(message: Message):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        await message.reply(correct_use_learn_arg)

@bot.on.chat_message(text=['/читать <st>', 'читать <st>'])
async def slearn(message: Message, st):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        if not await check(message, id=message.from_id):
            await message.reply(noadmin)
        else:
            if st.lower() == 'true':
                q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
                result = q.fetchall()
                learn = result[0][7]
                q.execute(f"UPDATE players SET learn = '1' WHERE id = '{message.peer_id}'")
                connection.commit()
                await message.reply(now_i_only_learn)
            elif st.lower() == 'false':
                q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
                result = q.fetchall()
                learn = result[0][7]
                q.execute(f"UPDATE players SET learn = '0' WHERE id = '{message.peer_id}'")
                connection.commit()
                await message.reply(gen_mod)
            else:
                await message.reply(correct_use_learn_arg)
            await update_stats(message)

@bot.on.chat_message(text='с дст <st>')
async def s_dst(message: Message, st):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        if not await check(message, id=message.from_id):
            await message.reply(noadmin)
        else:
            if st.lower() == 'true':
                q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
                result = q.fetchall()
                status = result[0][5]
                q.execute(f"UPDATE players SET dst = '1' WHERE id = '{message.peer_id}'")
                connection.commit()
                await message.reply(f'Distorion mode: {st}')
            elif st.lower() == 'false':
                q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
                result = q.fetchall()
                status = result[0][5]
                q.execute(f"UPDATE players SET dst = '0' WHERE id = '{message.peer_id}'")
                connection.commit()
                await message.reply(f'Distorion mode: {st}')
            else:
                await message.reply(correct_use_dst_arg)
            await update_stats(message)

@bot.on.chat_message(text=['аргумент <st>', '/аргумент <st>'])
async def s_arr(message: Message, st):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        if not await check(message, id=message.from_id):
            await message.reply(noadmin)
        else:
            if st.lower() == 'true':
                q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
                result = q.fetchall()
                arrange = result[0][8]
                q.execute(f"UPDATE players SET arrange = '1' WHERE id = '{message.peer_id}'")
                connection.commit()
                await message.reply(f'Arrange mode: {st}')
            elif st.lower() == 'false':
                q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
                result = q.fetchall()
                arrange = result[0][8]
                q.execute(f"UPDATE players SET arrange = '0' WHERE id = '{message.peer_id}'")
                connection.commit()
                await message.reply(f'Arrange mode: {st}')
            else:
                await message.reply(correct_use_arr_arg)
            await update_stats(message)

@bot.on.chat_message(text=['/с арр', 'с арр'])
async def sarr_noarg(message: Message):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        await message.reply(correct_use_arr_arg)
    await update_stats(message)

@bot.on.chat_message(text=['/усттекст', 'усттекст', '/усттекст'])
async def picgen3(message: Message):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        await message.reply(please_set_amount_words)
    await update_stats(message)

@bot.on.chat_message(text=['/усттекст <txt>', 'усттекст <txt>', 'усттекст <txt>', '/усттекст <txt>'])
async def settext(message: Message, txt):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        if not await check(message, id=message.from_id):
            await message.reply(noadmin)
        else:
            if int(txt) >= 3:
                q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
                result = q.fetchall()
                txtgen = result[0][4]
                q.execute(f"UPDATE players SET txtgen = '{txt}' WHERE id = '{message.peer_id}'")
                connection.commit()
                await message.reply(f'{new_ammount_msg} - {txt}')
            else:
                await message.reply(mininal_message_to_gen)

@bot.on.chat_message(text=['/устфото', 'устфото', '/устфото', 'устфото'])
async def setphotonarg(message: Message):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        await message.reply(please_set_amount_photo)

@bot.on.chat_message(text=['устфото <txt>', 'устфото <txt>', '/устфото <txt>'])
async def setphoto(message: Message, txt):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        if not await check(message, id=message.from_id):
            await message.reply(noadmin)
        else:
            if int(txt) >= 1:
                q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
                result = q.fetchall()
                picgen = result[0][3]
                q.execute(f"UPDATE players SET picgen = '{txt}' WHERE id = '{message.peer_id}'")
                connection.commit()
                await message.reply(f'{new_ammount_msg} - {txt}')
            else:
                await message.reply(minimal_photo_amount)
    await update_stats(message)
