'''
Created on 21 nov. 2016

@author: Henrik
'''


'''
Created on 18 nov. 2016

@author: Henrik
'''
import cherrypy
import pymysql

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()

class Book:
    
     
        
    exposed = True
    
    def GET(self, bookid):
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)
        cur = conn1.cursor()
        cur.execute("SELECT title FROM book where id=%s", (bookid,))
        name = cur.fetchone()
        return """
        <html>

<head>
<title>Bookishelf</title>
</head>

<body background="Profile.jpg" text=#D6EAF8>

    
    <a href="Homepage.html">
    <img src="http://e2a.solapo.com/img/i22639.jpg" height="50" width="100">
    </a>

    <h1>
    <font face="Century Gothic" color="#FCF3CF">
    &nbsp LOGIN TO ENTER THE FUTURE
    </font>
    </h1>
    <font size=5 face="Consolas" color="#FADBD8">
    <hr width=50% align="left">
    <br><br><br>

    <font color="#EBF5FB"><p align="center">Enter your details to Login</font>

    <form action="http://foo.com" method="post">
    <input name="bookid" value="1">
    <input name="userid" value="1">
    <button>Send my greetings</button>
</form>

    <tr><td>
    User-ID:</td><td align="left"><input type="text" name="bookid" maxlength="32" size="16">
    </td></tr>

    <tr><td>
    Password:</td><td align="left"><input type="password" name="userid">
    </td></tr>

    <tr><td align="center"><input type="submit" value="Login"></td></tr>

    </table>

    </form>

    <br><br>
    <p align="center"><font face="Century Gothic" color="#2E86C1">
    Not a member yet?
    </font>
    <a href=Register.html><font color="#EBF5FB">Sign Up</font></a>

    </font>
</body>
<br><br><br>
<font face="Century Gothic" color="#1A5276">
<hr align="center" width="50%">
<p align="center">&copy2016&nbsp Bookishelf.com
</font>

</html>
"""
        
    def POST(self, id, title, qty, price):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)
        
        

        cur = conn1.cursor()
        
        cur.execute("INSERT INTO book VALUES(%s, %s, %s, %s)", (id, title, qty, price))
        
                
        

        
        
       
        
        #cur.commit()
        cur.close
        return ('Success!')
        
       # return ('The book: %s The user: %s' % (dbquery1, dbquery2))