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

@bot.on.message(command='ебатьшакала')
async def create_shakal_img(message: Message):
   await addtobd(message.peer_id)
   if await check_bl_wl(message) != False:
       if message.attachments and message.attachments[0].photo:
        file_id = time.time()
        randomint = random.randint(1000, 10000000)
        photo = message.attachments[0].photo.sizes[-1].url
        p = requests.get(photo)
        out = open(fr'img_{message.peer_id}_{file_id}.jpg', "wb")
        out.write(p.content)
        out.close()
        user_img = PIL.Image.open(f'img_{message.peer_id}_{file_id}.jpg').convert("RGBA")
        (width, height) = user_img.size

        image = Image(filename=f'img_{message.peer_id}_{file_id}.jpg')
        with image.clone() as liquid:
            liquid.liquid_rescale(int(user_img.size[0]*0.5), int(user_img.size[1]*0.5))
            liquid.save(filename=f'result_{message.peer_id}_{file_id}.jpg')
            liquid.size
        user_img = PIL.Image.open(f'result_{message.peer_id}_{file_id}.jpg').resize((width, height))
        user_img.save(f'result_{message.peer_id}_{file_id}.jpg')
        photo = await PhotoMessageUploader(bot.api).upload(f'result_{message.peer_id}_{file_id}.jpg')
        await message.reply(attachment=photo)
        os.remove(f'result_{message.peer_id}_{file_id}.jpg')
        os.remove(f'img_{message.peer_id}_{file_id}.jpg')
        await update_stats(message)
       else:
            await message.reply(nophoto)
