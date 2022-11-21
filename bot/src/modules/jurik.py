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

@bot.on.message(text='/жирик <txt>')
async def jurik(message: Message, txt):
    file_id = time.time()
    with open(f'{config.modules_dir}/zhirinovsky/zhirinovsky.jpeg', 'rb') as f:
        blob_flie = f.read()
        txt = re.sub('^(ЕСТЬ ИДЕЯ|МБ|МОЖЕТ БЫТЬ|ПРЕДЛАГАЮ|А МОЖЕТ|МОЖЕТ|ДАВАЙТЕ|ДАВАЙ) ', '', txt, flags=re.IGNORECASE)
        with Image(blob=blob_flie) as img:
            with Image(width=560, height=360) as img2:
                img2.options['pango:wrap'] = 'word-char'
                img2.options['pango:single-paragraph'] = 'false'
                img2.font = Font('OswaldRegular')
                img2.font_color = '#000000'
                img2.font_size = 44
                img2.pseudo(560, 360, pseudo=f'pango:{txt}')
                img.composite(image=img2, left=50, top=630)
            img.merge_layers('flatten')
            img.format = 'jpeg'
            with img.clone() as liquid:
                liquid.save(filename=f'{config.modules_dir}/zhirinovsky/jurik_{message.peer_id}_{file_id}.jpg')
        mettionsphoto = await PhotoMessageUploader(bot.api).upload(f'{config.modules_dir}/zhirinovsky/jurik_{message.peer_id}_{file_id}.jpg')
        await message.reply(attachment=mettionsphoto)
        os.remove(f'{config.modules_dir}/zhirinovsky/jurik_{message.peer_id}_{file_id}.jpg')
        await update_stats(message)
