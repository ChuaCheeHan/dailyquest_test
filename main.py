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


		template = template_env.get_template('home.html')
		context = {
			'current_time': current_time,
			'user': user,
			'login_url': login_url,
			'logout_url': logout_url,
		}
		self.response.out.write(template.render(context))

class Index(webapp2.RequestHandler):
	def get(self):
	    
		current_time = datetime.datetime.today().isoweekday()
		user = users.get_current_user()
		login_url = users.create_login_url(self.request.path)
		logout_url = users.create_logout_url(self.request.path)

		newdata = get_newdata()
		newdata1 = get_newdata_1()
		newdata2 = get_newdata_2()
		newdata3 = get_newdata_3()
		newdata4 = get_newdata_4()
		
		template = template_env.get_template('index.html')
		context = {
			'current_time': current_time,
			'user': user,
			'login_url': login_url,
			'logout_url': logout_url,
			'newdata':newdata,
			'newdata1': newdata1,
			'newdata2': newdata2,
			'newdata3': newdata3,
			'newdata4': newdata4,
			

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

class Badges(webapp2.RequestHandler):
    def get(self):
		user = users.get_current_user()
		login_url = users.create_login_url(self.request.path)
		logout_url = users.create_logout_url(self.request.path)
		experience = get_experience()

		template = template_env.get_template('badges.html')
		context = {
			'user': user,
			'login_url': login_url,
			'logout_url': logout_url,
			'experience': experience,
		}
		self.response.out.write(template.render(context))

class DQToday(webapp2.RequestHandler):
    def get(self):
		current_time = datetime.datetime.today().isoweekday()
		user = users.get_current_user()
		login_url = users.create_login_url(self.request.path)
		logout_url = users.create_logout_url(self.request.path)

		newdata = get_newdata()
		newdata1 = get_newdata_1()
		newdata2 = get_newdata_2()
		newdata3 = get_newdata_3()
		newdata4 = get_newdata_4()
		

		template = template_env.get_template('dqtoday.html')
		context = {
			'current_time': current_time,
			'user': user,
			'login_url': login_url,
			'logout_url': logout_url,
			'newdata':newdata,
			'newdata1': newdata1,
			'newdata2': newdata2,
			'newdata3': newdata3,
			'newdata4': newdata4,
		}
		self.response.out.write(template.render(context))	
		
class NewData(ndb.Model):
	dataget = ndb.StringProperty(default=None)
	dataget1 = ndb.StringProperty(default=None)
	dataget2 = ndb.StringProperty(default=None)
	dataget3 = ndb.StringProperty(default=None)
	dataget4 = ndb.StringProperty(default=None)
	experienceget = ndb.IntegerProperty(default=0)
	user = ndb.UserProperty(auto_current_user_add=True)


def get_experience(user_id=None):
	if not user_id:
		user = users.get_current_user()
		if not user:
			return None
		user_id = user.user_id()

	key = ndb.Key('NewData', user_id + 'z')
	experience = key.get()
	if not experience:
		experience = NewData(id=user_id + 'z')
	return experience		

def get_newdata(user_id=None):
	if not user_id:
		user = users.get_current_user()
		if not user:
			return None
		user_id = user.user_id()

	key = ndb.Key('NewData', user_id + 'a')
	newdata = key.get()
	if not newdata:
		newdata = NewData(id=user_id + 'a')
	return newdata		

def get_newdata_1(user_id=None):
	if not user_id:
		user = users.get_current_user()
		if not user:
			return None
		user_id = user.user_id()

	key = ndb.Key('NewData', user_id + 'b')
	newdata1 = key.get()
	if not newdata1:
		newdata1 = NewData(id=user_id + 'b')
	return newdata1	
	
def get_newdata_2(user_id=None):
	if not user_id:
		user = users.get_current_user()
		if not user:
			return None
		user_id = user.user_id()

	key = ndb.Key('NewData', user_id + 'c')
	newdata2 = key.get()
	if not newdata2:
		newdata2 = NewData(id=user_id + 'c')
	return newdata2	

	
def get_newdata_3(user_id=None):
	if not user_id:
		user = users.get_current_user()
		if not user:
			return None
		user_id = user.user_id()

	key = ndb.Key('NewData', user_id + 'd')
	newdata3 = key.get()
	if not newdata3:
		newdata3 = NewData(id=user_id + 'd')
	return newdata3	
	
def get_newdata_4(user_id=None):
	if not user_id:
		user = users.get_current_user()
		if not user:
			return None
		user_id = user.user_id()

	key = ndb.Key('NewData', user_id + 'e')
	newdata4 = key.get()
	if not newdata4:
		newdata4 = NewData(id=user_id + 'e')
	return newdata4	
	
class addtask(webapp2.RequestHandler):
    def get(self):
		current_time = datetime.datetime.now()
		user = users.get_current_user()
		login_url = users.create_login_url(self.request.path)
		logout_url = users.create_logout_url(self.request.path)

		newdata = get_newdata()
		newdata1 = get_newdata_1()
		newdata2 = get_newdata_2()
		newdata3 = get_newdata_3()
		newdata4 = get_newdata_4()

		template = template_env.get_template('addtask.html')
		context = {
			'current_time': current_time,
			'user': user,
			'login_url': login_url,
			'logout_url': logout_url,
			'newdata': newdata,
			'newdata1': newdata1,
			'newdata2': newdata2,
			'newdata3': newdata3,
			'newdata4': newdata4,
		}
		self.response.out.write(template.render(context))

class DataPage(webapp2.RequestHandler):
	def post(self):
		newdata = get_newdata()
		newdata1 = get_newdata_1()
		newdata2 = get_newdata_2()
		newdata3 = get_newdata_3()
		newdata4 = get_newdata_4()
		try:
			dataget = self.request.get('dataget')
			dataget1 = self.request.get('dataget1')
			dataget2 = self.request.get('dataget2')
			dataget3 = self.request.get('dataget3')
			dataget4 = self.request.get('dataget4')
			newdata.dataget = dataget
			newdata1.dataget1 = dataget1
			newdata2.dataget2 = dataget2
			newdata3.dataget3 = dataget3
			newdata4.dataget4 = dataget4
			newdata1.put()
			newdata.put()
			newdata2.put()
			newdata3.put()
			newdata4.put()
		except ValueError:
			#input wrong value
			pass
		self.redirect('/addtask')

class Delete2(webapp2.RequestHandler):
    def post(self):
		newdata2 = get_newdata_2()
		newdata2.key.delete()
		self.redirect('/dqtoday')

class Delete(webapp2.RequestHandler):
    def post(self):
		newdata = get_newdata()
		newdata.key.delete()
		self.redirect('/dqtoday')
		
class Delete1(webapp2.RequestHandler):
    def post(self):
		newdata1 = get_newdata_1()
		newdata1.key.delete()
		self.redirect('/dqtoday')
	    
class Delete3(webapp2.RequestHandler):
    def post(self):
		newdata3 = get_newdata_3()
		newdata3.key.delete()
		self.redirect('/dqtoday')	
	    
class Delete4(webapp2.RequestHandler):
    def post(self):
		newdata1 = get_newdata_4()
		newdata4.key.delete()
		self.redirect('/dqtoday')

application = webapp2.WSGIApplication([('/', MainPage),
                                       ('/home', MainPage),
									   ('/index', Index),
									   ('/about', About),
									   ('/leaderboards', Leaderboards),
									   ('/badges', Badges),
									   ('/dqtoday', DQToday),
									   ('/addtask', addtask),
									   ('/datapage', DataPage),
									   ('/delete2', Delete2),
									   ('/delete1', Delete1),
									   ('/delete3', Delete3),
									   ('/delete4', Delete4),
									   ('/delete', Delete)],
									  debug=True)