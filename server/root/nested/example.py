'''
Created on 17 nov. 2016

@author: Henrik
'''
import cherrypy
import random
import string


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))
if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
                        
