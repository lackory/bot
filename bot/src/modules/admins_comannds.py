
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
import subprocess

# Locals
command_blacklisted = 'Команда которую вы хотели выполнить, была обнаружена в списке нежелательных для выполения! В целях безопасности, у вас пропадает админка, и создателям отправлен отчёт об этом действии.\n\nЕсли это произойшло случайно, создатели вернут вам админку.'
completed = 'Операция выполнена успешно'

@bot.on.message(text='/админ <useridsetadmin>')
async def set_admin(message: Message, useridsetadmin):
    if await check_admin_list(message) != False:
            adml = open('Lists/admins.txt', 'r')
            admll = adml.read()
            adml.close()
            admlt = open('Lists/admins.txt', 'w')
            admlfr = f'{admll}\n{useridsetadmin}'
            admlt.write(admlfr)
            admlt.close()
            await message.reply(completed)

@bot.on.message(text='/пользователь <useriddeladmin>')
async def set_user(message: Message, useriddeladmin):
    if await check_admin_list(message) != False:
        adml = open('Lists/admins.txt', 'r')
        admll = adml.read()
        adml.close()
        admlt = open('Lists/admins.txt', 'w')
        admlfr = admll.replace(useriddeladmin, '')
        admlt.write(admlfr)
        admlt.close()
        await message.reply(completed)

@bot.on.message(text='/бан <ban_id>')
async def ban_user(message: Message, ban_id):
    if await check_admin_list(message) != False:
            adml = open('Lists/blacklist.txt', 'r')
            admll = adml.read()
            adml.close()
            admlt = open('Lists/blacklist.txt', 'w')
            admlfr = f'{admll}\n{ban_id}'
            admlt.write(admlfr)
            admlt.close()
            await message.reply(completed)

@bot.on.message(text='/разбанить <unban_id>')
async def unban_user(message: Message, unban_id):
    if await check_admin_list(message) != False:
        adml = open('Lists/blacklist.txt', 'r')
        admll = adml.read()
        adml.close()
        admlt = open('Lists/blacklist.txt', 'w')
        admlfr = admll.replace(unban_id, '')
        admlt.write(admlfr)
        admlt.close()
        await message.reply(completed)

@bot.on.message(text='/добавитьвбелыйлист <whitelist_id>')
async def write_id(message: Message, whitelist_id):
    if await check_admin_list(message) != False:
            adml = open('Lists/whitelist.txt', 'r')
            admll = adml.read()
            adml.close()
            admlt = open('Lists/whitelist.txt', 'w')
            admlfr = f'{admll}\n{whitelist_id}'
            admlt.write(admlfr)
            admlt.close()
            await message.reply(completed)

@bot.on.message(text='/убратьизбелоголиста <unwrite_id>')
async def unwrite_to_whitelist_id(message: Message, unwrite_id):
    if await check_admin_list(message) != False:
        adml = open('Lists/whitelist.txt', 'r')
        admll = adml.read()
        adml.close()
        admlt = open('Lists/whitelist.txt', 'w')
        admlfr = admll.replace(unwrite_id, '')
        admlt.write(admlfr)
        admlt.close()
        await message.reply(completed)

@bot.on.message(text='/терминал <shell_command>')
async def complete_terminal_command(message: Message, shell_command):
    if await check_admin_list(message) != False:
        user_id = await bot.api.users.get(message.from_id)
        wordCheck = f'{user_id[0].id}'
        commands_blacklist = open('Lists/commands_blacklist.txt', encoding='utf8').read().split('\n')
        if str(shell_command) not in commands_blacklist:
            vmescom = subprocess.getoutput(str(shell_command))
            await message.reply(loadingmsg)
            await message.answer(vmescom)
        else:
            await message.reply(command_blacklisted)
            adml = open('Lists/admins.txt', 'r')
            admll = adml.read()
            adml.close()
            admlt = open('Lists/admins.txt', 'w')
            admlfr = admll.replace(wordCheck, '')
            admlt.write(admlfr)
            admlt.close()

@bot.on.message(text='/спамадмин <msg>')
async def spam_for_admin(message: Message, msg):
    if await check_admin_list(message) != False:
        while True:
            await message.reply(msg)
