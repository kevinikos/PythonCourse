from lab5.get_orderbook import bitbayOrders
import requests
import random


# def userGenerator(**kwargs):
# 	created_users.append(kwargs)
# 	return created_users
#
#
# def main():
# 	for user in range(0, number_of_users):
# 		userGenerator(id=users[user]["id"]["value"], first_name=users[user]["name"]["first"], last_name=users[user]["name"]["last"], username=users[user]["login"]["username"])


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


def tradeCrypto(user_1, user_2, ask_price, ask_amount):
	print(user_1, "exchanged", ask_amount, "ETH with", user_2, "for", ask_price, "BTC")


def main():
	users = userGenerator(number_of_users=50)
	user_1, user_2 = pairUsers(users)
	bid_price, bid_amount, ask_price, ask_amount = bitbayOrders("ethbtc")
	tradeCrypto(user_1, user_2, ask_price, ask_amount)


main()
