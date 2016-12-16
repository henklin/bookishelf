
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
            cur.execute("SELECT username, id, open, info, answer FROM ticket INNER JOIN user ON ticket.userid = user.userid")
        elif typOfTicket == "2":
            cur.execute("SELECT username, id, open, info, answer FROM ticket INNER JOIN user ON ticket.userid = user.userid WHERE open = true")
        elif typOfTicket == "3":
            cur.execute("SELECT username, id, open, info, answer FROM ticket INNER JOIN user ON ticket.userid = user.userid WHERE open = false")
        
        name = cur.fetchone()
        return str(name)
    
    
    def PUT(self, bookid, change):
        
        conn1 =pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)
        cur = conn1.cursor()
        
        cur.execute("SELECT answer FROM ticket WHERE id = %s", (bookid))
        temp = cur.fetchone()
        print (temp[0])
        
        if temp[0] == None:
            wholeChange = change + " "
        else:
            wholeChange = temp[0] + change + " "


        cur.execute("""UPDATE ticket SET answer = %s WHERE id = %s """, (wholeChange, bookid))

        cur.close
        return str('Success!')








