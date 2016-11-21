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
    
    def POST(self, bookid, userid):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("SELECT price FROM book WHERE id=%s", (bookid,))
        
        bookprice = cur.fetchone()
        
        cur.execute("SELECT credit FROM user WHERE userid=%s", (userid,))
        
        usercredit = cur.fetchone()
        
        usercreditint = int(usercredit[0])
        bookpriceint = int(bookprice[0])
        
        newcredit = (usercreditint - bookpriceint)
        
        
        if(bookprice > usercredit):
            return('Not enough credit')
        else:
            cur.execute("UPDATE user SET credit=%s WHERE userid=%s", (newcredit, userid))
            cur.execute("UPDATE book SET qty = qty - 1 WHERE id=%s", (bookid,))
        
        #cur.commit()
        cur.close
        return ('Success!')
        
       # return ('The book: %s The user: %s' % (dbquery1, dbquery2))