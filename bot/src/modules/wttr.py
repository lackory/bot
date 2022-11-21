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

import aiohttp

@bot.on.message(text='/погода <city>')
async def wttr_in_full(message: Message, city):
    if await check_bl_wl(message) != False:
        file_id = time.time()
        p = requests.get(f'https://wttr.in/{city}.png')
        out = open(fr'img_{message.peer_id}_{file_id}.jpg', "wb")
        out.write(p.content)
        out.close()
        photo = await PhotoMessageUploader(bot.api).upload(f'img_{message.peer_id}_{file_id}.jpg')
        await message.reply(attachment=photo)
        os.remove(f'img_{message.peer_id}_{file_id}.jpg')
        await update_stats(message)
