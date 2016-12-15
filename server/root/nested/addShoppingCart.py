'''
Created on 18 nov. 2016

@author: Henrik
'''
import cherrypy
import pymysql
from mako.template import Template

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()

class AddShoppingCart:
    
    
    exposed = True
    
    
    def POST(self, bookid, userid):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("SELECT qty FROM book WHERE id=%s" % (bookid) )
        
        qty = cur.fetchone()
        
        
        
        if(qty[0] < 0):
            return('Out of stock!')
        
        cur.execute("INSERT INTO shoppingCart (userid, bookid) VALUES(%s,%s)" % (userid, bookid) )
        
        
        
        
        
        cur.close()
        
        
        
        return ("""<!DOCTYPE html>
<html>
<head>
<style>
body{
      background-image:url("https://images.pexels.com/photos/175994/pexels-photo-175994.jpeg?w=940&h=650&auto=compress&cs=tinysrgb");
      background-size: 2700px 2000px;
      background-repeat: no-repeat;
      background-attachment: fixed;
      background-position: center;
}
</style>
</head>
<body>

<h1> <i> <center> <font size="10"> <p style="margin-top: 10cm;"> Book Sucessfully added into cart </p></font> </center> </i></h1>
<a href="" target="_self"> <center> <font size="10"> Continue Shopping </font> </center> </a>
</body>
</html>""")