'''
Created on 18 nov. 2016

@author: Henrik
'''
import cherrypy
import pymysql
from mako.template import Template

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()

class AddCredit:
    
    
    exposed = True
    
    
    def POST(self, userid, amount):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("SELECT qty FROM user WHERE userid=%s " % (bookid) )
        cur.close()
        
        