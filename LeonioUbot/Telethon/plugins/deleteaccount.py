# Copyright (C) 2020 @SnayGFX
#
from telethon import functions, types
from Telethon.events import message

@message(outgoing=True, pattern="^[.]delacc$")
async def testCommand(e):
  await e.edit("""Delete 
⊂_ヽ
  ＼＼ your
   ＼( ͡° ͜ʖ ͡°)
    > ⌒ヽ
   /   へ＼
   /  / ＼＼account
   ﾚ ノ   ヽ_つ
  / /""")