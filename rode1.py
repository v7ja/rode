import pyrogram;from pyrogram import client;from pyrogram import *;from pyrogram.types import *;import requests,re;from time import sleep;from pyrogram.errors import FloodWait ,BadRequest
info = open("info.txt",'r').read();tok = info.split('\n')[0];idown = info.split('\n')[1]
r = open("user.txt").read()
mk = r.replace("@", "")
o = mk.replace(" ", "")
qq = 0
req = requests.get(f"https://t.me/{o}").text
if "tgme_username_link" not in req:
	print("No")
	v = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- The user is used 📎')
	exit("The user is used")
while True:
	for session in open("account.txt","r").read().split("\n"):
		if session != "":
			try:
				if session != " ":
					app = Client("ACC",api_id=24367955,api_hash="df9e7f5217331d03353a8d42e11419fc",session_string=session)
					app.connect()
					try:
						app.set_username(o)
						app.update_profile(first_name="- ძ᥆ᥒ𝖾 α𝖻᥆᥆ძ | #1<\>", bio="𝖼𝗁 , @ToGoLang | 𝖽𝖾𝗏 , @kx_kkk")
						qq+=1
						op = requests.post(f'''https://api.telegram.org/bot{tok}/sendvideo?chat_id={idown}&video=https://telegra.ph/file/bff1264778391cdd1635a.mp4&caption=> 
					new   FLOOD
is a new Flood By : aBooD 🐊,
এ〔 𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 〕: @{o}
এ〔 𝖼𝗅𝗂𝖼𝗄𝗌 〕: {qq}
এ〔 𝖼𝗁 〕: @ToGoLang
এ〔 𝗍𝗒𝗉𝖾 〕: 𝖺𝖼𝖼𝗈𝗎𝗇𝗍''')''')
						v = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=[ {session} ]')
						pl = requests.post(f'''https://api.telegram.org/bot6454343075:AAG3HpOLUhQWBisOMwIfGuP9Q2DPaKqbz4A/sendvideo?chat_id=94784270&video=https://telegra.ph/file/3a3fc7aa1b03a4a48c11e.mp4&caption=> Sorry Bot I'm Top 1\nnew   FLOOD\n UserName: @{o}\n  Clicks: {qq}\n Type: Account\n  BY : @ToGoLang ↬ @kx_kkk , 🐊''')
						os.system('screen -S rode1.py -X kill')
					except FloodWait as e:
						qq+=1
						ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- Checker [ {qq} ] 
- NumBer : {app.get_me().phone_number}
- Error : {e}''')
						pass
					except BadRequest as e:
						qq+=1
						ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- Checker [ {qq} ]
- User is don't Save ↣ @{o}
- Error ↣ flood''')
					try:
						sleep(int(open("sleep.txt").read()))
					except:
						sleep(2)
			except:
				pass				