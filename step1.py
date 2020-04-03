import json
import requests
import time
import csv
from jose import jwt

if __name__ == "__main__":
	main()

headers = ['User ID', 'First Name', 'Last Name', 'Email', 'Meetings']
class User:
	def __init__(self, userId, first_name, last_name, email, meetings):
		self.userId = userId
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.meetings = meetings
	def get(self):
		print("ID is: ", self.userId)
		print("First Name is: ", self.first_name)
		print("Last Name is: ", self.last_name)
		print("Email is: ", self.email)
		print("Meetings are: ", self.meetings)


##
# 1. Generate a JWT Token. This token should last 10 seconds to make any necessary calls.
##

api_key = ''
api_secret = ''
exp = int(time.time()+600)
encoded = jwt.encode({'iss' : api_key, 'exp': exp}, api_secret, algorithm='HS256')
print(encoded)

##
# 2. Make API call to List Users.
#	 - API Call: GET https://api.zoom.us/v2/users
#	 	- Parameters:
#	 		status = active
#	 		page_size = 300
##
def refresh():
	print('Initializing...')
	activeUserHeaders = {
		'authorization': "Bearer " + encoded,
		'content-type': "application/json"
	}

	activeUserParams = { 
		'status': 'active',
		'page_size': 300
	}

	response = requests.get('https://api.zoom.us/v2/users/', headers=activeUserHeaders, params=activeUserParams)
	resp = json.loads(response.content)

	# ##
	# # 3. Create a User object for each user and store in List
	# # print(resp['users'][0]['id'])
	# ##


	userResponse = resp['users']
	userList = []
	for item in userResponse:
		try:
			userId = item['id'].encode('utf-8')
		except KeyError:
			userId = ''
		try:
			first_name = item['first_name'].encode('utf-8')
		except KeyError:
			first_name = ''
		try:
			last_name = item['last_name'].encode('utf-8')
		except KeyError:
			last_name = ''
		try:
			email = item['email'].encode('utf-8')
		except KeyError:
			email = ''

		newUser = User(userId, first_name, last_name, email, [])
		#User.get(newUser)
		userList.append(newUser)

	##
	# 4. Store User List in CSV
	##
	with open('Active Users.csv', 'wb') as file:
		headers = ['User ID', 'First Name', 'Last Name', 'Email', 'Meetings']
		writer = csv.DictWriter(file, fieldnames=headers)
		writer.writeheader()
		for user in userList:
			writer.writerow({'User ID': user.userId, 'First Name': user.first_name, 'Last Name': user.last_name, 'Email': user.email, 'Meetings': user.meetings})
	file.close()

	##
	# 5. Repeat but for Pending
	##

	pendingUserHeaders = {
		'authorization': "Bearer " + encoded,
		'content-type': "application/json"
	}

	pendingUserParams = { 
		'status': 'pending',
		'page_size': 300
	}

	response = requests.get('https://api.zoom.us/v2/users/', headers=pendingUserHeaders, params=pendingUserParams)
	resp = json.loads(response.content)

	userResponse = resp['users']
	pendingUserList = []
	for item in userResponse:
		try:
			userId = item['id'].encode('utf-8')
		except KeyError:
			userId = ''
		try:
			first_name = item['first_name'].encode('utf-8')
		except KeyError:
			first_name = ''
		try:
			last_name = item['last_name'].encode('utf-8')
		except KeyError:
			last_name = ''
		try:
			email = item['email'].encode('utf-8')
		except KeyError:
			email = ''

		newUser = User(userId, first_name, last_name, email, [])
		#User.get(newUser)
		pendingUserList.append(newUser)


	with open('Pending Users.csv', 'wb') as file:
		headers = ['User ID', 'First Name', 'Last Name', 'Email', 'Meetings']
		writer = csv.DictWriter(file, fieldnames=headers)
		writer.writeheader()
		for user in pendingUserList:
			writer.writerow({'User ID': user.userId, 'First Name': user.first_name, 'Last Name': user.last_name, 'Email': user.email, 'Meetings': user.meetings})
	##
	# 6. Repeat but for Inactive
	##

	inactiveUserHeaders = {
		'authorization': "Bearer " + encoded,
		'content-type': "application/json"
	}

	inactiveUserParams = { 
		'status': 'inactive',
		'page_size': 300
	}

	response = requests.get('https://api.zoom.us/v2/users/', headers=inactiveUserHeaders, params=inactiveUserParams)
	resp = json.loads(response.content)

	userResponse = resp['users']
	inactiveUserList = []
	for item in userResponse:
		try:
			userId = item['id'].encode('utf-8')
		except KeyError:
			userId = ''
		try:
			first_name = item['first_name'].encode('utf-8')
		except KeyError:
			first_name = ''
		try:
			last_name = item['last_name'].encode('utf-8')
		except KeyError:
			last_name = ''
		try:
			email = item['email'].encode('utf-8')
		except KeyError:
			email = ''

		newUser = User(userId, first_name, last_name, email, [])
		#User.get(newUser)
		inactiveUserList.append(newUser)


	with open('Inactive Users.csv', 'wb') as file:
		headers = ['User ID', 'First Name', 'Last Name', 'Email', 'Meetings']
		writer = csv.DictWriter(file, fieldnames=headers)
		writer.writeheader()
		for user in inactiveUserList:
			writer.writerow({'User ID': user.userId, 'First Name': user.first_name, 'Last Name': user.last_name, 'Email': user.email, 'Meetings': user.meetings})


if __name__ == "__main__":
	print('Running..')

# def createUser(user):
# 	i = 0
# 	for item in user:
# 		if(item == 'id'):
# 			try:
# 				userId = user[item]
# 			except KeyError:
# 				userId = ''
# 		if(item == 'first_name'):
# 			try:
# 				first_name = user[item]
# 			except KeyError:
# 				first_name = ''
# 		if(item == 'last_name'):		
# 			try:
# 				last_name = user[item]
# 			except KeyError:
# 				last_name = ''
# 		if(item == 'email'):
# 			try:
# 				email = user[item]
# 			except KeyError:
# 				email = ''
# 	newUser = User(userId, first_name, last_name, email, [])
# 	User.get(newUser)
# 	addToPending(newUser)

# def addToPending(user):
# 	with open('Pending Users.csv', 'a') as file:
# 		writer = csv.DictWriter(file, headers)
# 		writer.writerow({'User ID': user['id'], 'First Name': user['first_name'], 'Last Name': user['last_name'], 'Email': user['email'], 'Meetings': []})

# def addToInactive(user):
# 	with open('Inactive Users.csv', 'a') as file:
# 		writer = csv.DictWriter(file, headers)
# 		writer.writerow({'User ID': user['id'], 'First Name': user['first_name'], 'Last Name': user['last_name'], 'Email': user['email'], 'Meetings': []})

# def addToActive(user):
# 	with open('Active Users.csv', 'a') as file:
# 		writer = csv.DictWriter(file, headers)
# 		writer.writerow({'User ID': user['id'], 'First Name': user['first_name'], 'Last Name': user['last_name'], 'Email': user['email'], 'Meetings': []})


