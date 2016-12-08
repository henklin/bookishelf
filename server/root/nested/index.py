'''
Created on 18 nov. 2016

@author: Henrik
'''
import cherrypy
import pymysql
import string

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()

class Index:

    exposed = True
    
    def GET(self):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        
        cur.execute("SELECT image FROM book ORDER BY nrSold, id desc limit 5")
        
        images = cur.fetchall()
        
        imageList = [None] * 5
        i = 0
        for i in range(0,5):
            
            imgStr0 = str(images[i]).replace("(", "")
            imgStr1 = str(imgStr0).replace(")", "")
            imgStr2 = str(imgStr1).replace("'", "")
            imgStr3 = str(imgStr2).replace(",", "")
            imageList[i] = imgStr3
            




       

        
        
        idsList = [None] * 5

        
        cur.execute("SELECT id FROM book ORDER BY nrSold, id desc limit 5")
        
        ids = cur.fetchall()
        
        
        
        
        cur.close()
        i = 0
        for i in range(0,5):
            
            idsStr0 = str(ids[i]).replace("(", "")
            idsStr1 = str(idsStr0).replace(")", "")
            idsStr2 = str(idsStr1).replace("'", "")
            idsStr3 = str(idsStr2).replace(",", "")
            idsList[i] = idsStr3
        
        
        
        
        
        
        
        
        return ("""
        <html>

<head>
<title>Bookishelf</title>
</head>

<body background="http://wallpaperus.org/wallpapers/03/122/books-1920x1080-wallpaper-1711426.jpg" text=#D6EAF8>
    

    <table>
    <tr><td>
    <img src="http://images.clipartpanda.com/embryo-clipart-book17.png" height="100" width="300">
    </td>
    <td width="1000" align="right">
    <h2><a href="Login.html"><font size=30 face="Consolas" color="#EBF5FB">Login</font></a></h2>
    </td></tr>
    </table>

    <h1>
    <font face="Century Gothic" color="#FCF3CF">
    &nbsp LOGIN TO ENTER THE FUTURE
    </font>
    </h1>
    <font size="16" face="Consolas" color="#2E86C1">
    <hr width=50 align="left">

    <font color="#EBF5FB" size="20"><p align="center">Start by searching your Favorite Book</font>

    <form action="http://localhost:8080/Bookishelf/search.jsp" method="get">
    <table align="center">

    <tr><td>
    Search:</td><td align="left"><input type="text" name="user" maxlength="32" size="16">
    </td><td>
    <select name="Genre">
      <option value="Fiction">Fiction</option>
      <option value="Horror">Horror</option>
      <option value="Thriller">Thriller</option>
      <option value="Romance">Romance</option>
    </select>
    </td>

    <td><input type="submit" value="Search"></td></tr>

    </table>

    </form>

<br>
<font face="Century Gothic" color="#FADBD8">
<table align="center">
<tr>
<th colspan=5 align="center">Trending Books</th>
<tr></tr></tr>
<tr>
<td><form method="get" action="http://127.0.0.1:8080/api/bookPage">
<input type="hidden" name="bookid" value="%s">
<button>
<img height="300" width="200" src="%s" alt="book1">
</button>
</form></td>

<td><form method="get" action="http://127.0.0.1:8080/api/bookPage">
<input type="hidden" name="bookid" value="%s">
<button>
<img height="300" width="200" src="%s" alt="book1">
</button>
</form></td>

<td><form method="get" action="http://127.0.0.1:8080/api/bookPage">
<input type="hidden" name="bookid" value="%s">
<button>
<img height="300" width="200" src="%s" alt="book1">
</button>
</form></td>

<td><form method="get" action="http://127.0.0.1:8080/api/bookPage">
<input type="hidden" name="bookid" value="%s">
<button>
<img height="300" width="200" src="%s" alt="book1">
</button>
</form></td>

<td><form method="get" action="http://127.0.0.1:8080/api/bookPage">
<input type="hidden" name="bookid" value="%s">
<button>
<img height="300" width="200" src="%s" alt="book1">
</button>
</form></td>

</tr>

<tr>

<form method="post" action="http://127.0.0.1:8080/api/shoppingCart">

<td align="center">
<input type="hidden" name="bookid" value=%s>
<input type="hidden" name="userid" value=1>
<input type="submit" value="Add to cart">
</td>

</form>

<form method="post" action="http://127.0.0.1:8080/api/shoppingCart">

<td align="center">
<input type="hidden" name="bookid" value=%s>
<input type="hidden" name="userid" value=1>
<input type="submit" value="Add to cart">
</td>

</form>

<form method="post" action="http://127.0.0.1:8080/api/shoppingCart">

<td align="center">
<input type="hidden" name="bookid" value=%s>
<input type="hidden" name="userid" value=1>
<input type="submit" value="Add to cart">
</td>

</form>

<form method="post" action="http://127.0.0.1:8080/api/shoppingCart">

<td align="center">
<input type="hidden" name="bookid" value=%s>
<input type="hidden" name="userid" value=1>
<input type="submit" value="Add to cart">
</td>

</form>


<form method="post" action="http://127.0.0.1:8080/api/shoppingCart">

<td align="center">
<input type="hidden" name="bookid" value=%s>
<input type="hidden" name="userid" value=1>
<input type="submit" value="Add to cart">
</td>
</form>


</tr>




</table>
</font>

    <br><br>
    <p align="center"><font face="Century Gothic" color="#FADBD8">
    Not a member yet?
    </font>
    <a href=Register.html><font color="#EBF5FB">Sign Up</font></a>

    </font>
</body>
<br><br><br>
<font face="Century Gothic" color="#1A5276">
<hr align="center" width="50">
<p align="center">&copy2016&nbsp Bookishelf.com
</font>

        </html>""" % (idsList[0], imageList[0], idsList[1], imageList[1], idsList[2], imageList[2], idsList[3], imageList[3], idsList[4], imageList[4], idsList[0], idsList[1], idsList[2], idsList[3], idsList[4]))
    
  
        
      