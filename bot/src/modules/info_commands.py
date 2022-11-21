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

# Imports
import psutil, platform, cpuinfo, datetime, psutil._common
from sys import version
from datetime import timedelta

# Config
cpu_name = cpuinfo.get_cpu_info()['brand_raw']

# Locals
bot_ver_title = 'Версия бота:'
platform_title = 'Платформа:'
python_ver_title = 'Версия Python:'
pong_msg = 'Pong!'
cpu_use_title = 'Загруженность CPU:'
cores_title = 'ядрер'
threads_title = 'потоков'
ram_use_title = 'Загруженность RAM:'
total_ram_title = 'всего:'
modules_title = 'Модулей:'
uptime_title = 'Uptime:'
settings_msg = '⚙️ Доступные настройки:\n\ns dst true/false - дисторион мод фотографий у демотиватора.\ns text <значение> - кол-во текста для генерации\ns photo <значение> - кол-во фоток для генерации\ns learn True/False - бот будет молчать и обучаться\ns gen dem/text - что будет генерировать - демотиваторы или текст\ns arr True/False - Не сжимать демотиватор (Рамка демотиватора будет регулироваться под изображение)'
ping_msg = 'Pong!'
donate_msg = 'Спасибо что вы хотите поддержать этот проект! Мы ценим ваш вклад в наше развитие :)\n\nВаша ссылка для осуществления платежа:\nhttps://clck.ru/amoW6'

async def get_chat_level(message):
    q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
    result = q.fetchall()
    chat_gen_msgs_num = result[0][9]
    chat_num_compare = config.levels.copy()
    chat_num_compare.append(int(chat_gen_msgs_num) + 1)
    chat_num_compare.sort()
    return chat_num_compare.index(int(chat_gen_msgs_num) + 1)
    connection.commit()

async def get_user_level(message):
    q.execute(f"SELECT * FROM players WHERE id = {message.from_id}")
    result = q.fetchall()
    user_gen_msgs_num = result[0][9]
    user_num_compare = config.levels.copy()
    user_num_compare.append(int(user_gen_msgs_num) + 1)
    user_num_compare.sort()
    return user_num_compare.index(int(user_gen_msgs_num) + 1)
    connection.commit()


@bot.on.chat_message(command='инфа')
async def info(message: Message):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        pic2 = 0
        with open(dir_to_pic + str(message.peer_id) + '.txt', encoding='utf8') as f:
            for line in f:
                pic2 = pic2 + 1
        lines = 0
        with open(dir_to_txt + str(message.peer_id) + '.txt', encoding='utf8') as f:
            for line in f:
                lines = lines + 1
        q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
        result = q.fetchall()
        status = result[0][1]
        kolvo = result[0][2]
        picgen = result[0][3]
        txtgen = result[0][4]
        mode = result[0][5]
        learn = result[0][7]
        arrange = result[0][8]
        connection.commit()
        if status == 1:
            status = 'текст'
        else:
            status = 'демотиваторы'
        if arrange == 1:
            arrmode = 'True'
        else:
            arrmode = 'False'
        if learn == 1:
            ginfo = 'Я только обучаюсь'
            lrn = 'True'
        else:
            ginfo = f'{txtgen} слов и {picgen} картинок\nДо следующей генерации {txtgen-kolvo} слов'
            lrn = 'False'
        if mode == 1:
            md = 'True'
        else:
            md = 'False'
        await message.reply(f'ID беседы: {message.peer_id-2000000000}\nВсего в базе {lines} сообщений и {pic2} картинок\nРежим беседы: {status}\n\nНастройки:\nDistorion mode: {md}\nonly.learn = {lrn}\nArrange mode: {arrmode}\n\nГенерация через каждые: {ginfo}')
        await update_stats(message)

@bot.on.chat_message(command='параметры')
async def settings(message: Message):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        await message.reply(settings_msg)
        await update_stats(message)

@bot.on.chat_message(command='стат')
async def get_stats(message: Message):
    await update_stats(message)
    if await check_bl_wl(message) != False:
        q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
        result = q.fetchall()
        gen_msgs = result[0][9]
        q.execute(f"SELECT * FROM players WHERE id = {message.from_id}")
        user_gen_msgs = q.fetchall()[0][9]
        user_id = message.from_id
        user_level = await get_user_level(message)
        chat_level = await get_chat_level(message)
        await message.reply(f'Ваш ID: {user_id}\nСообщения, отправленные мной по вашему запросу: {user_gen_msgs}*\nВсего сообщений отправленно мной в этом чате: {gen_msgs}*\nВаш уровень: {user_level} - {config.level_names[user_level - 1]}\nУровень чата: {chat_level} - {config.level_names[chat_level - 1]}\n\n* - включает в себя цитаты, шутки, демотиваторы и просто сгенерированные сообщения.')
        connection.commit()

@bot.on.private_message(command='стат')
async def get_stats(message: Message):
    await addtobd(message.from_id)
    if await check_bl_wl(message) != False:
        q.execute(f"SELECT * FROM players WHERE id = {message.from_id}")
        connection.commit()
        user_gen_msgs = q.fetchall()[0][9]
        user_id = message.from_id
        user_level = await get_user_level(message)
        await message.reply(f'Ваш ID: {user_id}\nСообщения, отправленные мной по вашему запросу: {user_gen_msgs}*\nВаш уровень: {user_level} - {config.level_names[user_level - 1]} \n\n* - включает в себя цитаты, шутки, демотиваторы и просто сгенерированные сообщения.')

@bot.on.message(command='пинг')
async def ping(message: Message):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        await message.reply(ping_msg)
        await update_stats(message)

@bot.on.chat_message(command='помощь')
async def help(message: Message):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        await message.reply(func_info)
        await update_stats(message)

@bot.on.message(command='сисинфо')
async def sys_info(message: Message):
    if await check_bl_wl(message) != False:
        bot_info = f'{bot_name} Server Info:\n\n{bot_ver_title} {bot_ver}\n{platform_title} {platform.system()} {platform.release()}\n{python_ver_title} {version}\n{cpu_use_title} {psutil.cpu_percent()}% {cpu_name}) ({psutil.cpu_count(logical=False)} {cores_title}, {psutil.cpu_count(logical=True)} {threads_title})\n{ram_use_title} {psutil.virtual_memory()[2]}% ({total_ram_title} {psutil._common.bytes2human(psutil.virtual_memory().total)})\n{uptime_title} {datetime.timedelta(seconds=int(time.time() - start_time))}\n{modules_title} {len(modules)}'
        await message.reply(bot_info)
        await update_stats(message)

@bot.on.message(command='донат')
async def donate(message: Message):
    if await check_bl_wl(message) != False:
        await addtobd(message.peer_id)
        await message.reply(donate_msg)
        await update_stats(message)
