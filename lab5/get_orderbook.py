import requests


def bitbayOrders(symbol):
	response = requests.get("https://bitbay.net/API/Public/" + symbol + "/orderbook.json")
	data = response.json()
	bids = data["bids"]
	asks = data["asks"]
	upper_bid = bids[0]
	upper_ask = asks[0]
	bid_course = upper_bid[0]
	bid_amount = upper_bid[1]
	ask_course = upper_ask[0]
	ask_amount = upper_ask[1]
	bid_price = round(bid_course * bid_amount, 5)
	ask_price = round(ask_course * ask_amount, 5)
	# print("upper bid course:", bid_course, "| upper ask course:", ask_course)
	return bid_price, bid_amount, ask_price, ask_amount


if __name__ == '__main__':
	bitbayOrders("ethbtc")
