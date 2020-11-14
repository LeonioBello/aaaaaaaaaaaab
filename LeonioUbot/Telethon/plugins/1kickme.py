from Telethon.events import message
from telethon import functions

@message(outgoing=True, pattern="^[.]kickme$")
async def kickMe(e):
  if e.is_private:
    await e.edit("❌❌Questo comando puoi farlo solo nei gruppi e nei canali❌❌!")
  else:
    await e.edit("AutoKickato con successo✔️,hai smesso di dare fastidio a sto gruppo")
    await e.client(functions.channels.LeaveChannelRequest(e.chat_id))
