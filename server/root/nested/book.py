'''
    Created on 21 nov. 2016
    
    @author: Henrik
    '''


'''
    Created on 18 nov. 2016
    
    @author: Henrik
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
        cur.execute("SELECT * FROM book where id=%s", (bookid,))
    
        name = cur.fetchone()
        return str(name)
    
    
    
    def POST(self, id, title, qty, price, image):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)
        
        cur = conn1.cursor()
        
        cur.execute("INSERT INTO book VALUES(%s, %s, %s, %s, 0, %s)", (id, title, qty, price,image))
        #cur.commit()
        cur.close
        return ('Success!')

# return ('The book: %s The user: %s' % (dbquery1, dbquery2))





