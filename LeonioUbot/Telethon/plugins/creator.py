
from telethon import functions, types
from Telethon.events import message

@message(outgoing=True, pattern="^[.]creator$")
async def testCommand(e):
  await e.edit("Questo Userbot è stato creato da <a href='t.me/LeonioOfficialVoip'><b>geme</b></a>", parse_mode="html")
