# coding: utf-8

import webapp2
import urllib2
import httplib



class PageHandler(webapp2.RequestHandler):
	def get(self, page=None):
		conn = httplib.HTTPSConnection('www.google.cn', 443)
		conn.request('GET', 'https://code.google.com/p/'+page, headers = {"Host": "code.google.com"})
		res = conn.getresponse()
		self.response.write(res.read())


app = webapp2.WSGIApplication([
	(r'/p/(.*)', PageHandler)
], debug=True)

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
