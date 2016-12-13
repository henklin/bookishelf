'''
Created on 5 dec. 2016

@author: Abigail
'''

import cherrypy
import random
import string
import sqlite3
import pymysql
from loginpage import UserLoginPage
from loginresult import LoginResultPage
from loginregister import RegisterPage
from search import SearchResult
from bookihomepage import HomePage


if __name__ == '__main__':
    
    
    
    config = {
    '/': {
        'tools.encode.debug': True,
        'tools.encode.text_only': False,
        'tools.encode.encoding': 'utf8'
    },
}

    cherrypy.tree.mount(
        UserLoginPage(), '/api/loginpage',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    
    cherrypy.tree.mount(
        LoginResultPage(), '/api/loginresult',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.tree.mount(
        RegisterPage(), '/api/loginregister',
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

    cherrypy.tree.mount(
        HomePage(), '/api/bookihomepage',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    
    
    cherrypy.engine.start()
    cherrypy.engine.block()
                        
