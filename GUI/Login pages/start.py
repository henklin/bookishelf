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
from registered import Registeration
from search import SearchResult
from bookihomepage import HomePage
from logoutpage import Logout
from ticket import TicketPage
from ticketanswer import TicketAnswerPage


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
        Registeration(), '/api/registered',
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

    cherrypy.tree.mount(
        Logout(), '/api/logoutpage',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    
    cherrypy.tree.mount(
        TicketPage(), '/api/ticket',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.tree.mount(
        TicketAnswerPage(), '/api/ticketanswer',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    
    cherrypy.engine.start()
    cherrypy.engine.block()
                        
