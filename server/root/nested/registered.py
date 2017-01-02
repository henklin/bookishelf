import os, os.path
import random
import string
import pymysql
import cherrypy
import requests


class Register:

    exposed = True
    
    def POST(self, firstname, lastname, username, email, password, repassword):

        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        try:
            cur.execute("INSERT INTO user (firstname, lastname, username, email, password) VALUES ('%s', '%s', '%s', '%s', '%s')" % (firstname, lastname, username, email, password))
        except:
            r = requests.get("http://127.0.0.1:8080/api/register")
            return (r.text)

        cur.close

        conn2 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur2 = conn2.cursor()

        cur2.execute("SELECT userid FROM user WHERE username=%s", username)

        userid=cur2.fetchone()

        return ("""
        <!DOCTYPE html>

<head>
<title>Bookishelf</title>
</head>

<body background="http://wallpaperus.org/wallpapers/03/122/books-1920x1080-wallpaper-1711426.jpg" text=#D6EAF8>
	

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

	<h1>
	<font face="Century Gothic" color="#FCF3CF">
	&nbsp Hello %s
	</font>
	</h1>
	<font size="16" face="Consolas" color="#2E86C1">
	<hr width=50px align="left">

	<font color="#EBF5FB" size="20"><p align="center">You have been successfully registered on our website!!<br>Thank you joining us!!!</font>



</font>
</form>

<br><br>

</body>
<br><br><br>
<font face="Century Gothic" color="#1A5276">
<hr align="center" width="50px">
<p align="center">&copy2016&nbsp Bookishelf.com
</font>

        </html>""" % (userid, firstname))
