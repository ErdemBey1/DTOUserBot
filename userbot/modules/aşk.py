# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#


from userbot.events import register

@register(outgoing=True, pattern="^.ask (.*)")
async def ask (event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.edit("️╔══╗╔╗ ♡ ♡ ♡\n╚╗╔╝║║╔═╦╦╦╔╗\n╔╝╚╗║╚╣║║║║╔╣\n╚══╝╚═╩═╩═╩═╝\n♡" + input_str +"♡\n𝓢𝓔𝓝𝓘 𝓢𝓔𝓥𝓘𝓨𝓞𝓡𝓤𝓜")
