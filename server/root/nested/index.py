'''
Created on 18 nov. 2016

@author: Henrik
'''
import cherrypy
import pymysql

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()

class Index:

    exposed = True
    
    def GET(self):
        return """
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
    <hr width=50% align="left">

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
<input type="hidden" name="bookid" value="1">
<button>
<img height="300" width="200" src="http://www.images-booknode.com/book_cover/2574/full/le-jour-ou-j-ai-voulu-devenir-populaire-2573812.jpg" alt="book1">
</button>
</form></td>

<td><a href="book2.html">
<img height="300" width="200" src="https://s-media-cache-ak0.pinimg.com/736x/6b/cf/4f/6bcf4fb135c5a3e68af6b3cef6f843c0.jpg" alt="book2">
</a></td>

<td><a href="book3.html">
<img height="300" width="200" src="https://images-na.ssl-images-amazon.com/images/I/51leqJMvzZL._SX258_BO1,204,203,200_.jpg" alt="book3">
</a></td>

<td><a href="book4.html">
<img height="300" width="200" src="https://www.josephprince.org/crm/images/crm_resources/9781606830093.png" alt="book4">
</a></td>

<td><a href="book5.html">
<img height="300" width="200" src="http://esoftwiz.com/wp-content/uploads/2013/09/David-Copperfield-%E2%80%94-Charles-Dickens.jpg" alt="book5">
</a></td>

</tr>

<form method="get" action="http://127.0.0.1:8080/api/checkout">

<tr>
<td align="center">
<input type="hidden" name="bookid" value=1>
<input type="hidden" name="userid" value=1>
<input type="submit" value="Buy">
</td>


</tr>

</table>
</font>
</form>

    <br><br>
    <p align="center"><font face="Century Gothic" color="#FADBD8">
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

        </html>"""
    
  
        
      