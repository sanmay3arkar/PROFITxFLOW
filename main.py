from telegram import *
from telegram.ext import *
import time
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from additional.lists import mklst

bot = Bot("5813740213:AAErjpHMb6pwmKOeBGc7NO0T0HvSy0S58EE")
updates = Updater("5813740213:AAErjpHMb6pwmKOeBGc7NO0T0HvSy0S58EE", use_context = True)

cred = credentials.Certificate("profitxflow-39f9f-firebase-adminsdk-z9yva-296f8909b2.json")
firebase_admin.initialize_app(cred,
{
	'databaseURL' : "https://profitxflow-39f9f-default-rtdb.firebaseio.com"
}
)

JOIN, CHECK, HOME, CONFIRM, MKT= range(5)

mu = db.reference("Users")
musr = mu.get()

def start(update,context):
	user = update.effective_user
	chat = update.effective_chat
	if chat.type != "private":
		update.message.reply_text("<b>I am really sorry but i can only work on private chat. message me personally to use my fetures ;)</b>", parse_mode = "html")
		return
	
	if str(user.id) in musr.keys():
		key = ReplyKeyboardMarkup(
			[
				[
					"🔹Live Result",
					"🔹Bot Updates"
				],
				[
					"📊Selected Markets"
				],
				[
					"📞24/7 Support"
				]
			],
			resize_keyboard = True
		)
		update.message.reply_text("<b>You are at bot main menu. You will find all options below👇</b>", parse_mode = "html", reply_markup = key)
		return HOME
	key = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					"Intro",
					url = "https://youtu.be/9H2nyp4bLIE"
				),
				InlineKeyboardButton(
					"Live Test",
					url = "https://youtu.be/kt-dD7fztKI"
				)
			],
			[
				InlineKeyboardButton(
					"Live Results",
					url = "https://t.me/PROFITxFLOW_RESULTS"
				),
				InlineKeyboardButton(
					"Bot Updates",
					url = "https://t.me/PROFITxFLOW"
				)
			],
			[
				InlineKeyboardButton(
					"🔹JOIN NOW🔹",
					callback_data = "jn"
				)
			]
		]
	)
	update.message.reply_photo("https://firebasestorage.googleapis.com/v0/b/nagase-mana.appspot.com/o/Picsart_23-01-07_11-11-30-275.jpg?alt=media&token=ab39c225-da19-47bb-a190-6260bc91af1e", caption = "<b>⭕️PROFITxFLOW Bot\n\n</b><i>▪️This bot is made by King of Binary Trade Group (K.B.T Official). This is a well designed AI it can give 85% accurate binary signals based on market price action. all signals are takeable because all signals duration is 5 minutes but before taking this signals Proper money management is recomended.</i>\n\n🔹<b>This bot is <u>Free</u> for everyone. To get these signals click on <u>JOIN NOW</u> Below</b>", parse_mode = "html", reply_markup = key)
	return JOIN
	
def join(update, context):
	query = update.callback_query
	key1 = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					"Contact Us",
					url = "https://t.me/PROFITxFLOW_SUPPORT",
				)
			],
			[
				InlineKeyboardButton(
					"Join Link",
					url = "https://broker-qx.pro/sign-up/?lid=331267",
				)
			]
		]
	)
	bot.send_photo(chat_id = query.message.chat_id, photo = "https://firebasestorage.googleapis.com/v0/b/nagase-mana.appspot.com/o/sgnp.PNG?alt=media&token=d7609aa0-cadc-4cb8-802f-1e3f246c9d0f", caption = "<b>Dear {}👋,\n\nTo get free 85% accurate signals please follow the given Steps below👇\n\n🔹Please Create an Account on Quotex through given link below\n  • Link : <a href = 'https://broker-qx.pro/sign-up/?lid=331267'>Click Here</a>\n🔹Please Deposit minimum 50$ on this account to trade.\n\n<u>⭕️After doing the avobe steps Please send your ID Number here.</u>\n  • How to Find ID : <a href='https://telegra.ph/How-to-find-Quotex-ID-05-09'>Click Here</a>\n\n⚠️Note : </b><i>If you have an account on quotex then delete it from settings and create a new account with a new email through this link. its necessary to create a account through this link. after creating an account through this link and deposit 50$ on it everything will be set after that you can enjoy free 85% accurate signals for lifetime.</i>\n\n<b>Feel free to contact if you need any help ;)</b>".format(query.from_user.first_name), parse_mode = "html", reply_markup = key1)
	return CHECK
	
def check(update, context):
	qid = update.message.text
	user = update.message.from_user
	try:
		qqid = int(qid)
	except:
		update.message.reply_text("<b>Wrong ID❌\n\nI am really sorry. but the quotex ID should be numbers. please check how to find the ID and send again. thank you</b>", parse_mode = "html")
		return CHECK
	bot.send_message(chat_id = 1142185639, text = "<b>🔹User : <code>{}</code>\n🔹Name : <code>{}</code>\n🔹Quotex ID : <code>{}</code>\n\n⚠️Note : </b><i>this user applied for PROFITxFLOW Services. please check his query.</i>".format(user.id, user.full_name, qid), parse_mode = "html")
	update.message.reply_text("<b>Thanks👍\n\nPlease wait patiently our team will check it soon as possible. they will reply you with in 4 hours.</b>", parse_mode = "html")
	return CONFIRM

def confirm(update, context):
	query = update.callback_query
	if query.data == "re":
		key2 = InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						"Contact Us",
						url = "https://t.me/PROFITxFLOW_SUPPORT"
					)
				],
				[
					InlineKeyboardButton(
						"Join Link",
						url = "https://broker-qx.pro/sign-up/?lid=331267"
					)
				]
			]
		)
		bot.send_photo(chat_id = query.message.chat_id, photo = "https://firebasestorage.googleapis.com/v0/b/nagase-mana.appspot.com/o/sgnp.PNG?alt=media&token=d7609aa0-cadc-4cb8-802f-1e3f246c9d0f", caption = "<b>Dear {}👋,\n\nTo get free 85% accurate signals please follow the given Steps below👇\n\n🔹Please Create an Account on Quotex through given link below\n  • Link : <a href = 'https://broker-qx.pro/sign-up/?lid=331267'>Click Here</a>\n🔹Please Deposit minimum 50$ on this account to trade.\n\n<u>⭕️After doing the avobe steps Please send your ID Number here.</u>\n  • How to Find ID : <a href='https://telegra.ph/How-to-find-Quotex-ID-05-09'>Click Here</a>\n\n⚠️Note : </b><i>If you have an account on quotex then delete it from settings and create a new account with a new email through this link. its necessary to create a account through this link. after creating an account through this link and deposit 50$ on it everything will be set after that you can enjoy free 85% accurate signals for lifetime.</i>\n\n<b>Feel free to contact if you need any help ;)</b>".format(query.from_user.first_name), parse_mode = "html", reply_markup = key2)
		return CHECK
	elif query.data == "dn":
		key = ReplyKeyboardMarkup(
			[
				[
					"🔹Live Result",
					"🔹Bot Updates"
				],
				[
					"📊Selected Markets"
				],
				[
					"📞24/7 Support"
				]
			],
			resize_keyboard = True
		)
		key1 = InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						"Live Results",
						url = "https://t.me/PROFITxFLOW_RESULTS"	
					),
					InlineKeyboardButton(
						"Live Test",
						url = "https://youtu.be/kt-dD7fztKI"
					)
				],
				[
					InlineKeyboardButton(
						"K.B.T Official",
						url = "t.me/KINGOFBINARY"
					)
				]
			]
		)
		musr[str(query.from_user.id)] = ["K","AUDCAD", "AUDUSD", "EURGBP", "EURJPY", "EURUSD", "GBPUSD", "GBPJPY", "NZDUSD", "USDCHF", "USDJPY"]
		mu.set(musr)
		bot.send_photo(chat_id = query.message.chat_id, photo = "https://firebasestorage.googleapis.com/v0/b/nagase-mana.appspot.com/o/Picsart_23-01-07_11-11-30-275.jpg?alt=media&token=ab39c225-da19-47bb-a190-6260bc91af1e", caption = "<b>Well Done {}!!\n\nYou are now a official bot member✅\n\nYou will receive signals here from now on. Please use proper money management to use these signals and own tecnical analysis is recomemded. however all signals are 85% accurate and all signals are takeable.</b>".format(query.from_user.first_name), parse_mode = "html", reply_markup = key1)
		bot.send_message(chat_id = query.message.chat_id, text = "<b>You are at bot main menu. You will find all options below👇</b>", parse_mode = "html", reply_markup = key)
		return HOME

def res(update, context):
	key = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					"Live Results",
					url = "https://t.me/PROFITxFLOW_RESULTS"
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
	update.message.reply_text("<b>Below you will find bot Live Results and K.B.T Official Link👇\n\n🔹Live Results🔸<a href = 'https://t.me/PROFITxFLOW_RESULTS'>Click Here</a>🔸\n\n🔹K.B.T Official🔸<a href = 'https://t.me/KINGOFBINARY'>Click Here</a>🔸\n\n</b>📌<i>K.B.T Official is a binary trading group. exist since 2019. this group is made by some master lavel binary traders. they trade with deep concepts and strategy. in this group they have signals service, Binary teaching service. you are welcome to visit us.</i>", parse_mode = "html", reply_markup = key)
	return HOME

def upd(update, context):
	key = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					"Bot Updates",
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
	update.message.reply_text("<b>Below you will find bot Updates Channel and K.B.T Official Link👇\n\n🔹Bot Updates🔸<a href = 'https://t.me/PROFITxFLOW'>Click Here</a>🔸\n\n🔹K.B.T Official🔸<a href = 'https://t.me/KINGOFBINARY'>Click Here</a>🔸\n\n</b>📌<i>K.B.T Official is a binary trading group. exist since 2019. this group is made by some master lavel binary traders. they trade with deep concepts and strategy. in this group they have signals service, Binary teaching service. you are welcome to visit us.</i>", parse_mode = "html", reply_markup = key)
	return HOME

def sup(update, context):
	user = update.effective_user
	key = InlineKeyboardMarkup(
		[
			[
				InlineKeyboardButton(
					"Support Agent",
					url = "https://t.me/PROFITxFLOW_SUPPORT"
				)
			]
		]
	)
	update.message.reply_text("<b>Hey there {}👋\n\n<i>“Need any Help, Our Support agent always here to Help!!”</i>\n\n🔹Click to the button below to talk to our 24/7 Support agent👇</b>".format(user.first_name), parse_mode = "html", reply_markup = key)
	return HOME

def market(update, context):
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
		if i in musr[str(user.id)]:
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
		
		if "AUDCAD" in musr[str(user.id)]:
			musr[str(user.id)].remove("AUDCAD")
		else:
			musr[str(user.id)].append("AUDCAD")
				
		for i in mklst:
			if i in musr[str(user.id)]:
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
		
		if "AUDUSD" in musr[str(user.id)]:
			musr[str(user.id)].remove("AUDUSD")
		else:
			musr[str(user.id)].append("AUDUSD")
				
		for i in mklst:
			if i in musr[str(user.id)]:
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
		
		if "EURGBP" in musr[str(user.id)]:
			musr[str(user.id)].remove("EURGBP")
		else:
			musr[str(user.id)].append("EURGBP")
				
		for i in mklst:
			if i in musr[str(user.id)]:
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
		
		if "EURJPY" in musr[str(user.id)]:
			musr[str(user.id)].remove("EURJPY")
		else:
			musr[str(user.id)].append("EURJPY")
				
		for i in mklst:
			if i in musr[str(user.id)]:
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
		
		if "EURUSD" in musr[str(user.id)]:
			musr[str(user.id)].remove("EURUSD")
		else:
			musr[str(user.id)].append("EURUSD")
				
		for i in mklst:
			if i in musr[str(user.id)]:
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
		
		if "GBPUSD" in musr[str(user.id)]:
			musr[str(user.id)].remove("GBPUSD")
		else:
			musr[str(user.id)].append("GBPUSD")
				
		for i in mklst:
			if i in musr[str(user.id)]:
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
		
		if "GBPJPY" in musr[str(user.id)]:
			musr[str(user.id)].remove("GBPJPY")
		else:
			musr[str(user.id)].append("GBPJPY")
				
		for i in mklst:
			if i in musr[str(user.id)]:
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
		
		if "NZDUSD" in musr[str(user.id)]:
			musr[str(user.id)].remove("NZDUSD")
		else:
			musr[str(user.id)].append("NZDUSD")
				
		for i in mklst:
			if i in musr[str(user.id)]:
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
		
		if "USDCHF" in musr[str(user.id)]:
			musr[str(user.id)].remove("USDCHF")
		else:
			musr[str(user.id)].append("USDCHF")
				
		for i in mklst:
			if i in musr[str(user.id)]:
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
		
		if "USDJPY" in musr[str(user.id)]:
			musr[str(user.id)].remove("USDJPY")
		else:
			musr[str(user.id)].append("USDJPY")
				
		for i in mklst:
			if i in musr[str(user.id)]:
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
					"🔹Live Result",
					"🔹Bot Updates"
				],
				[
					"📊Selected Markets"
				],
				[
					"📞24/7 Support"
				]
			],
			resize_keyboard = True
		)
		bot.delete_message(query.message.chat_id, query.message.message_id)
		bot.send_message(chat_id = query.message.chat_id, text = "<b>You are at bot main menu. You will find all options below👇</b>", parse_mode = "html", reply_markup = key)
		return HOME

def console(update, context):
	user = update.effective_user
	if user.id != 1142185639:
		return
	text = update.message.text.split(None,1)
	try:
		text = text[1].split("|")
	except:
		update.message.reply_text("<b>Invalid Text Format please send like 👉 “/send user ID|Your Message|one or two” here | means Split, “one” means re check and “two” means everything is perfect</b>", parse_mode = "html")
		return
	if len(text) < 3:
		update.message.reply_text("<b>Less value detected. please send like this 👉 “/send user ID|Your Message|one or two” here | means Split, “one” means re check and “two” means everything is perfect</b>", parse_mode = "html")
		return
	if text[2] == "one":
		key = InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						"Re Submit",
						callback_data = "re"
					)
				]
			]
		)
	elif text[2] == "two":
		key = InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton(
						"Main Menu",
						callback_data = "dn"
					)
				]
			]
		)
	bot.send_message(chat_id = int(text[0]), text = "<b>{}</b>".format(text[1]), parse_mode = "html", reply_markup = key)


updates.dispatcher.add_handler(CommandHandler("send", console))

updates.dispatcher.add_handler(
	ConversationHandler(
		entry_points = [
			CommandHandler(
				"start",
				start
			)
		],
		states = {
			JOIN : [
				CallbackQueryHandler(
					join
				)
			],
			CHECK : [
				MessageHandler(
					Filters.text,
					check
				)
			],
			CONFIRM : [
				CallbackQueryHandler(
					confirm
				)
			],
			HOME : [
				MessageHandler(
					Filters.regex(
						"🔹Live Result"
					),
					res
				),
				MessageHandler(
					Filters.regex(
						"🔹Bot Updates"
					),
					upd
				),
				MessageHandler(
					Filters.regex(
						"📞24/7 Support"
					),
					sup
				),
				MessageHandler(
					Filters.regex(
						"📊Selected Markets"
					),
					market
				)
			],
			MKT : [
				CallbackQueryHandler(
					mkt
				)
			]
		},
		fallbacks = [
			CommandHandler(
				"start",
				start
			)
		]
	)
)
updates.start_polling()