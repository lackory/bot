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
mininal_messages_to_gen = 'Недостаточно сообщений/изображений для генерации.\nНужное количество: 5 сообщений и 1 фотография'
mininal_messages_to_genp = 'Недостаточно сообщений для генерации.\nНужное количество: 5 сообщений'

@bot.on.chat_message(command='ген')
async def gen(message: Message):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        file_id = time.time()
        q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
        result = q.fetchall()
        status = result[0][1]
        connection.commit()
        if status == 0:
            pic2 = 0
            with open(f'{dir_to_pic}{message.peer_id}.txt', encoding='utf8') as f:
                for line in f:
                    pic2 = pic2 + 1
            lines = 0
            with open(f'{dir_to_txt}{message.peer_id}.txt', encoding='utf8') as f:
                for line in f:
                    lines = lines + 1
            if lines >= 5 and pic2 >= 1:
                with open(f'{dir_to_txt}{message.peer_id}.txt', encoding='utf8') as file:
                    content = file.read().splitlines()
                q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
                result = q.fetchall()
                kolvo = result[0][2]
                mode = result[0][5]
                arrange = result[0][8]
                q.execute(f"UPDATE players SET kolvo = '0' WHERE id = '{message.peer_id}'")
                connection.commit()
                generator = mc.PhraseGenerator(samples=content)
                rndtxt = generator.generate_phrase(attempts=20, validators=[validators.words_count(minimal=1, maximal=5)])
                rndtxt2 = generator.generate_phrase(attempts=20, validators=[validators.words_count(minimal=1, maximal=10)])
                with open(f'{dir_to_pic}{message.peer_id}.txt', encoding='utf8') as file:
                    content2 = file.read().splitlines()
                rndpic = random.choice(content2)
                p = requests.get(rndpic)
                out = open(fr'randomimg_{message.peer_id}_{file_id}.jpg', "wb")
                out.write(p.content)
                out.close()
                if mode == 1:
                        user_img = PIL.Image.open(f'randomimg_{message.peer_id}_{file_id}.jpg').convert("RGBA")
                        (width, height) = user_img.size
                        image = Image(filename=f'randomimg_{message.peer_id}_{file_id}.jpg')
                        with image.clone() as liquid:
                            liquid.liquid_rescale(int(width*0.5), int(height*0.5))
                            liquid.save(filename=f'randomimg_{message.peer_id}_{file_id}.jpg')
                            liquid.size
                        user_img = PIL.Image.open(f'randomimg_{message.peer_id}_{file_id}.jpg').resize((width, height))
                        user_img.save(f'randomimg_{message.peer_id}_{file_id}.jpg')
                if arrange == 1:
                    dem = Demotivator(rndtxt, rndtxt2)
                    dem.create(f'randomimg_{message.peer_id}_{file_id}.jpg', arrange=True, result_filename=f'dem_{message.peer_id}_{file_id}.jpg')
                else:
                    dem = Demotivator(rndtxt, rndtxt2)
                    dem.create(f'randomimg_{message.peer_id}_{file_id}.jpg', watermark=watermarkwrong, result_filename=f'dem_{message.peer_id}_{file_id}.jpg')
                photo = await PhotoMessageUploader(bot.api).upload(f'dem_{message.peer_id}_{file_id}.jpg')
                await message.reply(attachment=photo)
                os.remove(f'randomimg_{message.peer_id}_{file_id}.jpg')
                os.remove(f'dem_{message.peer_id}_{file_id}.jpg')

            else:
                await message.reply(mininal_messages_to_gen)
        else:
            lines = 0
            with open(f'{dir_to_txt}{message.peer_id}.txt', encoding='utf8') as f:
                for line in f:
                    lines = lines + 1
            if lines >= 5:
                with open(f'{dir_to_txt}{message.peer_id}.txt', encoding='utf8') as file:
                    content = file.read().splitlines()
                q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
                result = q.fetchall()
                kolvo = result[0][2]
                q.execute(f"UPDATE players SET kolvo = '0' WHERE id = '{message.peer_id}'")
                connection.commit()
                generator = mc.PhraseGenerator(samples=content)
                rndtxt = generator.generate_phrase(attempts=20, validators=[validators.words_count(minimal=1, maximal=5)])
                rndtxt2 = generator.generate_phrase(attempts=20, validators=[validators.words_count(minimal=1, maximal=10)])
                long2 = len(rndtxt2)
                if long2 <= 60:
                    await message.answer(f'{rndtxt} {rndtxt2}')
                else:
                    rndtxt2 = rndtxt2[:60]
                    await message.answer(f'{rndtxt} {rndtxt2}')
            else:
                await message.reply(mininal_messages_to_genp)
    await update_stats(message)
