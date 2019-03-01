import requests


def bitbayOrders(symbol):
	response = requests.get("https://bitbay.net/API/Public/" + symbol + "/orderbook.json")
	data = response.json()
	bids = data["bids"]
	asks = data["asks"]
	upper_bid = bids[0]
	upper_ask = asks[0]
	bid_course = upper_bid[0]
	ask_course = upper_ask[0]
	# print("upper bid course:", bid_course, "| upper ask course:", ask_course)
	return ask_course


def binanceOrders(symbol):
	response = requests.request("GET", "https://www.binance.com/api/v1/depth", params={"symbol": symbol})
	data = response.json()
	bids = data["bids"]
	asks = data["asks"]
	upper_bid = bids[0]
	upper_ask = asks[0]
	bid_course = float(upper_bid[0])
	ask_course = float(upper_ask[0])
	# print("upper bid course:", bid_course, "| upper ask course:", ask_course)
	return ask_course


if __name__ == '__main__':
	symbol = "ETHBTC"
	bitbayOrders(symbol)
	binanceOrders(symbol)
