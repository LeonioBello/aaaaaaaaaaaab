# Copyright (C) 2020 @SnayGFX
#
from telethon import functions, types
from Telethon.events import message

@message(outgoing=True, pattern="^[.]face$")
async def testCommand(e):
  await e.edit("""🟫🟫🟫🟫🟫🟫🟫🟫
🟫🟫🟫🟫🟫🟫🟫🟫
🟫🟧🟧🟧🟧🟧🟧🟫
🟧🟧🟧🟧🟧🟧🟧🟧
🟧⬜️🟦🟧🟧🟦⬜️🟧
🟧🟧🟧🟫🟫🟧🟧🟧
🟧🟧🟫🟧🟧🟫🟧🟧
🟧🟧🟫🟫🟫🟫🟧🟧""")