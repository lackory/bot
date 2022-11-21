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
correct_use_dem = 'Правильное использование: /дем <txt1>//<txt2>'

@bot.on.message(text='/дем <txt1>//<txt2>')
async def dem2(message: Message, txt1, txt2):
    await addtobd(message.peer_id)
    if message.attachments and message.attachments[0].photo:
        file_id = time.time()
        photo = message.attachments[0].photo.sizes[-1].url
        p = requests.get(photo)
        out = open(fr'randomimg_{message.peer_id}_{file_id}.jpg', "wb")
        out.write(p.content)
        out.close()
        if len(txt2) >= 60:
            txt2 = txt2[:60]
        if len(txt1) >= 40:
            txt1 = txt1[:40]
        dem = Demotivator(txt1, txt2)
        dem.create(f'randomimg_{message.peer_id}_{file_id}.jpg', watermark=watermarkwrong, result_filename=f'dem_{message.peer_id}_{file_id}.jpg')
        photo = await PhotoMessageUploader(bot.api).upload(f'dem_{message.peer_id}_{file_id}.jpg')
        await message.reply(attachment=photo)
        os.remove(f'randomimg_{message.peer_id}_{file_id}.jpg')
        os.remove(f'dem_{message.peer_id}_{file_id}.jpg')
        await update_stats(message)
    else:
        await message.reply(nophoto)

@bot.on.message(text='/дем <txt1>')
async def dem1(message: Message, txt1):
    await addtobd(message.peer_id)
    if message.attachments and message.attachments[0].photo:
        file_id = time.time()
        photo = message.attachments[0].photo.sizes[-1].url
        p = requests.get(photo)
        out = open(f'randomimg_{message.peer_id}_{file_id}.jpg', "wb")
        out.write(p.content)
        out.close()
        if len(txt1) >= 40:
            txt1 = txt1[:40]
        dem = Demotivator(txt1, '')
        dem.create(f'randomimg_{message.peer_id}_{file_id}.jpg', watermark=watermarkwrong, result_filename=f'dem_{message.peer_id}_{file_id}.jpg')
        photo = await PhotoMessageUploader(bot.api).upload(f'dem_{message.peer_id}_{file_id}.jpg')
        await message.reply(attachment=photo)
        os.remove(f'randomimg_{message.peer_id}_{file_id}.jpg')
        os.remove(f'dem_{message.peer_id}_{file_id}.jpg')
        await update_stats(message)
    else:
        await message.reply(nophoto)

@bot.on.message(text='/дем')
async def dem_correct_use_arg(message: Message):
    await message.reply(correct_use_dem)
