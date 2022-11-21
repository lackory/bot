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
news_in_vk_text = 'Новости во ВКонтакте'
news_msg = '📢 Новости нашего бота доступны по ссылке: vk.com/botsamogon\n'

# Config
news_btn_menu = Keyboard(inline=True)
news_btn_menu.add(OpenLink(f'https://vk.com/{group_shortname}', news_in_vk_text))
nyaddress = 'https://calendar.yoip.ru/calc/days-to-new-year/'
holiday_address = 'https://www.calend.ru/img/export/informer.png'

@bot.on.message(command='новости')
async def getnews(message: Message):
    if await check_bl_wl(message) != False:
        await message.reply('Вам куда?', keyboard=news_btn_menu)
        await update_stats(message)

@bot.on.message(command='праздники')
async def getholidays(message: Message):
    if await check_bl_wl(message) != False:
        file_id = time.time()
        await message.reply(loadingmsg)
        img = requests.get(holiday_address)
        img_option = open(f'calendru_{message.peer_id}_{file_id}.jpg', 'wb')
        img_option.write(img.content)
        img_option.close()
        cat = await PhotoMessageUploader(bot.api).upload(f'calendru_{message.peer_id}_{file_id}.jpg')
        await message.reply(attachment=cat)
        os.remove(f'calendru_{message.peer_id}_{file_id}.jpg')
        await update_stats(message)

@bot.on.message(command='доновогогода')
async def newyear(message: Message):
    if await check_bl_wl(message) != False:
        now = datetime.datetime.today()
        NY = datetime.datetime(2023, 1, 1)
        d = NY-now
        mm, ss = divmod(d.seconds, 60)
        hh, mm = divmod(mm, 60)
        await message.reply(f'До нового года осталость: {d.days} дней {hh} часа {mm} мин {ss} сек по МСК.')
        await update_stats(message)
