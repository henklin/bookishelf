import os, os.path
import random
import string

import cherrypy


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>

<head>
<title>Bookishelf</title>
</head>

<body background="http://wallpaperus.org/wallpapers/03/122/books-1920x1080-wallpaper-1711426.jpg" text=#D6EAF8>

	
	<a href="Homepage.html">
	<img src="http://images.clipartpanda.com/embryo-clipart-book17.png" height="50" width="100">
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

	<form action="http://localhost:8080/api/books" method="get">
	<table align="center">

	<tr><td>
	User-ID:</td><td align="left"><input type="text" name="user" maxlength="32" size="16">
	</td></tr>

	<tr><td>
	Password:</td><td align="left"><input type="password" name="pswd">
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
        </html>"""


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)