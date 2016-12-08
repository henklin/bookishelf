'''
    Created on 05 dec. 2016
    
    @author: Alejandro
    '''

import cherrypy
import pymysql

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()

class AllBooks:
    
    
    
    exposed = True
    
    def GET(self):
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)
        cur = conn1.cursor()
        cur.execute("SELECT * FROM book")
    
        name = cur.fetchall()
        return str(name)





