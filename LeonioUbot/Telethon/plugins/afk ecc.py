import os, asyncio, json
from telethon import functions, types
from Telethon.events import message
from gtts import gTTS

inWait = []

if os.path.exists("saves.json"):
	with open("saves.json", "r+") as f:
		SAVES = json.load(f)
else:
	SAVES = {"AFKMode": False, "Approved": [], "mutedList": [], "AFK-Mex": "Puoi personalizzare il seguente messaggio con .msgafk", "Block-Mex": "Puoi customizzare il seguente messaggio con .msgblock"}
	with open("saves.json", "w+") as f:
		json.dump(SAVES, f)


async def save():
	global SAVES
	with open("saves.json", "w+") as f:
		json.dump(SAVES, f)


@message(outgoing=True, pattern="^[.]tts")
async def textToSpeech(e):
	st = e.text.split(" ", 1)
	if st.__len__() == 2:
		await e.delete()
		tts = gTTS(text=st[1], lang='it')
		tts.save("audio.ogg")
		await e.client.send_file(e.chat_id, file="audio.ogg", voice_note=True)
		os.remove("audio.ogg")
	else:
		await e.edit("**❌ Specificare il testo ❌**")


@message(outgoing=True, pattern="^[.]msgafk")
async def setAFKMex(e):
	global SAVES
	st = e.text.split(" ", 1)
	if st.__len__() == 2:
		SAVES["AFK-Mex"] = st[1]
		save()
		await e.edit("**✅ Messaggio Impostato Correttamente ✅**")
	else:
		await e.edit("**❌ Specificare il messaggio ❌**")


@message(outgoing=True, pattern="^[.]msgblock")
async def setBlockMex(e):
  global SAVES
  st = e.text.split(" ", 1)
  if st.len() == 2:
    SAVES["Block-Mex"] = st[1]
    save()
    await e.edit("✅ Messaggio Impostato Correttamente ✅")
  else:
    await e.edit("❌ Specificare il messaggio ❌")




@message(outgoing=True, pattern="^[.]block$")
async def BlockUser(e):
  global SAVES
  if e.is_reply:
    try:
      await e.client(functions.contacts.BlockRequest((await (await e.get_reply_message()).get_sender()).id))
      await e.edit(SAVES["Block-Mex"])
    except:
      await e.edit("❌ Impossibile bloccare questo utente ❌")
  elif e.is_private:
    try:
      await e.client(functions.contacts.BlockRequest(e.chat_id))
      await e.edit(SAVES["Block-Mex"])
    except:
      await e.edit("❌ Impossibile bloccare questo utente ❌")
  else:
    await e.edit("❌ Puoi usare questo comando solo rispondendo al messaggio di un utente o scrivendolo in privato ad un utente ❌")


@message(outgoing=True, pattern="^[.]afk$")
async def setAFK(e):
	global SAVES
	if SAVES["AFKMode"]:
		SAVES["AFKMode"] = False
		save()
		await e.edit("**❌ AFK Mode Disattivata ❌**")
	else:
		SAVES["AFKMode"] = True
		save()
		await e.edit("**✅ AFK Mode Attivata ✅**")


@message(outgoing=True, pattern="^[.]approve$")
async def approveUser(e):
	global SAVES
	if e.chat_id in SAVES["Approved"]:
		await e.edit("**❌ Quest utente è già approvato ❌**")
	else:
		SAVES["Approved"].append(e.chat_id)
		save()
		await e.edit("**✅ Utente Approvato ✅**")


@message(outgoing=True, pattern="^[.]disapprove$")
async def disapproveUser(e):
	global SAVES
	if e.chat_id in SAVES["Approved"]:
		SAVES["Approved"].remove(e.chat_id)
		save()
		await e.edit("**❌ Utente Disapprovato ❌**")
	else:
		await e.edit("**❌ Quest utente non è approvato ❌**")


@message(incoming=True)
async def doAFK(e):
	global SAVES, inWait
	if SAVES["AFKMode"] and e.is_private and not (await e.get_sender()).bot and not e.chat_id in SAVES["Approved"]:
		await e.delete()
		if not e.chat_id in inWait:
			inWait.append(e.chat_id)
			if e.text == None or e.text == "":
				mex = "__MEDIA__"
			else:
				mex = e.text
			await e.respond(SAVES["AFK-Mex"].replace("{msg}", mex))
			await asyncio.sleep(30)
			inWait.remove(e.chat_id)



@message(outgoing=True, pattern="^[.]mute$")
async def setMute(e):
	global SAVES
	if e.is_private and not (await e.get_sender()).bot:
		if e.chat_id in SAVES["mutedList"]:
			SAVES["mutedList"].remove(e.chat_id)
			save()
			await e.edit("**🔈 Utente Smutato 🔈**")
		else:
			SAVES["mutedList"].append(e.chat_id)
			save()
			await e.edit("**🔇 Utente Mutato 🔇**")



@message(incoming=True)
async def muteManager(e):
	global SAVES
	if e.is_private and not (await e.get_sender()).bot and e.chat_id in SAVES["mutedList"]:
		await e.delete()
