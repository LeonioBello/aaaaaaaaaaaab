
from telethon import functions, types
from Telethon.events import message

@message(outgoing=True, pattern="^[.]cat$")
async def testCommand(e):
  await e.edit("""──────▄▀▄─────▄▀▄
─────▄█░░▀▀▀▀▀░░█▄
─▄▄──█░░░░░░░░░░░█──▄▄
█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█""")
