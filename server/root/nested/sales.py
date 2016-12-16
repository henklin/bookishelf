
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
        cur.execute("SELECT order.id, user.username, title, price, date FROM mydb.order INNER JOIN mydb.book on book.id = order.bookid INNER JOIN mydb.user on order.userid = user.userid")
        
        name = cur.fetchall()
        return str(name)
