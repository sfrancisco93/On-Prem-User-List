# Building Block for managing Zoom solely through terminal
In this script, we have created a User class in Python. The script will initially populate three CSV files on your end: Active, Pending, and Inactive. Afterwards, the script will continue to actively listen for incoming User webhooks from Zoom to move the user between the CSV files. 

# Pseudocode
	1. Call Get Users and retrieve all users
		- API Call: GET https://api.zoom.us/v2/users
		- Parameters:
			status = active
			page_size = 300

	2. For each user, create User
	3. Append User to User List
	4. Save User List in CSV File
	5. Continue listening for the following:
	
```python
	if(event == 'user.created'):
	print('User Alert - A User has been created.')
	if(event == 'user.invitation_accepted'):
		print('User Alert - A User accepted an invitation')
	if(event == 'user.updated'): 
		print('User Alert - A User has been updated')
	if(event == 'user.settings_updated'):
		print('User Alert - A user\'s settings has been updated')
	if(event == 'user.deactivated'):
		print('User Alert - A user has been deactivated')
	if(event == 'user.activated'):
		print('User Alert - A user has been activated')
	if(event == 'user.disassociated'):
		print('User Alert - A user has been disassociated')
	if(event == 'user.deleted'):
		print('User Alert - A user has been deleted')
```

	6. Update CSV files

#Future implementation
* Ability to run commands such as:
```python
	createUser('Email Address', 'First Name', 'Last Name', 'User Type')
	deleteUser('Email Address')
	bill = User('bill_nye@email.com')
	bill.createMeeting(meetingType, pmi, start date, start time)
```
