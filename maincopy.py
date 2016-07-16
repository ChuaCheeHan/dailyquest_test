import datetime
import jinja2
import os
import webapp2
import models

from google.appengine.api import users
from google.appengine.ext import ndb

template_env = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.getcwd()))

class MainPage(webapp2.RequestHandler): 
	def get(self):
		current_time = datetime.datetime.now()
		user = users.get_current_user()
		login_url = users.create_login_url(self.request.path)
		logout_url = users.create_logout_url(self.request.path)

		userprefs = models.get_userprefs()
		if userprefs:
			current_time += datetime.timedelta(0, 0, 0, 0, 0, userprefs.tz_offset)

		template = template_env.get_template('home.html')
		context = {
			'current_time': current_time,
			'user': user,
			'login_url': login_url,
			'logout_url': logout_url,
			'userprefs': userprefs,
		}
		self.response.out.write(template.render(context))

class Index(webapp2.RequestHandler):
	def get(self):
		current_time = datetime.datetime.now()
		user = users.get_current_user()
		login_url = users.create_login_url(self.request.path)
		logout_url = users.create_logout_url(self.request.path)

		userprefs = models.get_userprefs()
		if userprefs:
			current_time += datetime.timedelta(0, 0, 0, 0, 0, userprefs.tz_offset)

		template = template_env.get_template('index.html')
		context = {
			'current_time': current_time,
			'user': user,
			'login_url': login_url,
			'logout_url': logout_url,
			'userprefs': userprefs,
		}
		self.response.out.write(template.render(context))
		
class About(webapp2.RequestHandler):
    """Incomplete"""
    def get(self):
        template = template_env.get_template('about.html')
        self.response.out.write(template.render())

class Leaderboards(webapp2.RequestHandler):
    def get(self):
		user = users.get_current_user()
		login_url = users.create_login_url(self.request.path)
		logout_url = users.create_logout_url(self.request.path)

		template = template_env.get_template('leaderboards.html')
		context = {
			'user': user,
			'login_url': login_url,
			'logout_url': logout_url,
		}
		self.response.out.write(template.render(context))

class DQToday(webapp2.RequestHandler):
    def get(self):
		user = users.get_current_user()
		login_url = users.create_login_url(self.request.path)
		logout_url = users.create_logout_url(self.request.path)

		template = template_env.get_template('dqtoday.html')
		context = {
			'user': user,
			'login_url': login_url,
			'logout_url': logout_url,
		}
		self.response.out.write(template.render(context))	
		
class NewData(ndb.Model):
	dataget = ndb.StringProperty(default=None)
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

class addtask(webapp2.RequestHandler):
    def get(self):
		current_time = datetime.datetime.now()
		user = users.get_current_user()
		login_url = users.create_login_url(self.request.path)
		logout_url = users.create_logout_url(self.request.path)

		newdata = get_newdata()

		template = template_env.get_template('addtask.html')
		context = {
			'current_time': current_time,
			'user': user,
			'login_url': login_url,
			'logout_url': logout_url,
			'newdata': newdata,
		}
		self.response.out.write(template.render(context))

class DataPage(webapp2.RequestHandler):
	def post(self):
		newdata = get_newdata()
		try:
			dataget = self.request.get('dataget')
			newdata.dataget = dataget
			newdata.put()
		except ValueError:
			#input wrong value
			pass
		self.redirect('/addtask')


application = webapp2.WSGIApplication([('/', MainPage),
                                       ('/home', MainPage),
									   ('/index', Index),
									   ('/about', About),
									   ('/leaderboards', Leaderboards),
									   ('/dqtoday', DQToday),
									   ('/addtask', addtask),
									   ('/datapage', DataPage)],
									  debug=True)