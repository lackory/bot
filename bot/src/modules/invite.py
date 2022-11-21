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
hello_msg_chat = '👋 Привет! Я Бот Самогонщик Oxygen,\nбот, который генерирует текст или демотиваторы на основе сообщений вашего чата\nСейчас через 25 сообщений и 3 картинки я делаю демотиваторы. (это можно настроить)\n\nВыдайте мне доступ к переписке или администратора, чтоб я начал свою работу.\nУзнать, что я умею - /help'

@bot.on.chat_message(ChatActionRule("начало"))
async def invited(message: Message) -> None:
    if message.group_id == -message.action.member_id:
        await message.answer(hello_msg_chat)
        await update_stats(message)
