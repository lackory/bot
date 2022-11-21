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
man_not_found = 'Мануал не найден.'

import os

if not os.path.exists(f'{config.modules_dir}/man/'):
    os.mkdir(f'{config.modules_dir}/man/')

@bot.on.message(text='/мануал <man_text>')
async def get_manual(message: Message, man_text):
    if await check_bl_wl(message) != False:
        if not os.path.exists(f'{config.modules_dir}/man/{man_text}') or '..' in message.text:
            await message.reply(man_not_found)
        if os.path.exists(f'{config.modules_dir}/man/{man_text}') and '..' not in message.text:
            await message.reply(open(f'{config.modules_dir}/man/{man_text}').read())
        await update_stats(message)

@bot.on.message(command='листатьмануал')
async def get_manuals_list(message: Message):
    if await check_bl_wl(message) != False:
        man_list = ''
        for man in os.listdir(f'{config.modules_dir}/man/'):
            man_list += f'- {man}\n'
        await message.reply(f'{man_list}\n\n/man [man_name]')
        await update_stats(message)
