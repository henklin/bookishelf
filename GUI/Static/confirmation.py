import os, os.path
import random
import string

import cherrypy


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>

<head>
<title>order</title>
</head>

<body background="http://wallpaperus.org/wallpapers/03/122/books-1920x1080-wallpaper-1711426.jpg" text=#D6EAF8>
	
	<a href="Homepage.html">
	<img src="http://images.clipartpanda.com/embryo-clipart-book17.png" height="50" width="100">
	</a>


<h1><font face="Century Gothic" color="#084b8a">Order Confirmation</font></h1>

<font size=4 face="Consolas">
	<hr width=50% align="left">
	<br><br><br>
		
<p align="center">Your payment was successful and your order will be delivered within short time.
<p align="center">Thank You for using Bookishelf
<p align="center">:)
<br><br><br><br><br>


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