
'''
    Created on 15 dec. 2016
    
    @author: Alejandro P. Hernandez
    
'''

import cherrypy
import pymysql

class Sales:
    
    
    
    exposed = True
    
    def GET(self):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)
        cur = conn1.cursor()
        allSales = cur.execute("SELECT bookOrder.id, user.username, title, price, date FROM bookOrder INNER JOIN mydb.book on book.id = bookOrder.bookid INNER JOIN mydb.user on bookOrder.userid = user.userid")

        
        allSales = cur.fetchall()
        return str(allSales)
