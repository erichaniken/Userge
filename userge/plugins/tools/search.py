# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.


from userge import userge, Message


@userge.on_cmd("s", about={
    'header': "search commands in USERGE",
    'examples': ".s wel"})
async def search(message: Message):
    cmd = message.input_str

    if not cmd:
        await message.err(text="Enter any keyword to search in commands")
        return

    found = [i for i in userge.get_help(all_cmds=True)[0] if cmd in i]
    out_str = '    '.join(found)

    if found:
        out = f"**--I found ({len(found)}) commands for-- : `{cmd}`**\n\n`{out_str}`"

    else:
        out = f"__command not found for__ : `{cmd}`"

    await message.edit(text=out, del_in=0)
