def support(df1, l, n1, n2):
	for i in range(l-n1+1, l+1):
		if (df1[i]["open"]>df1[i-1]["open"]):
			return 0
	for i in range(l+1, l+n2+1):
		if (df1[i]["open"] < df1[i-1]["open"]):
			return 0
	return 1

def resistance(df1, l, n1, n2):
	for i in range(l-n1+1, l+1):
		if (df1[i]["close"]<df1[i-1]["close"]):
			return 0
	for i in range(l+1, l+n2+1):
		if (df1[i]["close"]>df1[i-1]["close"]):
			return 0
	return 1

def audcad(cred, t):
	df = cred.get_candles("AUDCAD", 300, 203, t.time())
	point = []
	for row in range(2, 198):
		if support(df, row, 2, 3):
			point.append(df[row]["open"])
		if resistance(df, row, 2, 3):
			point.append(df[row]["close"])
	return point

def audusd(cred, t):
	df = cred.get_candles("AUDUSD", 300, 203, t.time())
	point = []
	for row in range(2, 198):
		if support(df, row, 2, 3):
			point.append(df[row]["open"])
		if resistance(df, row, 2, 3):
			point.append(df[row]["close"])
	return point

def eurgbp(cred, t):
	df = cred.get_candles("EURGBP", 300, 203, t.time())
	point = []
	for row in range(2, 198):
		if support(df, row, 2, 3):
			point.append(df[row]["open"])
		if resistance(df, row, 2, 3):
			point.append(df[row]["close"])
	return point

def eurjpy(cred, t):
	df = cred.get_candles("EURJPY", 300, 203, t.time())
	point = []
	for row in range(2, 198):
		if support(df, row, 2, 3):
			point.append(df[row]["open"])
		if resistance(df, row, 2, 3):
			point.append(df[row]["close"])
	return point
	
def eurusd(cred, t):
	df = cred.get_candles("EURUSD", 300, 203, t.time())
	point = []
	for row in range(2, 198):
		if support(df, row, 2, 3):
			point.append(df[row]["open"])
		if resistance(df, row, 2, 3):
			point.append(df[row]["close"])
	return point

def gbpusd(cred, t):
	df = cred.get_candles("GBPUSD", 300, 203, t.time())
	point = []
	for row in range(2, 198):
		if support(df, row, 2, 3):
			point.append(df[row]["open"])
		if resistance(df, row, 2, 3):
			point.append(df[row]["close"])
	return point

def gbpjpy(cred, t):
	df = cred.get_candles("GBPJPY", 300, 203, t.time())
	point = []
	for row in range(2, 198):
		if support(df, row, 2, 3):
			point.append(df[row]["open"])
		if resistance(df, row, 2, 3):
			point.append(df[row]["close"])
	return point

def nzdusd(cred, t):
	df = cred.get_candles("NZDUSD", 300, 203, t.time())
	point = []
	for row in range(2, 198):
		if support(df, row, 2, 3):
			point.append(df[row]["open"])
		if resistance(df, row, 2, 3):
			point.append(df[row]["close"])
	return point

def usdchf(cred, t):
	df = cred.get_candles("USDCHF", 300, 203, t.time())
	point = []
	for row in range(2, 198):
		if support(df, row, 2, 3):
			point.append(df[row]["open"])
		if resistance(df, row, 2, 3):
			point.append(df[row]["close"])
	return point

def usdjpy(cred, t):
	df = cred.get_candles("USDJPY", 300, 203, t.time())
	point = []
	for row in range(2, 198):
		if support(df, row, 2, 3):
			point.append(df[row]["open"])
		if resistance(df, row, 2, 3):
			point.append(df[row]["close"])
	return point