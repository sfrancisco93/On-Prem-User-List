from flask import Flask, request, render_template
import json
import csv
import os.path
from step1 import User, refresh


testUser = User('xxx', 'first', 'last', 'sam.lum@email.com', [])
refresh()
app = Flask(__name__)

@app.route("/user", methods=['POST'])
def userTriggered():
	event = request.get_json().get('event')
	payload = request.get_json().get('payload')
	userDetails = payload['object']

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
	refresh()

	return request.json

if __name__ == "__main__":
	app.run(debug = True)
