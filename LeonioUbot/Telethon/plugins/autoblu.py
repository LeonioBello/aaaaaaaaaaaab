"""
Available Commands:
.autou"""

from telethon import events

import asyncio





@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "autoblu":

        await event.edit(input_str)

        animation_chars = [
            "*auto blu corr.....*",
            "*TORNA IN CANTINA*",
            ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
