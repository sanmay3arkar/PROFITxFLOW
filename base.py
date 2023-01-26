from telegram import *
from telegram.ext import *
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from additional.lists import mklst
import time

bot = Bot("5813740213:AAErjpHMb6pwmKOeBGc7NO0T0HvSy0S58EE")
updates = Updater("5813740213:AAErjpHMb6pwmKOeBGc7NO0T0HvSy0S58EE", use_context = True)

cred = credentials.Certificate("profitxflow-39f9f-firebase-adminsdk-z9yva-296f8909b2.json")
firebase_admin.initialize_app(cred,
{
	'databaseURL' : "https://profitxflow-39f9f-default-rtdb.firebaseio.com"
}
)

delm = {}
mu = db.reference("VIPUser")
musr = mu.get()
u = db.reference("User")
usr = u.get()

for i in usr.keys():
	try:
		bot.send_message(chat_id = int(i), text = "<b>This bot has been restarted due to server maintenance. please use /start command to use again.</b>", parse_mode = "html")
	except:
		pass

onet = {}

ONE, HOME, SELECT, CODE, CHECK, CHECK2, MKT = range(7)

def start(update, context):
	user = update.effective_user
	chat = update.effective_chat
	if chat.type != "private":
		update.message.reply_text("<b>I am really sorry. but i only able to work in private chat. text me privately to use me ;)</b>", parse_mode = "html")
		return
	if str(user.id) in usr.keys():
		key = ReplyKeyboardMarkup(
		[
			[
				"🔹Subscription",
				"🔹Referral"
			],
			[
				"🔹Results",
				"📞Support"
			],
			[
				"📊Selected Markets"
			]
		],
		resize_keyboard = True
	)
		update.message.reply_text("<b>You are at bot main menu. You will find all options below👇</b>", parse_mode = "html", reply_markup = key)
		return HOME
	mes = update.message.reply_photo("https://firebasestorage.googleapis.com/v0/b/nagase-mana.appspot.com/o/Picsart_23-01-07_11-11-30-275.jpg?alt=media&token=ab39c225-da19-47bb-a190-6260bc91af1e", caption = "<b>Hello {}👋\n\n<i>Welcome to PROFITxFLOW. Here you can receive Automated AI based 70% accurate signals. Explore the below options to know more⭕️</i></b>".format(user.first_name), parse_mode = "html")
	
	button = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					"Results",
					url = "https://t.me/PROFITxFLOW_RESULTS"
				),
				InlineKeyboardButton(
					"Official Channel",
					url = "https://t.me/KINGOFBINARY"
				)
			],
			[
				InlineKeyboardButton(
					"Joined☑️",
					callback_data = "jn"
				)
			]
		]
	)
	time.sleep(2)
	txt = update.message.text
	txt = txt.split()
	if len(txt) == 2:
		txt = txt[1]
		try:
			txt = int(txt)
			onet[user.id] = str(txt)
		except:
			pass
	mes.delete()
	update.message.reply_text("<b>⭕️Please join the result channel and K.B.T Official channel to proceed further👇</b>", reply_markup = button, parse_mode = "html")
	return ONE

def one(update, context):
	query = update.callback_query
	m = bot.get_chat_member(chat_id = "@PROFITxFLOW_RESULTS", user_id = query.from_user.id)
	m1 = bot.get_chat_member(chat_id = "@KINGOFBINARY", user_id = query.from_user.id)
	if m.status != "member":
		if m.status != "creator":
			query.answer("make sure you joined all the mentioned channel and group..!!", show_alert = True)
			return
	if m1.status != "member":
		if m1.status != "creator":
			query.answer("make sure you joined all the mentioned channel and group..!!", show_alert = True)
			return
	
	uid = query.from_user.id
	if uid in onet.keys():
		if str(onet[uid]) in usr.keys():
			usr[onet[uid]]["Referral"].append(uid)
			try:
				bot.send_message(chat_id = onet[uid], text = "<b>Congratulations🎊.. {} has joined through your referral link✅</b>".format(query.from_user.first_name), parse_mode = "html")
			except:
				pass
			usr[str(uid)] = {}
			usr[str(uid)]["Referral"] = []
			usr[str(uid)]["Referral"].append(1)
			usr[str(uid)]["SReferral"] = 0
			usr[str(uid)]["UReferral"] = 0
			usr[str(uid)]["Refer By"] = onet[uid]
			onet.pop(uid)
	
	if str(uid) not in usr.keys():
		usr[str(uid)] = {}
		usr[str(uid)]["Referral"] = []
		usr[str(uid)]["Referral"].append(1)
		usr[str(uid)]["SReferral"] = 0
		usr[str(uid)]["UReferral"] = 0
	u.set(usr)
	ke = ReplyKeyboardMarkup(
		[
			[
				"🔹Subscription",
				"🔹Referral"
			],
			[
				"🔹Results",
				"📞Support"
			],
			[
				"📊Selected Markets"
			]
		],
		resize_keyboard = True
	)
	key1 = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					"Intro",
					url = "https://youtu.be/tvFxOWf_oUg"
				),
				InlineKeyboardButton(
					"Live Test",
					url = "https://youtu.be/6q2vpMkUSuk"
				)
			],
			[
				InlineKeyboardButton(
					"Updates",
					url = "https://t.me/PROFITxFLOW"
				)
			]
		]
	)
	
	
	
	bot.send_photo(chat_id = query.message.chat_id, photo = "https://firebasestorage.googleapis.com/v0/b/nagase-mana.appspot.com/o/Picsart_23-01-07_11-11-30-275.jpg?alt=media&token=ab39c225-da19-47bb-a190-6260bc91af1e", caption = "<b>⭕️PROFITxFLOW bot Home.\n\n</b><i>▪️This bot is made by King of Binary Trade Group (K.B.T Official). This is a well designed AI it can give 70% accurate binary signals based on market price action. all signals are takeable because all signals duration is 5 minutes but before taking this signals Proper money management is recomended. to get these signals you can buy Subscription from below</i>\n\n<b><u>♦️Subscription Packs👇</u>\n\n<i>🔹1 Week Plan : 19$\n🔹1 Month Plan : 69$\n🔹2 Month Plan : 119$\n🔹3 Month Plan : 149$</i></b>", parse_mode = "html", reply_markup = key1)
	
	bot.send_message(chat_id = query.message.chat_id, text = "<b>You are at bot main menu. You will find all options below👇</b>", parse_mode = "html", reply_markup = ke)
	
	bot.delete_message(query.message.chat_id, query.message.message_id)
	return HOME
	
def sup(update, context):
	user = update.effective_user
	
	key = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					"support",
					url = "https://t.me/PROFITxFLOW_SUPPORT"
				)
			]
		]
	)
	
	update.message.reply_text("<b>Hello There {},\nneed any kind of help, our support agent always here to help.!\n\nClick to this button below to talk to our support agent in person👇</b>".format(user.first_name), parse_mode = "html", reply_markup = key)
	return HOME
	
def res(update, context):
	key = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					"Results",
					url = "https://t.me/PROFITxFLOW_RESULTS"
				)
			],
			[
				InlineKeyboardButton(
					"Updates",
					url = "https://t.me/PROFITxFLOW"
				)
			],
			[
				InlineKeyboardButton(
					"K.B.T Official",
					url = "https://t.me/KINGOFBINARY"
				)
			]
		]
	)
	update.message.reply_text("<b>Here below you will find results channel and updates channel and K.B.T Official channel👇</b>", parse_mode = "html", reply_markup = key)
	return HOME

def sub(update, context):
	user = update.effective_user
	mes = update.message.reply_text("<b>Please Wait🔄...</b>", parse_mode = 'html', reply_markup = ReplyKeyboardRemove())
	time.sleep(1.3)
	if str(user.id) in musr.keys():
		days = musr[str(user.id)]["Duration"] / 24
		days = str(days)
		if "." in days:
			days = days.split(".")
			days = days[0]
		hours = int(days)
		hours = hours * 24
		hours = musr[str(user.id)]["Duration"] - hours
		if hours < 0:
			hours = 0
		key = ReplyKeyboardMarkup(
		[
			[
				"🔹Subscription",
				"🔹Referral"
			],
			[
				"🔹Results",
				"📞Support"
			],
			[
				"📊Selected Markets"
			]
		],
		resize_keyboard = True
	)
		mes.delete()
		update.message.reply_text("<b>Hello there {}👋\n\n• Your subscription going to end in👇\n🔹{} Days {} Hours🔹\n\nHope you're enjoying the signal service. Good Luck✅</b>".format(user.first_name, days, hours), parse_mode = "html", reply_markup = key)
		return HOME
	mes.delete()
	key = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					"Enter Code",
					callback_data = "ec"
				),
				InlineKeyboardButton(
					"Buy Code",
					callback_data = "bc"
				)
			],
			[
				InlineKeyboardButton(
					"Cancel",
					callback_data = "bk"
				)
			]
		]
	)
	update.message.reply_text("<b>Opps..!! You don't have any active Subscription.\n\n⭕️Follow the Buttons below to Enter new code or buy new code👇</b>", parse_mode = "html", reply_markup = key)
	return SELECT

def select(update, context):
	query = update.callback_query
	if query.data == "ec":
		key = InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						"Cancel",
						callback_data = "cl"
					)
				]
			]
		)
		query.edit_message_text("<b>Please Send Your Subscription Code👇</b>", parse_mode = "html", reply_markup = key)
		delm[query.from_user.id] = query.message.message_id
		return CODE
	elif query.data == "bc":
		key = InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						"Support",
						url = "https://t.me/PROFITxFLOW_SUPPORT"
					)
				]
			]
		)
		query.edit_message_text("<b>Hello there {},\n\nIf you want to buy a new subscription code then kindly talk to our Support agent for further assistance✅\n\nHere is our Plans:\n<i>🔹1 Week Plan : 19$\n🔹1 Month Plan : 69$\n🔹2 Month Plan : 119$\n🔹3 Month Plan : 149$</i></b>".format(query.from_user.first_name), parse_mode = "html", reply_markup = key)
		key = ReplyKeyboardMarkup(
		[
			[
				"🔹Subscription",
				"🔹Referral"
			],
			[
				"🔹Results",
				"📞Support"
			],
			[
				"📊Selected Markets"
			]
		],
		resize_keyboard = True
	)
		mes = bot.send_message(chat_id = query.message.chat_id, text = "<b>• Bot Main Menu</b>", parse_mode = "html", reply_markup = key)
		return HOME
	elif query.data == "bk":
		key = ReplyKeyboardMarkup(
		[
			[
				"🔹Subscription",
				"🔹Referral"
			],
			[
				"🔹Results",
				"📞Support"
			],
			[
				"📊Selected Markets"
			]
		],
		resize_keyboard = True
	)
		bot.delete_message(query.message.chat_id, query.message.message_id)
		bot.send_message(chat_id = query.message.chat_id, text = "<b>You are at bot main menu. You will find all options below👇</b>", parse_mode = "html", reply_markup = key)
		return HOME

def codeq(update, context):
	query = update.callback_query
	if query.data == "cl":
		key = ReplyKeyboardMarkup(
		[
			[
				"🔹Subscription",
				"🔹Referral"
			],
			[
				"🔹Results",
				"📞Support"
			],
			[
				"📊Selected Markets"
			]
		],
		resize_keyboard = True
	)
		bot.delete_message(query.message.chat_id, query.message.message_id)
		bot.send_message(chat_id = query.message.chat_id, text = "<b>You are at bot main menu. You will find all options below👇</b>", parse_mode = "html", reply_markup = key)
		return HOME

def code(update, context):
	mes = update.message.reply_text("<b>Please Wait🔄...</b>", parse_mode = "html")
	bot.delete_message(update.message.chat_id, delm[update.effective_user.id])
	dels = db.reference("Codes")
	scodes = dels.get()
	if update.message.text not in scodes.keys():
		mes.edit_text("<b>The code you entered was invalid❌... Please try again.</b>", parse_mode = "html")
		time.sleep(2)
		key = InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						"Cancel",
						callback_data = "cl"
					)
				]
			]
		)
		mes.edit_text("<b>Please Send Your Subscription Code👇</b>", parse_mode = "html", reply_markup = key)
		delm[update.effective_user.id] = mes.message_id
		return CODE
		
	key = ReplyKeyboardMarkup(
		[
			[
				"🔹Subscription",
				"🔹Referral"
			],
			[
				"🔹Results",
				"📞Support"
			],
			[
				"📊Selected Markets"
			]
		],
		resize_keyboard = True
	)
	musr[str(update.effective_user.id)] = {}
	musr[str(update.effective_user.id)]["Duration"] = scodes[update.message.text]
	musr[str(update.effective_user.id)]["Markets"] = ["AUDCAD", "AUDUSD", "EURGBP", "EURJPY", "EURUSD", "GBPUSD", "GBPJPY", "NZDUSD", "USDCHF", "USDJPY", "A"]
	if "Refer By" in usr[str(update.effective_user.id)].keys():
		usr[usr[str(update.effective_user.id)]["Refer By"]]["SReferral"] += 1
		bot.send_message(chat_id = usr[str(update.effective_user.id)]["Refer By"], text = "<b>Congratulations🎊.. 1 Successful referral has been added to your account.</b>", parse_mode = "html")
		usr[usr[str(update.effective_user.id)]["Refer By"]]["Referral"].remove(update.effective_user.id)
		usr[str(update.effective_user.id)].pop("Refer By")
		u.set(usr)
	scodes.pop(update.message.text)
	dels.set(scodes)
	mu.set(musr)
	days = musr[str(update.effective_user.id)]["Duration"] / 24
	days = str(days)
	if "." in days:
		days = days.split(".")
		days = days[0]
	mes.delete()
	update.message.reply_text("<b>Congratulations🎊.. Your Subscription for {} days has been started from now on✅\n\nThanks For joining us☑️</b>".format(days), parse_mode = "html", reply_markup = key)
	return HOME

def rfr(update,context):
	user = update.effective_user
	mes = update.message.reply_text("<b>Please Wait🔄...</b>", parse_mode = "html", reply_markup = ReplyKeyboardRemove())
	time.sleep(1.5)
	key = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					"Know More",
					callback_data = "km"
				)
			],
			[
				InlineKeyboardButton(
					"Back",
					callback_data = "bk"
				)
			]
		]
	)
	mes.delete()
	update.message.reply_photo(photo = "https://firebasestorage.googleapis.com/v0/b/nagase-mana.appspot.com/o/Picsart_23-01-08_17-36-32-623.jpg?alt=media&token=6cd6e4da-82c3-4931-9569-3573d8793c1f", caption = "<b>Hello there {}👋\n\n🔸Your total referral is {} ☑️\n🔸Your successful referral is {} ☑️\n🔸Your used referral is {} ☑️\n\nHere is your referral link👇\n🔹https://telegram.me/{}?start={}\n\nClick on the button below to know more👇</b>".format(user.first_name, len(usr[str(user.id)]["Referral"]) - 1 + usr[str(user.id)]["SReferral"] + usr[str(user.id)]["UReferral"], usr[str(user.id)]["SReferral"], usr[str(user.id)]["UReferral"], bot.username, user.id), parse_mode = "html", reply_markup = key)
	return CHECK

def check(update, context):
	query = update.callback_query
	if query.data == "bk":
		bot.delete_message(query.message.chat_id, query.message.message_id)
		key = ReplyKeyboardMarkup(
		[
			[
				"🔹Subscription",
				"🔹Referral"
			],
			[
				"🔹Results",
				"📞Support"
			],
			[
				"📊Selected Markets"
			]
		],
		resize_keyboard = True
	)
		bot.send_message(chat_id = query.message.chat_id, text = "<b>You are at bot main menu. You will find all options below👇</b>", parse_mode = "html", reply_markup = key)
		return HOME
	elif query.data == "km":
		key = InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						"Back",
						callback_data = "bk"
					)
				]
			]
		)
		bot.delete_message(query.message.chat_id, query.message.message_id)
		bot.send_message(chat_id = query.message.chat_id, text = "<b><u>⭕️Referral Program:</u>\n\n<i>🔹After your friend joined through your referral link, it will count as a referral on your dashboard.\n\n🔹When your friend purchase a subscription plan it will count as a successful referral immediately.\n\n🔹For each successful referral you will get 5$ off on the subscription plan.\n\n🔹For 4 successful referral you will get 1 week signal plan for free.\n\n🔹For 15 successful referral you will get 1 month signal plan for free.\n\n🔹After you purchase plan through referral discount, Your referral will count as a used referral.</i></b>", parse_mode = "html", reply_markup = key)
		return CHECK2

def check2(update, context):
	query = update.callback_query
	user = query.from_user
	bot.delete_message(query.message.chat_id, query.message.message_id)
	key = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					"Know More",
					callback_data = "km"
				)
			],
			[
				InlineKeyboardButton(
					"Back",
					callback_data = "bk"
				)
			]
		]
	)
	bot.send_photo(chat_id = query.message.chat_id, photo = "https://firebasestorage.googleapis.com/v0/b/nagase-mana.appspot.com/o/Picsart_23-01-08_17-36-32-623.jpg?alt=media&token=6cd6e4da-82c3-4931-9569-3573d8793c1f", caption = "<b>Hello there {}👋\n\n🔸Your total referral is {} ☑️\n🔸Your successful referral is {} ☑️\n🔸Your used referral is {} ☑️\n\nHere is your referral link👇\n🔹https://telegram.me/{}?start={}\n\nClick on the button below to know more👇</b>".format(user.first_name, len(usr[str(user.id)]["Referral"]) -1 + usr[str(user.id)]["SReferral"] + usr[str(user.id)]["UReferral"], usr[str(user.id)]["SReferral"], usr[str(user.id)]["UReferral"], bot.username, user.id), parse_mode = "html", reply_markup = key)
	return CHECK

def mrket(update, context):
	if str(update.effective_user.id) not in musr.keys():
		update.message.reply_text("<b>Opps..!! it's looks like you do not have any active plan. please purchase a subscription code then activate it then try again⭕️</b>", parse_mode = "html")
		return HOME
	mes = update.message.reply_text("<b>Please Wait🔄...</b>", parse_mode = "html", reply_markup = ReplyKeyboardRemove())
	time.sleep(1.3)
	key = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					"AUDCAD",
					callback_data = "AC"
				),
				InlineKeyboardButton(
					"AUDUSD",
					callback_data = "AU"
				),
				InlineKeyboardButton(
					"EURGBP",
					callback_data = "EG"
				)
			],
			[
				InlineKeyboardButton(
					"EURJPY",
					callback_data = "EJ"
				),
				InlineKeyboardButton(
					"EURUSD",
					callback_data = "EU"
				),
				InlineKeyboardButton(
					"GBPUSD",
					callback_data = "GU"
				)
			],
			[
				InlineKeyboardButton(
					"GBPJPY",
					callback_data = "GJ"
				),
				InlineKeyboardButton(
					"NZDUSD",
					callback_data = "NU"
				),
				InlineKeyboardButton(
					"USDCHF",
					callback_data = "UC"
				)
			],
			[
				InlineKeyboardButton(
					"USDJPY",
					callback_data = "UJ"
				)
			],
			[
				InlineKeyboardButton(
					"Back",
					callback_data = "mb"
				)
			]
		]
	)
	user = update.effective_user	
	txt = "<b>⭕️Here are the list of your selected markets👇\n\n"
	for i in mklst:
		if i in musr[str(user.id)]["Markets"]:
			txt += "🔹{} (✅)\n".format(i)
		else:
			txt += "🔹{} (❌)\n".format(i)
	txt += "\nClick on the buttons below to enable and disable any specific market👇</b>"
	mes.delete()
	update.message.reply_text(txt, parse_mode = "html", reply_markup = key)
	return MKT

def mkt(update, context):
	key = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					"AUDCAD",
					callback_data = "AC"
				),
				InlineKeyboardButton(
					"AUDUSD",
					callback_data = "AU"
				),
				InlineKeyboardButton(
					"EURGBP",
					callback_data = "EG"
				)
			],
			[
				InlineKeyboardButton(
					"EURJPY",
					callback_data = "EJ"
				),
				InlineKeyboardButton(
					"EURUSD",
					callback_data = "EU"
				),
				InlineKeyboardButton(
					"GBPUSD",
					callback_data = "GU"
				)
			],
			[
				InlineKeyboardButton(
					"GBPJPY",
					callback_data = "GJ"
				),
				InlineKeyboardButton(
					"NZDUSD",
					callback_data = "NU"
				),
				InlineKeyboardButton(
					"USDCHF",
					callback_data = "UC"
				)
			],
			[
				InlineKeyboardButton(
					"USDJPY",
					callback_data = "UJ"
				)
			],
			[
				InlineKeyboardButton(
					"Back",
					callback_data = "mb"
				)
			]
		]
	)
	query = update.callback_query
	if query.data == "AC":
		user = query.from_user
		txt = "<b>⭕️Here are the list of your selected markets👇\n\n"
		
		if "AUDCAD" in musr[str(user.id)]["Markets"]:
			musr[str(user.id)]["Markets"].remove("AUDCAD")
		else:
			musr[str(user.id)]["Markets"].append("AUDCAD")
				
		for i in mklst:
			if i in musr[str(user.id)]["Markets"]:
				txt += "🔹{} (✅)\n".format(i)
			else:
				txt += "🔹{} (❌)\n".format(i)
		txt += "\nClick on the buttons below to enable and disable any specific market👇</b>"
		mu.set(musr)
		query.edit_message_text(txt, parse_mode = "html", reply_markup = key)
		return MKT
	
	elif query.data == "AU":
		user = query.from_user
		txt = "<b>⭕️Here are the list of your selected markets👇\n\n"
		
		if "AUDUSD" in musr[str(user.id)]["Markets"]:
			musr[str(user.id)]["Markets"].remove("AUDUSD")
		else:
			musr[str(user.id)]["Markets"].append("AUDUSD")
				
		for i in mklst:
			if i in musr[str(user.id)]["Markets"]:
				txt += "🔹{} (✅)\n".format(i)
			else:
				txt += "🔹{} (❌)\n".format(i)
		txt += "\nClick on the buttons below to enable and disable any specific market👇</b>"
		mu.set(musr)
		query.edit_message_text(txt, parse_mode = "html", reply_markup = key)
		return MKT
	
	elif query.data == "EG":
		user = query.from_user
		txt = "<b>⭕️Here are the list of your selected markets👇\n\n"
		
		if "EURGBP" in musr[str(user.id)]["Markets"]:
			musr[str(user.id)]["Markets"].remove("EURGBP")
		else:
			musr[str(user.id)]["Markets"].append("EURGBP")
				
		for i in mklst:
			if i in musr[str(user.id)]["Markets"]:
				txt += "🔹{} (✅)\n".format(i)
			else:
				txt += "🔹{} (❌)\n".format(i)
		txt += "\nClick on the buttons below to enable and disable any specific market👇</b>"
		mu.set(musr)
		query.edit_message_text(txt, parse_mode = "html", reply_markup = key)
		return MKT
	
	elif query.data == "EJ":
		user = query.from_user
		txt = "<b>⭕️Here are the list of your selected markets👇\n\n"
		
		if "EURJPY" in musr[str(user.id)]["Markets"]:
			musr[str(user.id)]["Markets"].remove("EURJPY")
		else:
			musr[str(user.id)]["Markets"].append("EURJPY")
				
		for i in mklst:
			if i in musr[str(user.id)]["Markets"]:
				txt += "🔹{} (✅)\n".format(i)
			else:
				txt += "🔹{} (❌)\n".format(i)
		txt += "\nClick on the buttons below to enable and disable any specific market👇</b>"
		mu.set(musr)
		query.edit_message_text(txt, parse_mode = "html", reply_markup = key)
		return MKT
	
	elif query.data == "EU":
		user = query.from_user
		txt = "<b>⭕️Here are the list of your selected markets👇\n\n"
		
		if "EURUSD" in musr[str(user.id)]["Markets"]:
			musr[str(user.id)]["Markets"].remove("EURUSD")
		else:
			musr[str(user.id)]["Markets"].append("EURUSD")
				
		for i in mklst:
			if i in musr[str(user.id)]["Markets"]:
				txt += "🔹{} (✅)\n".format(i)
			else:
				txt += "🔹{} (❌)\n".format(i)
		txt += "\nClick on the buttons below to enable and disable any specific market👇</b>"
		mu.set(musr)
		query.edit_message_text(txt, parse_mode = "html", reply_markup = key)
		return MKT
	
	elif query.data == "GU":
		user = query.from_user
		txt = "<b>⭕️Here are the list of your selected markets👇\n\n"
		
		if "GBPUSD" in musr[str(user.id)]["Markets"]:
			musr[str(user.id)]["Markets"].remove("GBPUSD")
		else:
			musr[str(user.id)]["Markets"].append("GBPUSD")
				
		for i in mklst:
			if i in musr[str(user.id)]["Markets"]:
				txt += "🔹{} (✅)\n".format(i)
			else:
				txt += "🔹{} (❌)\n".format(i)
		txt += "\nClick on the buttons below to enable and disable any specific market👇</b>"
		mu.set(musr)
		query.edit_message_text(txt, parse_mode = "html", reply_markup = key)
		return MKT
	
	elif query.data == "GJ":
		user = query.from_user
		txt = "<b>⭕️Here are the list of your selected markets👇\n\n"
		
		if "GBPJPY" in musr[str(user.id)]["Markets"]:
			musr[str(user.id)]["Markets"].remove("GBPJPY")
		else:
			musr[str(user.id)]["Markets"].append("GBPJPY")
				
		for i in mklst:
			if i in musr[str(user.id)]["Markets"]:
				txt += "🔹{} (✅)\n".format(i)
			else:
				txt += "🔹{} (❌)\n".format(i)
		txt += "\nClick on the buttons below to enable and disable any specific market👇</b>"
		mu.set(musr)
		query.edit_message_text(txt, parse_mode = "html", reply_markup = key)
		return MKT
	
	elif query.data == "NU":
		user = query.from_user
		txt = "<b>⭕️Here are the list of your selected markets👇\n\n"
		
		if "NZDUSD" in musr[str(user.id)]["Markets"]:
			musr[str(user.id)]["Markets"].remove("NZDUSD")
		else:
			musr[str(user.id)]["Markets"].append("NZDUSD")
				
		for i in mklst:
			if i in musr[str(user.id)]["Markets"]:
				txt += "🔹{} (✅)\n".format(i)
			else:
				txt += "🔹{} (❌)\n".format(i)
		txt += "\nClick on the buttons below to enable and disable any specific market👇</b>"
		mu.set(musr)
		query.edit_message_text(txt, parse_mode = "html", reply_markup = key)
		return MKT
	
	elif query.data == "UC":
		user = query.from_user
		txt = "<b>⭕️Here are the list of your selected markets👇\n\n"
		
		if "USDCHF" in musr[str(user.id)]["Markets"]:
			musr[str(user.id)]["Markets"].remove("USDCHF")
		else:
			musr[str(user.id)]["Markets"].append("USDCHF")
				
		for i in mklst:
			if i in musr[str(user.id)]["Markets"]:
				txt += "🔹{} (✅)\n".format(i)
			else:
				txt += "🔹{} (❌)\n".format(i)
		txt += "\nClick on the buttons below to enable and disable any specific market👇</b>"
		mu.set(musr)
		query.edit_message_text(txt, parse_mode = "html", reply_markup = key)
		return MKT
	
	elif query.data == "UJ":
		user = query.from_user
		txt = "<b>⭕️Here are the list of your selected markets👇\n\n"
		
		if "USDJPY" in musr[str(user.id)]["Markets"]:
			musr[str(user.id)]["Markets"].remove("USDJPY")
		else:
			musr[str(user.id)]["Markets"].append("USDJPY")
				
		for i in mklst:
			if i in musr[str(user.id)]["Markets"]:
				txt += "🔹{} (✅)\n".format(i)
			else:
				txt += "🔹{} (❌)\n".format(i)
		txt += "\nClick on the buttons below to enable and disable any specific market👇</b>"
		mu.set(musr)
		query.edit_message_text(txt, parse_mode = "html", reply_markup = key)
		return MKT
	
	elif query.data == "mb":
		key = ReplyKeyboardMarkup(
			[
				[
					"🔹Subscription",
					"🔹Referral"
				],
				[
					"🔹Results",
					"📞Support"
				],
				[
					"📊Selected Markets"
				]
			],
			resize_keyboard = True
		)
		bot.delete_message(query.message.chat_id, query.message.message_id)
		bot.send_message(chat_id = query.message.chat_id, text = "<b>You are at bot main menu. You will find all options below👇</b>", parse_mode = "html", reply_markup = key)
		return HOME


updates.dispatcher.add_handler(ConversationHandler(
	entry_points=[CommandHandler("start", start)],
	states = {
			ONE : [CallbackQueryHandler(one)],
			HOME : [MessageHandler(Filters.regex("📞Support"), sup),
			MessageHandler(Filters.regex("🔹Results"), res), MessageHandler(Filters.regex("🔹Subscription"), sub),
			MessageHandler(Filters.regex("🔹Referral"), rfr), MessageHandler(Filters.regex("📊Selected Markets"), mrket)],
			SELECT : [CallbackQueryHandler(select)],
			CODE : [CallbackQueryHandler(codeq),
			MessageHandler(Filters.text, code)],
			CHECK : [CallbackQueryHandler(check)],
			CHECK2 : [CallbackQueryHandler(check2)],
			MKT : [CallbackQueryHandler(mkt)]
		},
		fallbacks = [CommandHandler("start", start)]
	)
)
updates.start_polling()