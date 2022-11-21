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

# Imports
import time
import os
from gtts import gTTS

if not os.path.exists(f'{config.modules_dir}/ttsdata/'):
    os.mkdir(f'{config.modules_dir}/ttsdata/')

@bot.on.message(text='/сказатьтекст <saytext>')
async def say(message: Message, saytext):
    if await check_bl_wl(message) != False:
        voice_msg_id = f'{message.peer_id}_{message.from_id}_{time.time()}'
        text_message = gTTS(saytext, lang='ru')
        text_message.save(f'{config.modules_dir}/ttsdata/voice_msg_{voice_msg_id}.mp3')
        with open(f'{config.modules_dir}/ttsdata/voice_msg_{voice_msg_id}.mp3', 'rb') as f:
            voice_message = f.read()
        audio_message = await VoiceMessageUploader(bot.api).upload(f'{config.modules_dir}/ttsdata/voice_msg_{voice_msg_id}.mp3', f'{config.modules_dir}/ttsdata/voice_msg_{voice_msg_id}.mp3', peer_id=message.peer_id)
        await message.reply(attachment=audio_message)
        os.remove(f'{config.modules_dir}/ttsdata/voice_msg_{voice_msg_id}.mp3')
