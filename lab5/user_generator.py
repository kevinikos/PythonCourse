from lab5.get_orderbook import bitbayOrders, binanceOrders
from cs50 import get_string
import lab5.get_ticker
import requests
import random
import time


def userGenerator(number_of_users):
	created_users = []
	response = requests.get("https://randomuser.me/api/?results=" + str(number_of_users))
	data = response.json()
	users = data["results"]
	for each_user in range(0, number_of_users):
		user = {}
		user["id"] = each_user
		# user["id"] = users[each_user]["id"]["value"]
		user["first_name"] = users[each_user]["name"]["first"]
		user["last_name"] = users[each_user]["name"]["last"]
		user["username"] = users[each_user]["login"]["username"]
		created_users.append(user)
	# print(json.dumps(created_users, indent=2, sort_keys=False))
	return created_users


def pairUsers(users):
	user_1, user_2 = random.sample(users, 2)
	return user_1["first_name"], user_2["first_name"]


def tradeCrypto(single_symbol, user_1, user_2, ask_course_bit, ask_course_bin):
	crypto_amount = random.uniform(0.5, 1.9)
	ask_price_bit = ask_course_bit * crypto_amount
	ask_course_bin = ask_course_bin * crypto_amount
	single_symbol = single_symbol.replace("BTC", "")
	print(user_1, "exchanged", round(crypto_amount, 6), single_symbol, "with", user_2, "for", round(ask_course_bin, 6), "BTC")


def main():
	binance_symbols = lab5.get_ticker.binanceSymbols()
	bitbay_symbols = lab5.get_ticker.bitbaySymbols()
	linked_symbols = lab5.get_ticker.linkedSymbols(binance_symbols, bitbay_symbols)
	for symbol in linked_symbols:
		print(symbol)
	print("-" * 10)
	symbol = get_string("cryptocurrency pair: ").upper()
	print("-" * 10)
	if symbol in linked_symbols:
		users = userGenerator(number_of_users=100)
		transaction_limit = 10
		while transaction_limit != 0:
			user_1, user_2 = pairUsers(users)
			bid_course_bit, ask_course_bit = bitbayOrders(symbol)
			bid_course_bin, ask_course_bin = binanceOrders(symbol)
			tradeCrypto(symbol, user_1, user_2, ask_course_bit, ask_course_bin)
			transaction_limit -= 1
			time.sleep(1.5)


main()
