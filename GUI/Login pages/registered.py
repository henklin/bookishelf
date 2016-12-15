import os, os.path
import random
import string
import pymysql
import cherrypy


class Registeration:

    exposed = True
    
    def POST(self, firstname, lastname, address, email, usern, upassword, repassword):

        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("INSERT INTO userinfo SET (FirstName, LastName, Address, Email, username, userpassword) VALUES (%s, %s, %s, %s, %s, %s)" % (firstname, lastname, address, email, usern, upassword))

        cur.close

        return ("""
        <!DOCTYPE html>

<head>
<title>Bookishelf</title>
</head>

<body background="http://wallpaperus.org/wallpapers/03/122/books-1920x1080-wallpaper-1711426.jpg" text=#D6EAF8>
	
	
	<img src="http://images.clipartpanda.com/embryo-clipart-book17.png" height="50" width="100">

	<h1>
	<font face="Century Gothic" color="#FCF3CF">
	&nbsp Hello %s
	</font>
	</h1>
	<font size="16" face="Consolas" color="#2E86C1">
	<hr width=50px align="left">

	<font color="#EBF5FB" size="20"><p align="center">You have been successfully registered on our website!!<br>Thank you joining us!!!</font>


<table align="center">
<tr>
<th colspan=5 align="center">Trending Books</th>
<tr></tr></tr>
<tr>
<td><a href="book1.html">
<img height="300" width="200" src="%s" alt="book1">
</a></td>

<td><a href="book2.html">
<img height="300" width="200" src="" alt="book2">
</a></td>

<td><a href="book3.html">
<img height="300" width="200" src="" alt="book3">
</a></td>

<td><a href="book4.html">
<img height="300" width="200" src="" alt="book4">
</a></td>

<td><a href="book5.html">
<img height="300" width="200" src="" alt="book5">
</a></td>

</tr>

</table>
</font>
</form>

<br><br>

</body>
<br><br><br>
<font face="Century Gothic" color="#1A5276">
<hr align="center" width="50px">
<p align="center">&copy2016&nbsp Bookishelf.com
</font>

        </html>""" % (firstname))
