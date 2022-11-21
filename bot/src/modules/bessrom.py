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

# Configs 
bessrom_words = ['bess', 'rom', 'for', 'pabji', 'batteri', 'af', 'smooth', 'kernal', 'gamin', 'twrp', 'oranjfoks', 'ximi', 'sapdagon', 'miatool', 'mido', 'begonia', 'lavander', 'tissot', 'turbo', 'alo', 'vayu', 'surya', 'bocq', 'x', 'pru', 'iphun', '720g', '855', '860', '625', '660', '5s', 'se', '14', '3', '7', 'max', 'perfomance', 'nusuntara', 'linagOS', 'evox', 'pixzal experzence', 'aosp', 'muiu', 'posp', 'crdoid', 'havok', 'plus', 'derpfez', 'radml', 'wen']

@bot.on.message(command='bessrom')
async def bessrom(message: Message):
    if await check_bl_wl(message) != False:
        generated_bessrom = ''
        for i in range(random.randint(4, 7)):
            generated_bessrom += mc.PhraseGenerator(samples=bessrom_words).generate_phrase() + ' '
        await message.reply(generated_bessrom)
        await update_stats(message)