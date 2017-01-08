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
        
        cur.execute("SELECT bookid from shoppingCart INNER JOIN book on book.id=shoppingCart.bookid INNER JOIN user on user.userid=shoppingCart.userid where shoppingCart.userid=%s" % userid)
        bookIds = cur.fetchall()
        
        cur.close()
        returnString = ""
        i = 0
        for i in range(0, len(shoppingCart)):
            tempStr0 = str(shoppingCart[i]).replace("(", "")
            tempStr1 = str(tempStr0).replace(")", "")
            tempStr2 = str(tempStr1).replace("'", "")
            tempStr3 = str(tempStr2).replace(",", "")
            
            temp = str(bookIds[i]).replace("(", "")
            temp1 = str(temp).replace(")", "")
            temp2 = str(temp1).replace("'", "")
            temp3 = str(temp2).replace(",", "")
            
            
            
            tempHTML = Template("""<td>
<img src="${image}" alt="harry poter" style="width:100px;height:150px;">
<br>
<div align="center">
<form action="http://127.0.0.1:8080/api/deleteshoppingCart" method="post">
<input type="hidden" name="bookid" value="${bookid}">
<input type="hidden" name="theuserid" value="${userid1}">
<input type="submit" value="Remove">
</form>
</div>
</td>
            """)
            returnString += tempHTML.render(image=tempStr3, bookid=temp3, userid1=userid)
            
            
            
        return returnString
            

            
            
            
            
    
  

    exposed = True
    
    def POST(self, userid):
        
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("SELECT price from shoppingCart INNER JOIN book on book.id=shoppingCart.bookid INNER JOIN user on user.userid=shoppingCart.userid where shoppingCart.userid=%s" % userid)

        
        shoppingCartPrice = cur.fetchall()
        
        cur.execute("SELECT credit from shoppingCart INNER JOIN book on book.id=shoppingCart.bookid INNER JOIN user on user.userid=shoppingCart.userid where shoppingCart.userid=%s" % userid)

        
        usercredit = cur.fetchall()
        
        
        temp0 = str(usercredit[0]).replace("(", "")
        temp1 = str(temp0).replace(")", "")
        temp2 = str(temp1).replace("'", "")
        userCredit = str(temp2).replace(",", "")
        
        
        totalPrice = 0
        
        i = 0
        for i in range(0,len(shoppingCartPrice)):
            
            tempStr0 = str(shoppingCartPrice[i]).replace("(", "")
            tempStr1 = str(tempStr0).replace(")", "")
            tempStr2 = str(tempStr1).replace("'", "")
            tempStr3 = str(tempStr2).replace(",", "")
            totalPrice+=int(tempStr3)
        
        
        cur.close()
        
        newCredit = int(userCredit) - totalPrice
        
        creditString = ""
        
        if(newCredit < 0):
            creditString = "Not enough credit"
        else:
            creditString = ("Credit after purchase: %s" % newCredit)
        
        finalString = ShoppingCart.StringGen(self, userid)
      
        return ("""
        <!DOCTYPE html>
<html>
<head>
<title>Buy Book</title>
</head>
<body background ="http://www.mikelavere.com/wp-content/uploads/2015/03/self-improvement-books.jpg"  text=#0099cc>

            
	<table>
	<tr><td>
	<form method=post action="http://localhost:8080/api/">
	<input type="hidden" name="userid" value="%s">
	<button>
	<img src="http://images.clipartpanda.com/embryo-clipart-book17.png" height="50" width="100">
	</button>
	</form>
	</td>
	<td width="1000" align="right">
	<h2><a href="http://localhost:8080/api/logoutpage"><font size=15 face="Consolas" color="#EBF5FB">Logout</font></a></h2>
	</td></tr>
	</table>

<br><br><br>
<h2>
<div align= "center" >
Shopping cart
</div>
</h2>
<table align="center"><tr>
%s
</tr></table>
<br><br>
<div align="center">
<p><b>Total amount: %s kr</b></p>
<p><b>Your credit: %s kr</b></p>
<p><b>%s kr</b></p>
<br><br>
</div>
<br><br>

<table align="center">
<tr><td>
<form method="post" action="http://127.0.0.1:8080/api/checkout">
<input type="hidden" name="userid" value="%s">
<input type="submit" value="Check Out">
</form>
</td>
</tr>
<tr><td>
<form method="post" action="http://127.0.0.1:8080/api/credit">
<input type="hidden" name="userid" value="%s">
<input type="submit" value="Out of credits?">
</form>
</td></tr>
</table>

</div>

</body>
</html> """ % (userid, finalString, totalPrice, userCredit, creditString, userid, userid))
    
    
