'''
Created on 17 nov. 2016

@author: Henrik
'''
import cherrypy
import random
import string
import sqlite3
import pymysql
from checkout import Checkout
from book import Book
from index import Index
from login import Login
from bookPage import BookPage
from shoppingCart import ShoppingCart
from search import SearchResult
from loginpage import UserLogin
from loginresult import LoginResult
from addShoppingCart import AddShoppingCart

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()



if __name__ == '__main__':
    
    
    
    config = {
    '/': {
        'tools.encode.debug': True,
        'tools.encode.text_only': False,
        'tools.encode.encoding': 'utf8'
    },
}

    cherrypy.tree.mount(
        Checkout(), '/api/checkout',
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
    
    
    cherrypy.tree.mount(
        Index(), '/api',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    
    
    cherrypy.tree.mount(
        UserLogin(), '/api/login',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    
    cherrypy.tree.mount(
        LoginResult(), '/api/loginresult',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    
    cherrypy.tree.mount(
        BookPage(), '/api/bookPage',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    
    cherrypy.tree.mount(
        ShoppingCart(), '/api/shoppingCart',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    
    
    cherrypy.tree.mount(
        AddShoppingCart(), '/api/addshoppingCart',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    
    cherrypy.tree.mount(
        SearchResult(), '/api/search',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )


    cherrypy.engine.start()
    cherrypy.engine.block()
                        
