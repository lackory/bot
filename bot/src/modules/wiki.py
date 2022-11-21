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
import wikipedia

# Locals
wikipedia_error_msg = 'В энциклопедии нет информации об этом'
wikipedia_url_to_page_msg = 'Ссылка на полную статью:'

async def get_wiki(find_text):
    try:
        wikipedia.set_lang('ru')
        ny = wikipedia.page(find_text)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return(wikitext2 + f'\n{wikipedia_url_to_page_msg} {wikipedia.page(find_text).url}')
    except Exception as e:
        return wikipedia_error_msg

@bot.on.message(text='/вики <find_text>')    
async def search_in_wikipedia(message: Message, find_text):
    if await check_bl_wl(message) != False:
        article_text = await get_wiki(find_text)
        await message.reply(article_text)
