import webapp2
import models

class PrefsPage(webapp2.RequestHandler):
	def post(self):
		userprefs = models.get_userprefs()
		try:
			tz_offset = float(self.request.get('tz_offset'))
			userprefs.tz_offset = tz_offset
			userprefs.put()
		except ValueError:
			#input wrong value
			pass
		self.redirect('/')

class DataPage(webapp2.RequestHandler):
	def post(self):
		newdata = models.get_newdata()
		try:
			dataget = str(self.request.get('dataget'))
			newdata.dataget = dataget
			newdata.put()
		except ValueError:
			#input wrong value
			pass
<<<<<<< HEAD
		self.redirect('/')

application = webapp2.WSGIApplication([('/prefs', PrefsPage)],
=======
		self.redirect('/addtask')

application = webapp2.WSGIApplication([('/prefs', PrefsPage),
                                        ('/datapage', DataPage)],
>>>>>>> da63c2a702e7167543de9b8f55bdd281a373fe67
	                                  debug=True)