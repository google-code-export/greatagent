# coding: utf-8

import webapp2
import urllib2



class PageHandler(webapp2.RequestHandler):
	def get(self, page=None):
		self.response.write(urllib2.urlopen('https://code.google.com/p/'+page).read())


app = webapp2.WSGIApplication([
	# (r'/api', ApiHandler),
	(r'/p/(.*)', PageHandler)
], debug=True)

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
