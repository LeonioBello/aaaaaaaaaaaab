# Copyright (C) 2020 @SnayGFX
#
from telethon import functions, types
from Telethon.events import message

@message(outgoing=True, pattern="^[.]a$")
async def testCommand(e):
  await e.edit("ᵃ")