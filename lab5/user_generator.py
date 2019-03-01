from lab5.get_orderbook import bitbayOrders, binanceOrders
from cs50 import get_string
import lab5.get_ticker
import requests
import random
import time
import json


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
		user["wallet"] = {}
		user["wallet"]["btc"] = 10
		user["wallet"]["eth"] = 10
		created_users.append(user)
	# print(json.dumps(created_users, indent=2, sort_keys=False))
	return created_users


def pairUsers(users):
	user_1, user_2 = random.sample(users, 2)
	return user_1["username"], user_2["username"]


def tradeCrypto(single_symbol, user_1, user_2, course_binance):
	"""currently binance on fire"""
	user_1_amount = random.uniform(0.5, 1.9)
	user_2_amount = course_binance * user_1_amount
	single_symbol = single_symbol.replace("BTC", "")
	print(user_1, "exchanged", round(user_1_amount, 6), single_symbol, "with", user_2, "for", round(user_2_amount, 6), "BTC")
	return user_1, user_2, user_1_amount, user_2_amount


def userBalances(users, user_1, user_2, user_1_amount, user_2_amount):
	for user_id in range(0, len(users)):
		user_match = users[user_id]["username"]
		if user_1 == user_match:
			users[user_id]["wallet"]["eth"] -= user_1_amount
			users[user_id]["wallet"]["btc"] += user_2_amount
		elif user_2 == user_match:
			users[user_id]["wallet"]["eth"] += user_1_amount
			users[user_id]["wallet"]["btc"] -= user_2_amount
	return users


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
		users = userGenerator(number_of_users=5)
		transaction_limit = 2
		while transaction_limit != 0:
			user_1, user_2 = pairUsers(users)
			course_binance = binanceOrders(symbol)
			user_1, user_2, user_1_amount, user_2_amount = tradeCrypto(symbol, user_1, user_2, course_binance)
			userBalances(users, user_1, user_2, user_1_amount, user_2_amount)
			transaction_limit -= 1
			time.sleep(1.5)
		print("-" * 10)
		print(json.dumps(users, indent=2, sort_keys=False))


main()
