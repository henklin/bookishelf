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
            cur.execute("INSERT INTO user (firstname, lastname, username, email, password, credit) VALUES ('%s', '%s', '%s', '%s', '%s', 0)" % (firstname, lastname, username, email, password))
        except:
            r = requests.get("http://127.0.0.1:8080/api/register")
            return (r.text)

        cur.close



        return ("""
        <!DOCTYPE html>

<head>
<title>Bookishelf</title>
</head>

<body background="http://wallpaperus.org/wallpapers/03/122/books-1920x1080-wallpaper-1711426.jpg" text=#D6EAF8>
	


	<h1>
	<font face="Century Gothic" color="#FCF3CF">
	&nbsp Hello %s
	</font>
	</h1>
	<font size="16" face="Consolas" color="#2E86C1">
	<hr width=50px align="left">

	<font color="#EBF5FB" size="20"><p align="center">You have been successfully registered on our website!!<br><p align="center">Thank you joining us!!!</font><br>
<p align="center"><a href="http://127.0.0.1:8080/api/login">Please Login to Continue</a>


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
