async def update_stats(message):
    await addtobd(message.from_id)
    await addtobd(message.peer_id)    
    user = await bot.api.users.get(message.from_id)
    q.execute(f"SELECT * FROM players WHERE id = {message.peer_id}")
    result = q.fetchall() 
    gen_msgs = result[0][9] 
    if message.peer_id != message.from_id:
        q.execute(f"UPDATE players SET gen_msgs = '{gen_msgs + 1}' WHERE id = '{message.peer_id}'")
        new_num = gen_msgs + 1
        if int(new_num) in config.levels:
            await message.reply(f'Теперь ваш чат на уровне {config.levels.index(new_num) + 1} - {config.level_names[config.levels.index(new_num)]}!')        
    q.execute(f"SELECT * FROM players WHERE id = {message.from_id}")
    user_gen_msgs = q.fetchall()[0][9]        
    q.execute(f"UPDATE players SET gen_msgs = '{user_gen_msgs + 1}' WHERE id = '{message.from_id}'")
    new_num = user_gen_msgs + 1
    if int(new_num) in config.levels:
        new_lvl = config.levels.index(int(new_num)) + 1
        new_lvl_name = config.level_names[new_lvl - 1]
        await message.reply(f'Поздравляем, [id{message.from_id}|{user[0].first_name}]! Теперь вы на уровне {new_lvl} - {new_lvl_name}')
    connection.commit()   


async def addtobd(peerid):
    q.execute(f"SELECT * FROM players WHERE id = {peerid}")
    result = q.fetchall()
    if len(result) == 0:
            q.execute(f"INSERT INTO players (id, status)"
                        f"VALUES ('{peerid}', '{0}')")
    connection.commit()
    if not os.path.exists(f'{dir_to_txt}{peerid}.txt'):
        f = open(f'{dir_to_txt}{peerid}.txt', 'w', encoding='utf8')
        f.write('')
        f.close()
    if not os.path.exists(f'{dir_to_pic}{peerid}.txt'):
        f = open(f'{dir_to_pic}{peerid}.txt', 'w', encoding='utf8')
        f.write('')
        f.close() 

async def check(message, id: int) -> bool:
    items = (await bot.api.messages.get_conversations_by_id(peer_ids=message.peer_id)).items
    if not items:
        return False
    chat_settings = items[0].chat_settings
    admins = []
    admins.extend(chat_settings.admin_ids)
    admins.append(chat_settings.owner_id)
    return id in admins

async def check_bl_wl(message): 
    if config.blacklist == 1:
        blacklist = open(f'{lists_dir}blacklist.txt', encoding='utf8').read().split('\n')
        whitelist = ['']
        not_allowed_msg = blacklisted_msg 
    else:
        whitelist = open(f'{lists_dir}whitelist.txt', encoding='utf8').read().split('\n')
        blacklist = ['']
        not_allowed_msg = not_whitelisted_msg  
    if config.blacklist == 0 and str(message.from_id) in whitelist and str(message.from_id) in whitelist or config.blacklist == 1 and str(message.peer_id) not in blacklist and str(message.from_id) not in blacklist:
        return True
    else:
        await message.reply(not_allowed_msg, keyboard=contact_with_admin)
        return False
        
async def check_admin_list(message):
    user_id = await bot.api.users.get(message.from_id)
    adminlist = open(f'{lists_dir}admins.txt', encoding='utf8').read().split('\n')
    if config.admin_funcs == 1 and str(message.from_id) in adminlist:
        return True
    else:
        await message.reply(not_allowed_admin_command)
        return False