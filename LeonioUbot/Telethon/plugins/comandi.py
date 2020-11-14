from telethon import functions, types
from Telethon.events import message

@message(outgoing=True, pattern="^[.]comandi$")
async def comandi(e):
  await e.edit("""Lista comandi LeonioUserbot
 ——————————————-
 .help - cmd - comandi  - mostra i comandi dell'userbot
 .a mette in automatico un a piccola
 .lol
 .muro
 .gmex
 .pula
 .reply
 .type [msg]
 .voip
 .clock
 .moon
 .info
 .supreme scritta supreme
 .face
 .ok
 .stats
 .f
 .gay
 .deleteaccount
 .lmao
 .pornhub
 .addsticker
  magari ne metterò altri :D """)
