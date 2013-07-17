# coding: utf-8

import webapp2
import urllib2
import httplib



class PageHandler(webapp2.RequestHandler):
	def get(self, page=None):
		self.response.write(urllib2.urlopen('https://github.com/wwqgtxx/goagent_monitor').read())


app = webapp2.WSGIApplication([
	(r'/', PageHandler)
], debug=True)

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
