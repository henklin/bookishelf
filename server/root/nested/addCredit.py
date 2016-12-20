'''
Created on 18 nov. 2016

@author: Henrik
'''
import cherrypy
import pymysqlimport requests
from mako.template import Template

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()

class AddCredit:
    
    
    exposed = True
    
    
    def POST(self, userid, amount):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("SELECT qty FROM user WHERE userid=%s " % (bookid) )        qty = cur.fetchone()                        temp0 = str(bookIds[0]).replace("(", "")        temp1 = str(temp0).replace(")", "")        temp2 = str(temp1).replace("'", "")        temp3 = str(temp2).replace(",", "")                        newCredit = int(temp3) + int(amount)                        cur.execute("UPDATE user SET credit=%s WHERE userid=%s"  (newCredit, userid))                cur.close()            r = requests.post("http://127.0.0.1:8080/api/shoppingCart", data={'userid': theuserid})        return (r.text)   
        cur.close()                
        
        