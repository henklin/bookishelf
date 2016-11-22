'''
Created on 17 nov. 2016

@author: Henrik
'''
import cherrypy
import random
import string
import sqlite3
import pymysql
from books import Books
from book import Book

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()



if __name__ == '__main__':

    cherrypy.tree.mount(
        Books(), '/api/books',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    
    cherrypy.tree.mount(
        Book(), '/api/book',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()
                        
