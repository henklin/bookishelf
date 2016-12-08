'''
Created on 18 nov. 2016

@author: Henrik
'''
import cherrypy
import pymysql
from mako.template import Template

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()

class ShoppingCart:
    
    def StringGen(self, userid):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("SELECT image from shoppingCart INNER JOIN book on book.id=shoppingCart.bookid INNER JOIN user on user.userid=shoppingCart.userid where shoppingCart.userid=%s" % userid)
        shoppingCart = cur.fetchall()
        cur.close()
        returnString = ""
        i = 0
        for i in range(0, len(shoppingCart)):
            tempStr0 = str(shoppingCart[i]).replace("(", "")
            tempStr1 = str(tempStr0).replace(")", "")
            tempStr2 = str(tempStr1).replace("'", "")
            tempStr3 = str(tempStr2).replace(",", "")
            tempHTML = Template("""<img src="${image}" alt="harry poter" style="width:100px;height:150px;">
            """)
            returnString += tempHTML.render(image=tempStr3)
            
        return returnString
            

            
            
            
            
    
  

    exposed = True
    
    def GET(self, userid):
        
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("SELECT price from shoppingCart INNER JOIN book on book.id=shoppingCart.bookid INNER JOIN user on user.userid=shoppingCart.userid where shoppingCart.userid=%s" % userid)

        
        shoppingCartPrice = cur.fetchall()
        totalPrice = 0
        
        i = 0
        for i in range(0,len(shoppingCartPrice)):
            
            tempStr0 = str(shoppingCartPrice[i]).replace("(", "")
            tempStr1 = str(tempStr0).replace(")", "")
            tempStr2 = str(tempStr1).replace("'", "")
            tempStr3 = str(tempStr2).replace(",", "")
            totalPrice+=int(tempStr3)
        
        
        cur.close()
        
        finalString = ShoppingCart.StringGen(self, userid)
      
        return ("""
        <!DOCTYPE html>
<html>
<head>
<title>Buy Book</title>
</head>
<body background ="http://www.mikelavere.com/wp-content/uploads/2015/03/self-improvement-books.jpg"  text=#0099cc>
<br><br><br>
<h2>
<div align= "center" >
Shopping cart
</div>
</h2>
<div  style="height: 50; width: 300px;"> </div>
<div align="center">
%s
</div>
<br><br>
<div align="center">
<p><b>Total amount: %s kr</b></p><br><br>
</div>
<br><br>

<table align="center">
<tr><td>
<form method="post" action="http://127.0.0.1:8080/api/checkout">
<input type="hidden" name="userid" value="1">
<input type="submit" value="Check Out">
</form>
</td>
</tr>
</table>

</div>

</body>
</html> """ % (finalString, totalPrice))
    
    def POST(self, bookid, userid):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("SELECT qty FROM book WHERE id=%s" % (bookid) )
        
        qty = cur.fetchone()
        
        
        
        if(qty[0] < 0):
            return('Out of stock!')
        
        cur.execute("INSERT INTO shoppingCart (userid, bookid) VALUES(%s,%s)" % (userid, bookid) )
        
        
        
        
        
        cur.close()
        
        
        
       