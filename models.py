from google.appengine.api import users
from google.appengine.ext import ndb

class UserPrefs(ndb.Model):
	tz_offset = ndb.FloatProperty(default=0.0)
	user = ndb.UserProperty(auto_current_user_add=True)

def get_userprefs(user_id=None):
	if not user_id:
		user = users.get_current_user()
		if not user:
			return None
		user_id = user.user_id()

	key = ndb.Key('UserPrefs', user_id)
	userprefs = key.get()
	if not userprefs:
		userprefs = UserPrefs(id=user_id)
	return userprefs

class NewData(ndb.Model):
	new_entry = ndb.StringProperty(default=None)
	user = ndb.UserProperty(auto_current_user_add=True)

def get_newdata(user_id=None):
	if not user_id:
		user = users.get_current_user()
		if not user:
			return None
		user_id = user.user_id()

	key = ndb.Key('NewData', user_id)
	newdata = key.get()
	if not newdata:
		newdata = NewData(id=user_id)
	return newdata