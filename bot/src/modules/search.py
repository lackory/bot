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
librex_instance = 'https://search.madreyk.xyz/api.php?q='

import urllib
from json import loads

@bot.on.message(text='/поиск <text>')
async def search(message: Message, text):
    if await check_bl_wl(message) != False:
        results_json = loads(urllib.request.urlopen(f'{librex_instance}{urllib.parse.quote(text)}').read())
        result_text = ''
        for result in results_json:
            if 'special_response' not in result:
                result_text += f'\n\n{result["url"]}\n{result["description"]}'
            else:
                result_text += f'\n\n{result["special_response"]["source"]}{result["special_response"]["response"]}'
        await message.reply(result_text)
        await update_stats(message)
