'''
Created on 18 nov. 2016

@author: Henrik
'''
import cherrypy
import pymysql
from mako.template import Template

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()

class Checkout:
    
  

    exposed = True
    
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
            tempHTML = Template("""<img src="${image}" style="width:100px;height:150px;">
            """)
            returnString += tempHTML.render(image=tempStr3)
            
        return returnString
    
    def GET(self, bookid, userid):
        
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("INSERT INTO shoppingCart VALUES(1, %s, %s)" % (bookid, userid))
        
        cur.execute("SELECT price FROM book WHERE id=(%s)" % bookid )
        
        bookprice = cur.fetchone()
        
        cur.execute("SELECT title FROM book WHERE id=%s", (bookid,))
        
        booktitle = cur.fetchone()
        
        cur.execute("SELECT credit FROM user WHERE userid=%s", (userid,))
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
%s
</div>
</h2>
<div  style="height: 50; width: 300px;"> </div>
<div align="center">
<img src="http://cdn.collider.com/wp-content/uploads/2015/12/harry-potter-olly-moss-prisoner-of-azkaban.png"  alt="harry poter" style="width:304px;height:228px;">
</div>
<br><br>
<div align="center">
<p><b>Amount: %s</b></p><br><br>
</div>
<br><br>
<form action="conf.html">

<table align="center">
<tr><td>
<button type="submit" onclick="alert('Confirmed')" >
Check Out
</button>
</td>
</tr>
</table>

</div>
</form>
</body>
</html> """ % (booktitle[0], bookprice[0]))
    
    def POST(self, userid):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("SELECT price from shoppingCart INNER JOIN book on book.id=shoppingCart.bookid INNER JOIN user on user.userid=shoppingCart.userid where shoppingCart.userid=%s" % userid)

        shoppingCartPrice = cur.fetchall()
        totalPrice = 0
        
        i = 0
        for i in range(0,len(shoppingCartPrice)):
            
            priceStr0 = str(shoppingCartPrice[i]).replace("(", "")
            priceStr1 = str(priceStr0).replace(")", "")
            priceStr2 = str(priceStr1).replace("'", "")
            priceStr3 = str(priceStr2).replace(",", "")
            totalPrice+=int(priceStr3)
            
        shoppingCartPrice = cur.fetchall()
            
        cur.execute("SELECT book.id from shoppingCart INNER JOIN book on book.id=shoppingCart.bookid INNER JOIN user on user.userid=shoppingCart.userid where shoppingCart.userid=%s" % userid)

        bookIds = cur.fetchall()
        bookIdsOk = [None] * len(bookIds)
        i = 0
        for i in range(0,len(bookIds)):
            ##print("AHHEHEHEHEHHEHEH %s" % bookIds[0])
            ##tempStr0 = str(bookIds[i]).replace("(", "")
            ##tempStr1 = str(priceStr0).replace(")", "")
            ##tempStr2 = str(priceStr1).replace("'", "")
            ##tempStr3 = str(priceStr2).replace(",", "")
            ##print("ASDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA %s" % tempStr3)
            cur.execute("SELECT qty FROM book WHERE id=%s" % bookIds[i])
            ##bookIdsOk[i] = tempStr3
            qty = cur.fetchone()
            cur.execute("SELECT qty FROM book WHERE id=%s" % bookIds[i])
            tempQty = cur.fetchone()
            tempStr0 = str(tempQty[0]).replace("(", "")
            tempStr1 = str(priceStr0).replace(")", "")
            tempStr2 = str(priceStr1).replace("'", "")
            tempStr3 = str(priceStr2).replace(",", "")
            
            
            if(int(tempStr3) < 0):
                return("OUT OF BOOKS")
            
            
        
            
        
        
        cur.execute("SELECT credit FROM user WHERE userid=%s", (userid,))
        
        usercredit = cur.fetchone()
        
        usercreditint = int(usercredit[0])
        
        
        newcredit = (usercreditint - totalPrice)
        
        finalString = Checkout.StringGen(self, 1)
        if(totalPrice > usercreditint):
            return('Not enough credit')
        else:
            x = 0
            cur.execute("UPDATE user SET credit=%s WHERE userid=%s", (newcredit, userid))
            for x in range(0,len(bookIds)):
                cur.execute("UPDATE book SET qty = qty - 1 WHERE id=%s", (bookIds[x],))
                cur.execute("UPDATE book SET nrSold = nrSold + 1 WHERE id=%s", (bookIds[x],))
            cur.execute("DELETE FROM shoppingCart where userid=%s" % userid)
            
        #cur.commit()
        
        
        
        cur.close
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
You have placed your order, thank you!
</div>
</h2>
<div  style="height: 50; width: 300px;"> </div>
<div align="center">
%s
</div>
<br><br>
<div align="center">
<p><b>Order value: %s kr</b></p><br><br>
</div>
<br><br>

<table align="center">
<tr><td>
<form method="get" action="http://127.0.0.1:8080/api/">
<input type="submit" value="Continue shopping">
</form>
</td>
</tr>
</table>

</div>

</body>
</html> """ % (finalString, totalPrice))
        
        
        
       