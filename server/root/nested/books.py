'''
Created on 18 nov. 2016

@author: Henrik
'''
import cherrypy
import pymysql

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()

class Books:

    exposed = True
    
    def GET(self):
        return ('Hello');
    
    def POST(self, id):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb')

        cur = conn1.cursor()
        
        cur.execute("SELECT booktitle FROM books WHERE bookid=%s", (id,))
        
        dbquery = cur.fetchone()
        #cur.commit()
        cur.close
        
        return ('The test: %s' % dbquery)