'''
Created on 18 nov. 2016

@author: Henrik
'''
import cherrypy
import pymysql

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()

class Checkout:
    
  

    exposed = True
    
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
    
    def POST(self, bookid, userid):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("SELECT price FROM book WHERE id=(%s)" % bookid )
        
        bookprice = cur.fetchone()
        
        cur.execute("SELECT title FROM book WHERE id=%s", (bookid,))
        
        booktitle = cur.fetchone()
        
        cur.execute("SELECT credit FROM user WHERE userid=%s", (userid,))
        
        usercredit = cur.fetchone()
        
        usercreditint = int(usercredit[0])
        bookpriceint = int(bookprice[0])
        
        newcredit = (usercreditint - bookpriceint)
        
        
        if(bookprice > usercredit):
            return('Not enough credit')
        else:
            cur.execute("UPDATE user SET credit=%s WHERE userid=%s", (newcredit, userid))
            cur.execute("UPDATE book SET qty = qty - 1 WHERE id=%s", (bookid,))
        
        #cur.commit()
        cur.close
        return ('Succes! You have bought %(s)' % booktitle)
        
        
        
       