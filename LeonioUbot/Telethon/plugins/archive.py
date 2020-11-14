from Telethon.events import message

@message(outgoing=True, pattern="^[.]archive$")
async def archiveChat(e):
    for d in await e.client.get_dialogs(limit=None, ignore_migrated=True):
        if d.entity.id == e.chat_id:
            if d.archived:
                await e.edit("❌❌Chat Già Archiviata!❌❌")
            else:
                await d.archive()
                await e.edit("✅✅Chat Archiviata Correttamente!✅✅")
            break
        
    

@message(outgoing=True, pattern="^[.]unarchive$")
async def unarchiveChat(e):
    for d in await e.client.get_dialogs(limit=None, ignore_migrated=True):
        if d.entity.id == e.chat_id:
            if d.archived:
                await d.archive(folder=0)
                await e.edit("✅✅Chat Unarchiviata Correttamente!✅✅")
            else:
                await e.edit("❌❌Chat Non Archiviata!❌❌")
            break