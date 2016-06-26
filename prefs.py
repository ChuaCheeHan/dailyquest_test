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
		self.redirect('/')

application = webapp2.WSGIApplication([('/prefs', PrefsPage)],
	                                  debug=True)