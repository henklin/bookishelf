import os, os.path
import random
import string

import cherrypy


class RegisterPage:

    exposed = True
    
    def GET(self):
        return ("""
<!DOCTYPE html>
<html>

<head>
<title>Bookishelf</title>
</head>

<body background="http://wallpaperus.org/wallpapers/03/122/books-1920x1080-wallpaper-1711426.jpg" text=#D6EAF8>

	
	<a href="Homepage.html">
	<img src="http://images.clipartpanda.com/embryo-clipart-book17.png" height="50" width="100">
	</a>

	<h1>
	<font face="Century Gothic" color="#FCF3CF">
	&nbsp ENTER THE FUTURE
	</font>
	</h1>
	<font size=5 face="Consolas" color="#FADBD8">
	<hr width=50% align="left">
	<br><br><br>

	<font color="#EBF5FB"><p align="center">Enter your details to Register</font>

	<form action="api/exmp1" method="get">
	<table align="center">

	<tr><td>
	First Name:</td><td align="left"><input type="text" name="firstname" maxlength="32" size="16">
	</td></tr>

	<tr><td>
	Last Name:</td><td align="left"><input type="text" name="lastname" maxlength="32" size="16">
	</td></tr>

	<tr><td>
	E-mail ID:</td><td align="left"><input type="text" name="email" maxlength="32" size="16">
	</td></tr>

	<tr><td>
	User-name:</td><td align="left"><input type="text" name="user" maxlength="32" size="16">
	</td></tr>

	<tr><td>
	Password:</td><td align="left"><input type="text" name="password" maxlength="32" size="16">
	</td></tr>

	<tr><td>
	Re-type Password:</td><td align="left"><input type="repassword" name="pswd">
	</td></tr>

	<tr><td align="center"><input type="submit" value="Login"></td></tr>

	</table>

	</form>

	<br><br>

	</font>
</body>
<br><br><br>
<font face="Century Gothic" color="#1A5276">
<hr align="center" width="50%">
<p align="center">&copy2016&nbsp Bookishelf.com
</font>
        </html>""" )


