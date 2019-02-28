# 2 Use https://randomuser.me API to download a random user data.
# Create and store 100 random users with ids, username, name (first + last name) using this API (2p)
import requests
import random
import json


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
	return user_1, user_2


def main():
	users = userGenerator(number_of_users=50)
	pairUsers(users)


main()
