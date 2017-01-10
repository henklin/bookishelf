'''
Created on 18 nov. 2016

@author: Henrik
'''
import cherrypy
import pymysqlimport requests
from mako.template import Template

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()

class DeleteShoppingCart:
    
    
    exposed = True
    
    
    def POST(self, bookid, theuserid):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("DELETE FROM shoppingCart WHERE bookid=%s AND userid=%s " % (bookid, theuserid) )                cur.close()            r = requests.post("http://127.0.0.1:8080/api/shoppingCart", data={'userid': theuserid})        return (r.text)   
        cur.close()                
        
        