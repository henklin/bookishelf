
'''
    Created on 15 dec. 2016
    
    @author: Alejandro P. Hernandez
    
'''

import cherrypy
import pymysql

class Tickets:
    
    
    
    exposed = True
    
    def GET(self, typOfTicket):
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)
        cur = conn1.cursor()
        
        if typOfTicket == "1":
            cur.execute("SELECT * FROM ticket")
        elif typOfTicket == "2":
            cur.execute("SELECT * FROM ticket WHERE open = true")
        elif typOfTicket == "3":
            cur.execute("SELECT * FROM ticket WHERE open = false")
        
        cur.execute("SELECT * FROM book WHERE id=%s", (bookid))
        name = cur.fetchone()
        return str(name)
    
    
    
    def POST(self, title, qty, price, image, category, description):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)
        cur = conn1.cursor()
        
        #PUT CODE HERE
        
        cur.close
        return ('Success!')
    
    
    def PUT(self, bookid, valueChange, nrChange):
        
        conn1 =pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)
        cur = conn1.cursor()

        #PUT CODE HERE

        cur.close
        return str('Success!')








