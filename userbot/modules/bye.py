# @DTOUserBot
from telethon import events

import asyncio

from userbot.events import register

@register(outgoing=True, pattern="^.bye")

async def bye(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 11)

    await event.edit("Mən gedirəm ❤️")

    animation_chars = [
            "❤️=🙋🏻‍♀️====❤️",
            "❤️==🙋🏻‍♂️===❤️",
            "❤️===🙋🏻‍♀️==❤️",
            "❤️====🙋🏻‍♂️=❤️",
            "❤️=====🙋🏻‍♀️❤️",    
            "❤️====🙋🏻‍♂️=❤️",
            "❤️===🙋🏻‍♀️==❤️",
            "❤️==🙋🏻‍♂️===❤️",
            "❤️=🙋🏻‍♀️====❤️",
            "❤️🙋🏻‍♂️=====❤️",
            "`Bye Bye ❤️`", 
			]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])
