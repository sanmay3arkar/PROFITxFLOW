from telegram import Bot
from iqoptionapi.stable_api import IQ_Option as iq
from snr import audcad, audusd, eurgbp, eurjpy, eurusd, gbpusd, gbpjpy, nzdusd, usdchf, usdjpy
from threading import Thread
from additional.lists import lst, names
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import time
import datetime
import copy

cred = credentials.Certificate("profitxflow-39f9f-firebase-adminsdk-z9yva-296f8909b2.json")
firebase_admin.initialize_app(cred,
{
	'databaseURL' : "https://profitxflow-39f9f-default-rtdb.firebaseio.com"
})

option = iq("sanmaysarkar500@gmail.com", "Sanmay1239")

option.connect()
print("Connected")

vu = db.reference("VIPUser")
musr = vu.get()

bot = Bot("5813740213:AAErjpHMb6pwmKOeBGc7NO0T0HvSy0S58EE")

df1 = {"AUDCAD" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "AUDUSD" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "EURGBP" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "EURJPY" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "EURUSD" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "GBPUSD" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "GBPJPY" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "NZDUSD" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "USDCHF" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "USDJPY" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}}

df2 = {"AUDCAD" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "AUDUSD" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "EURGBP" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "EURJPY" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "EURUSD" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "GBPUSD" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "GBPJPY" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "NZDUSD" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "USDCHF" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}, "USDJPY" : {"open" : "", "close" : "", "tim" : "", "direc" : ""}}

def sgnl(pts, opt, ipv, nm, ddf1,ddf2, tm):	
	cndl = opt.get_candles(nm, 300, 2, time.time())
	pt = 0
	for i in pts:
		if (cndl[0]["close"] <= i + ipv) and (cndl[0]["close"] >= i - ipv):
			pt = i
	data = int
	if pt != 0:
		if cndl[0]["open"] > pt + ipv:
			data = 0
		elif cndl[0]["open"] < pt - ipv:
			data = 1
	
	ddf2[nm]["close"] = cndl[0]["close"]
	if data == 0:
		ddf1[nm]["open"] = cndl[1]["open"]
		ddf1[nm]["direc"] = "BUY"
		if len(str(tm.minute)) == 1:
			ddf1[nm]["tim"] = "{}:0{}".format(tm.hour, tm.minute)
		else:
			ddf1[nm]["tim"] = "{}:{}".format(tm.hour, tm.minute)
			
		for i in musr.keys():
			if nm in musr[i]["Markets"]:
				try:
					bot.send_photo(chat_id = int(i), photo = lst[nm], caption = "<b>{}\n\n🔹Signal : BUY/CALL⭕️\n\n🔹Duration : 5 Minutes\n\n⚠️Note : </b><i>All signals are based on market price action and given by a professional AI with a 70% accuracy, so before using this signal make sure to use your own analysis as well</i>".format(names[nm]), parse_mode = "html")
				except:
					pass
	elif data == 1:
		ddf1[nm]["open"] = cndl[1]["open"]
		ddf1[nm]["direc"] = "SELL"
		if len(str(tm.minute)) == 1:
			ddf1[nm]["tim"] = "{}:0{}".format(tm.hour, tm.minute)
		else:
			ddf1[nm]["tim"] = "{}:{}".format(tm.hour, tm.minute)
		
		for i in musr.keys():
			if nm in musr[i]["Markets"]:
				try:
					bot.send_photo(chat_id = int(i), photo = lst[nm], caption = "<b>{}\n\n🔹Signal : SELL/PUT⭕️\n\n🔹Duration : 5 Minutes\n\n⚠️Note : </b><i>All signals are based on market price action and given by a professional AI with a 70% accuracy, so before using this signal make sure to use your own analysis as well and make sure to use proper money management</i>".format(names[nm]), parse_mode = "html")
				except:
					pass
	else:
		ddf1[nm]["direc"] = "N"


count = 0
count1 = 0
pts = audcad(option, time)
pts1 = audusd(option, time)
pts2 = eurgbp(option, time)
pts3 = eurjpy(option, time)
pts4 = eurusd(option, time)
pts5 = gbpusd(option, time)
pts6 = gbpjpy(option, time)
pts7 = nzdusd(option, time)
pts8 = usdchf(option, time)
pts9 = usdjpy(option, time)

while True:
	if count == 24:
		pts = audcad(option, time)
		pts1 = audusd(option, time)
		pts2 = eurgbp(option, time)
		pts3 = eurjpy(option, time)
		pts4 = eurusd(option, time)
		pts5 = gbpusd(option, time)
		pts6 = gbpjpy(option, time)
		pts7 = nzdusd(option, time)
		pts8 = usdchf(option, time)
		pts9 = usdjpy(option, time)
		count = 0
	while True:
		t = datetime.datetime.now().minute
		t = str(t)
		time.sleep(1)
		if len(t) < 2:
			if t == "0":
				break
			elif t == "5":
				break
		else:
			if t[1] == "0":
				break
			elif t[1] == "5":
				break
	tt = datetime.datetime.now()

	t1 = Thread(target=sgnl, args=(pts, option, 0.000080, "AUDCAD", df1, df2, tt))
	t2 = Thread(target=sgnl, args=(pts1, option, 0.000080, "AUDUSD", df1, df2, tt))
	t3 = Thread(target=sgnl, args=(pts2, option, 0.000040, "EURGBP", df1, df2, tt))
	t4 = Thread(target=sgnl, args=(pts3, option, 0.021190, "EURJPY", df1, df2, tt))
	t5 = Thread(target=sgnl, args=(pts4, option, 0.000070, "EURUSD", df1, df2, tt))
	t6 = Thread(target=sgnl, args=(pts5, option, 0.000090, "GBPUSD", df1, df2, tt))
	t7 = Thread(target=sgnl, args=(pts6, option, 0.028342, "GBPJPY", df1, df2, tt))
	t8 = Thread(target=sgnl, args=(pts7, option, 0.000160, "NZDUSD", df1, df2, tt))
	t9 = Thread(target=sgnl, args=(pts8, option, 0.000080, "USDCHF", df1, df2, tt))
	t10 = Thread(target=sgnl, args=(pts9, option, 0.011716, "USDJPY", df1, df2, tt))
	time.sleep(0.2)
	t1.start()
	time.sleep(0.3)
	t2.start()
	time.sleep(0.3)
	t3.start()
	time.sleep(0.3)
	t4.start()
	time.sleep(0.3)
	t5.start()
	time.sleep(0.3)
	t6.start()
	time.sleep(0.3)
	t7.start()
	time.sleep(0.3)
	t8.start()
	time.sleep(0.3)
	t9.start()
	time.sleep(0.3)
	t10.start()
	time.sleep(0.3)
	t1.join()
	t2.join()
	t3.join()
	t4.join()
	t5.join()
	t6.join()
	t7.join()
	t8.join()
	t9.join()
	t10.join()
	
	count += 1
	mnt = tt.minute
	mnt = str(mnt)
	if (mnt) == "0":
		for i in musr.keys():
			if musr[i]["Duration"] != 0:
				musr[i]["Duration"] -= 1
			else:
				musr.pop(i)
		vu.set(musr)
	for i in df2.keys():
		time.sleep(1)
		if df2[i]["direc"] == "BUY":
			if df2[i]["open"] < df2[i]["close"]:
				bot.send_photo(chat_id = "@PROFITxFLOW_RESULTS", photo = lst[i], caption = "<b>📍PREVIOUS SIGNAL RESULT\n\n<i>📊Market : #{}\n📌Entry Spot : {}\n🛑Closed at : {}\n〽️Direction : UP📈\n🕑Entry Time : {}\n⌛️Expiry : 5 Minutes</i>\n\n⚠️RESULT : ✅💹WIN💹✅\n━━━━━━━━━━━━━━━━━━━━━\n🔺Non martingale content.\n🔺80% Accurate signals.\n🔺Get License 🔹<a href = 'https://t.me/PROFITxFLOW_SUPPORT'>Click Here</a>🔹\n🔺Signal Bot 🔹<a href = 'https://t.me/PROFITxFLOW_BOT'>Click Here</a>🔹</b>".format(i, df2[i]["open"], df2[i]["close"], df2[i]["tim"]), parse_mode = 'html')
				count += 1
			elif df2[i]["open"] > df2[i]["close"]:
				if count1 == 7:
					bot.send_photo(chat_id = "@PROFITxFLOW_RESULTS", photo = lst[i], caption = "<b>📍PREVIOUS SIGNAL RESULT\n\n<i>📊Market : #{}\n📌Entry Spot : {}\n🛑Closed at : {}\n〽️Direction : UP📈\n🕑Entry Time : {}\n⌛️Expiry : 5 Minutes</i>\n\n⚠️RESULT : ❌❌LOSE❌❌\n━━━━━━━━━━━━━━━━━━━━━\n🔺Non martingale content.\n🔺80% Accurate signals.\n🔺Get License 🔹<a href = 'https://t.me/PROFITxFLOW_SUPPORT'>Click Here</a>🔹\n🔺Signal Bot 🔹<a href = 'https://t.me/PROFITxFLOW_BOT'>Click Here</a>🔹</b>".format(i, df2[i]["open"], df2[i]["close"], df2[i]["tim"]), parse_mode = 'html')
					count1 = 0
		elif df2[i]["direc"] == "SELL":
			if df2[i]["open"] > df2[i]["close"]:
				bot.send_photo(chat_id = "@PROFITxFLOW_RESULTS", photo = lst[i], caption = "<b>📍PREVIOUS SIGNAL RESULT\n\n<i>📊Market : #{}\n📌Entry Spot : {}\n🛑Closed at : {}\n〽️Direction : DOWN📉\n🕑Entry Time : {}\n⌛️Expiry : 5 Minutes</i>\n\n⚠️RESULT : ✅💹WIN💹✅\n━━━━━━━━━━━━━━━━━━━━━\n🔺Non martingale content.\n🔺80% Accurate signals.\n🔺Get License 🔹<a href = 'https://t.me/PROFITxFLOW_SUPPORT'>Click Here</a>🔹\n🔺Signal Bot 🔹<a href = 'https://t.me/PROFITxFLOW_BOT'>Click Here</a>🔹</b>".format(i, df2[i]["open"], df2[i]["close"], df2[i]["tim"]), parse_mode = 'html')
				count += 1
			elif df2[i]["open"] < df2[i]["close"]:
				if count1 == 7:
					bot.send_photo(chat_id = "@PROFITxFLOW_RESULTS", photo = lst[i], caption = "<b>📍PREVIOUS SIGNAL RESULT\n\n<i>📊Market : #{}\n📌Entry Spot : {}\n🛑Closed at : {}\n〽️Direction : DOWN📉\n🕑Entry Time : {}\n⌛️Expiry : 5 Minutes</i>\n\n⚠️RESULT : ❌❌LOSE❌❌\n━━━━━━━━━━━━━━━━━━━━━\n🔺Non martingale content.\n🔺80% Accurate signals.\n🔺Get License 🔹<a href = 'https://t.me/PROFITxFLOW_SUPPORT'>Click Here</a>🔹\n🔺Signal Bot 🔹<a href = 'https://t.me/PROFITxFLOW_BOT'>Click Here</a>🔹</b>".format(i, df2[i]["open"], df2[i]["close"], df2[i]["tim"]), parse_mode = 'html')
					count1 = 0
					
	df2 = copy.deepcopy(df1)	
	time.sleep(60)

