'''
    Created on 18 nov. 2016
    
    @author: Henrik
    @author: Alejandro P. Hernandez
    
'''

import cherrypy
import pymysql

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()

class Book:
    
    
    
    exposed = True
    
    def GET(self, bookid):
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)
        cur = conn1.cursor()
        cur.execute("SELECT * FROM book WHERE id=%s", (bookid))
        name = cur.fetchone()
        return str(name)
    
    
    
    def POST(self, title, qty, price, image, category, description):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)
        
        cur = conn1.cursor()
        
        cur.execute("INSERT INTO book (title, qty, price, nrSold, image, category, description) VALUES(%s, %s, %s, 0, %s, %s, %s)", (title, qty, price, image, category, description))
        #cur.commit()
        cur.close
        return ('Success!')


    def PUT(self, bookid, valueChange, nrChange):
        
        conn1 =pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)
            
        cur = conn1.cursor()
        
        if nrChange == '1':
            cur.execute ("""UPDATE book SET title = %s WHERE id = %s """ , (valueChange,bookid))
        elif nrChange == '3':
            cur.execute ("""UPDATE book SET price = %s WHERE id = %s """ , (valueChange,bookid))
        elif nrChange == '2':
            cur.execute ("""UPDATE book SET qty = %s WHERE id = %s """ , (valueChange,bookid))
        elif nrChange == '5':
            cur.execute ("""UPDATE book SET image = %s WHERE id = %s """ , (valueChange,bookid))
        elif nrChange == '6':
            cur.execute ("""UPDATE book SET category = %s WHERE id = %s """ , (valueChange,bookid))
        elif nrChange == '7':
            cur.execute ("""UPDATE book SET description = %s WHERE id = %s """ , (valueChange,bookid))

        cur.close
        return str('Success!')

# return ('The book: %s The user: %s' % (dbquery1, dbquery2))

                    
                    
                    
                    
                    
                
