'''
Created on 18 nov. 2016

@author: Henrik
'''
import cherrypy
import pymysql

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()

class Login:

    exposed = True
    
    def GET(self):
        return ('Hello');
    
    def POST(self, username, password):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        
        cur.execute("SELECT username, password FROM user WHERE username=%s", (username,))
        
        usercredit = cur.fetchone()
        
       
        
   
        
            
        
        #cur.commit()
        cur.close
        return usercredit
        
       # return ('The book: %s The user: %s' % (dbquery1, dbquery2))