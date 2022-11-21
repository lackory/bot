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
import dog

# Config
randomcat_address = 'https://thiscatdoesnotexist.com/'

@bot.on.message(command='собака')
async def getdog(message: Message):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        file_id = time.time()
        await message.reply(loadingmsg)
        dog.getDog(filename=f'dog_{message.peer_id}_{file_id}')
        dogphoto = await PhotoMessageUploader(bot.api).upload(f'dog_{message.peer_id}_{file_id}.jpg')
        await message.answer(attachment=dogphoto)
        os.remove(f'dog_{message.peer_id}_{file_id}.jpg')
        await update_stats(message)

@bot.on.message(command='кот')
async def getcat(message: Message):
    if await check_bl_wl(message) != False:
        file_id = time.time()
        await message.reply(loadingmsg)
        img = requests.get(randomcat_address)
        img_option = open(f'cat_{message.peer_id}_{file_id}.jpg', 'wb')
        img_option.write(img.content)
        img_option.close()
        cat = await PhotoMessageUploader(bot.api).upload(f'cat_{message.peer_id}_{file_id}.jpg')
        await message.answer(attachment=cat)
        os.remove(f'cat_{message.peer_id}_{file_id}.jpg')
        await update_stats(message)
