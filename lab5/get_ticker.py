import requests
import time


def bitbayTicker(symbol):
	response = requests.get("https://bitbay.net/API/Public/" + symbol + "/ticker.json")
	data = response.json()
	best_bid = data["bid"]
	best_ask = data["ask"]
	print("BitBay")
	print("bid:", best_bid, "ask:", best_ask)
	return best_bid, best_ask


def binanceTicker(symbol):
	response = requests.get('https://api.binance.com/api/v1/ticker/bookTicker')
	data = response.json()
	for item in data:
		# if item['symbol'] == symbol.upper():
		if symbol.upper() in item["symbol"]:
			best_bid = float(item["bidPrice"])
			best_ask = float(item["askPrice"])
			print("Binance")
			print("bid:", best_bid, "ask:", best_ask)
			return best_bid, best_ask


def comparePrices(crypto_pair):
	bid_bitbay, ask_bitbay = bitbayTicker(crypto_pair)
	bid_binance, ask_binance = binanceTicker(crypto_pair)
	profit_bitbay = ((bid_bitbay - ask_binance) / bid_bitbay) * 100
	profit_binance = ((bid_binance - ask_bitbay) / bid_binance) * 100
	if profit_bitbay > 0 or profit_binance > 0:
		if profit_bitbay > profit_binance:
			print("Currently the Binance exchange market is better for buying while BitBay is better for selling")
			print("Profit:", round(profit_bitbay, 2), "%")
		else:
			print("Currently the BitBay exchange market is better for buying while Binance is better for selling")
			print("Profit:", round(profit_binance, 2), "%")
	else:
		print("Currently it is not worth to trade between given exchanges")
	# print(profit_bitbay, profit_binance)


def binanceSymbols():
	response = requests.get('https://api.binance.com/api/v1/ticker/bookTicker')
	data = response.json()
	symbols = []
	for item in range(len(data)):
		# print(data[item]['symbol'])
		symbols.append(data[item]['symbol'])
	return symbols


def bitbaySymbols():
	single_symbols = ["ETH", "LSK", "LTC", "GAME", "DASH", "BCC", "BTG", "KZC", "XIN", "XRP", "XMR", "ZEC", "GNT", "OMG", "FTO", "ZRX", "PAY", "BAT", "REP", "NEU", "TRX", "AMLT", "EXY", "BOB", "LML", "BSV", "XBX", "XLM"]
	symbols = [symbol.replace(symbol, symbol + "BTC") for symbol in single_symbols]
	return symbols


def linkedSymbols(binance_symbols, bitbay_symbols):
	linked_symbols = []
	for symbol in bitbay_symbols:
		if symbol in binance_symbols:
			linked_symbols.append(symbol)
	return linked_symbols


def main():
	binance_symbols = binanceSymbols()
	bitbay_symbols = bitbaySymbols()
	linked_symbols = linkedSymbols(binance_symbols, bitbay_symbols)
	for symbol in linked_symbols:
		print(symbol)
		try:
			comparePrices(symbol)
		except ZeroDivisionError as division_error:
			print(division_error)
		print("_" * 100)
		time.sleep(1)


main()
