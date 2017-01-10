
'''
    Created on 15 dec. 2016
    
    @author: Alejandro P. Hernandez
    
'''

import cherrypy
import pymysql

class TotalSales:
    
    
    
    exposed = True
    
    def GET(self):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)
        cur = conn1.cursor()
        
        totSales = cur.execute("SELECT sum(price) FROM mydb.bookOrder INNER JOIN mydb.book WHERE bookOrder.bookid = book.id")
        
        
        allSales = cur.fetchall()
        return str(allSales)
