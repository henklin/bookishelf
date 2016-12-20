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
}input[type=submit] {    width: 300px;    height: 45px;    padding: 12px 20px;    margin: 8px 0;    box-sizing: border-box;    font-size: 24px;    font-family: Consolas;    border-radius:28px;    border:1px solid #EBF5FB;    display:inline-block;}
</style>
</head>
<body>

<h1> <i> <center> <font size="10"> <p style="margin-top: 10cm;"> Book Sucessfully added into cart </p></font> </center> </i></h1>
<form action="http://127.0.0.1:8080/api/" method=post><input type=hidden name="userid" value="%s"><center> <font size="10"> <input type=submit value="Continue Shopping"></font> </center></form>
</body>
</html>""" % (userid))