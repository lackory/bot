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
from bs4 import BeautifulSoup

# Configs
quotes_address = 'http://ibash.org.ru/random.php'
jokes_address = 'https://www.anekdot.ru/random/anekdot/'

# Locals
fadvice_msg = 'совет: '

@bot.on.message(command='цитата')
async def get_quote(message: Message):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        quotes_response = get(quotes_address)
        quote = BeautifulSoup(quotes_response.text, 'lxml').find('div', class_='quotbody').text
        await message.reply(quote)
        await update_stats(message)

@bot.on.message(command='глупаяшутка')
async def get_stupidjoke(message: Message):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        jokes_response = get(jokes_address)
        joke = BeautifulSoup(jokes_response.text, 'lxml').find('div', class_='text').text
        await message.reply(joke)
        await update_stats(message)

@bot.on.message(command='совет')
async def get_advice(message: Message):
    await addtobd(message.peer_id)
    if await check_bl_wl(message) != False:
        info = requests.get("http://fucking-great-advice.ru/api/random")
        advice = (json.loads(info.content)["text"])
        await message.reply(f'{fadvice_msg}<<{advice}>>')
        await update_stats(message)
