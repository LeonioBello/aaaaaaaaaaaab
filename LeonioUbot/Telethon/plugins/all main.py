"""
DEVELOPED BY @madiodio | ALL RIGHTS ARE RESERVED
"""

import os

import asyncio

import json

from telethon.tl.functions.channels import CreateChannelRequest, CheckUsernameRequest, UpdateUsernameRequest

from telethon.tl.types import InputChannel, InputPeerChannel

from telethon.tl.functions.account import UpdateProfileRequest

from telethon.tl.functions.account import UpdateUsernameRequest as UUpdateUsernameRequest

from telethon import functions, types

from Telethon.events import message


inWait = []
inGrab = False

@message(outgoing=True, pattern="^[.]pula$")
async def CARABINIERIIIIIIIIIII(e):
	for i in range(10):
		await asyncio.wait([e.edit("🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴")])
		await asyncio.sleep(0.1)
		await asyncio.wait([e.edit("🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵")])
		await asyncio.sleep(0.1)
	await asyncio.wait([e.edit("**🚨🚔 CHIAMATE IL CIENTODICIOTTOOOOO!!! 🚔🚨**")])

@message(outgoing=True, pattern="^[.]type ")
async def niceText(e):
	split = e.text.split(" ", 1)
	if split.__len__() >= 2:
		text = split[1]
		mex = ""
		for i in range(len(text)):
			mex = mex + text[i]
			await asyncio.wait([e.edit("`" + mex + " |`")])
			await asyncio.sleep(0.1)
			await asyncio.wait([e.edit("`" + mex + "  ‏‏‎`")])
			await asyncio.sleep(0.1)
			if i == (len(text) - 1):
				await asyncio.wait([e.edit("`" + text + "`")])
			
		
	

@message(outgoing=True, pattern="^[.]type2 ")
async def testoFigo(e):
	Dio = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	Porco = "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩⓿➊➋➌➍➎➏➐➑➒"
	mex = e.text.split(" ", 1)[1]
	for i in range(len(Dio)):
		mex = mex.replace(Dio[i], Porco[i])
	newmex = ""
	for i in range(len(mex)):
		newmex += mex[i]
		await asyncio.wait([e.edit(newmex)])
		await asyncio.sleep(0.2)
	

@message(outgoing=True, pattern="^[.]spam ")
async def spamAIA(e):
	st = e.text.split(" ", 2)
	if st.__len__() == 3:
		if st[1].isnumeric():
			await e.delete()
			await asyncio.wait([e.respond(st[2]) for i in range(int(st[1]))])
		else:
			await e.edit("Numero messaggi da spammare non valido!")
	else:
		await e.edit("Sintassi non valida! ES: .spam 10 Ciao")
	

@message(outgoing=True, pattern="^[.]on$")
async def setNameON(e):
	global CONFIG
	try:
		await bot(UpdateProfileRequest(first_name=CONFIG["Nome-ON"], last_name=""))
		await e.edit("**✅ Nome Impostato Correttamente ✅**")
	except:
		await e.edit("**❌ Impossibile Impostare Il Nome ❌**")
	

@message(outgoing=True, pattern="^[.]off$")
async def setNameOFF(e):
	global CONFIG
	try:
		await bot(UpdateProfileRequest(first_name=CONFIG["Nome-OFF"], last_name=""))
		await e.edit("**✅ Nome Impostato Correttamente ✅**")
	except:
		await e.edit("**❌ Impossibile Impostare Il Nome ❌**")
	

@message(outgoing=True, pattern="^[.]changeusername (.+)")
async def changeUserName(e):
	try:
		await bot(UUpdateUsernameRequest(e.text.split(" ", 1)[1].replace("@", "")))
		await e.edit("**✅ Username Impostato Correttamente ✅**")
	except:
		await e.edit("**❌ Impossibile Impostare l' Username ❌**")
	

@message(outgoing=True, pattern="^[.]changebio (.+)")
async def changeBio(e):
	try:
		await bot(UpdateProfileRequest(about=e.text.split(" ", 1)[1]))
		await e.edit("**✅ Bio Impostata Correttamente ✅**")
	except:
		await e.edit("**❌ Impossibile modificare la bio ❌**")
	

@message(outgoing=True, pattern="^[.]grabusername (.+)")
async def grabUsername(e):
	global inGrab
	await e.edit("__Il processo di grab è stato avviato! Per stopparlo usa .stopgrab__")
	inGrab = True
	createdPrivateChannel = await bot(CreateChannelRequest("BlackList", "BlackList", megagroup=False))
	newChannelID = createdPrivateChannel.__dict__["chats"][0].__dict__["id"]
	newChannelAccessHash = createdPrivateChannel.__dict__["chats"][0].__dict__["access_hash"]
	desiredPublicUsername = e.text.split(" ", 1)[1].replace("@", "")
	while inGrab:
		try:
			checkUsernameResult = await bot(CheckUsernameRequest(InputPeerChannel(channel_id=newChannelID, access_hash=newChannelAccessHash), desiredPublicUsername))
			if checkUsernameResult:
				publicChannel = await bot(UpdateUsernameRequest(InputPeerChannel(channel_id=newChannelID, access_hash=newChannelAccessHash), desiredPublicUsername))
				inGrab = False
				await e.edit("__Grab Riuscito!__")
			else:
				await asyncio.sleep(1)
		except:
			await asyncio.sleep(1)
		
	

@message(outgoing=True, pattern="^[.]stopgrab$")
async def stopGrab(e):
	global inGrab
	if inGrab:
		inGrab = False
		await e.edit("__Grab Stoppato Correttamente__")
	else:
		await e.edit("__Grab non in corso!__")
	
		
	
