'''
Created on 15 dec. 2016

@author: Abigail
'''

import os, os.path
import string

import cherrypy
import pymysql


class TicketPage:

    exposed = True
    
    def GET(self):
        return ("""
<!DOCTYPE html>

<head>
<title>Bookishelf</title>

<style>
textarea {
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
	-moz-border-radius:28px;
	-webkit-border-radius:28px;
	border-radius:28px;
	border:1px solid #2E86C1;
	display:inline-block;

	}


input[type=submit] {
    width: 100%;
	height: 45px;
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
    font-size: 24px;
    font-family: Consolas;
	-moz-border-radius:28px;
	-webkit-border-radius:28px;
	border-radius:28px;
	border:1px solid #2E86C1;
	display:inline-block;
	
}


</style>

</head>

<body background="http://wallpaperus.org/wallpapers/03/122/books-1920x1080-wallpaper-1711426.jpg" text=#D6EAF8>
	

	<table>
	<tr><td>
	<a href="http://localhost:8080/api/bookihomepage">
	<img src="http://images.clipartpanda.com/embryo-clipart-book17.png" height="50" width="100">
	</a>
	</td>
	<td width="1000" align="right">
	<h2><a href="http://localhost:8080/api/logoutpage"><font size=15 face="Consolas" color="#EBF5FB">Logout</font></a></h2>
	</td></tr>
	</table>

	<h1>
	<font face="Century Gothic" size=20 color="#FCF3CF">
	&nbsp SEND A TICKET
	</font>
	</h1>
	<hr width=50% align="left">

	<font color="#EBF5FB" size="20"><p align="center">Fill in the details for sending the ticket request</font>

	<form action="http://localhost:8080/api/handleticket" method="get">
	<table align="center">

	<tr><td align=center>
	<font face="Consolas" size="8" color="#2E86C1">
	Enter your request:
	</font>
	<tr></td><td align="left"><textarea cols="100" rows="10" height="500px" width="5000px" name="ticket" maxlength="500" size="16">
	</textarea></td></tr>

	<td align=center><input type="submit" value="Send Ticket"></td></tr>

	</table>

	</form>


	<br><br>

</body>
<br><br><br>
<font face="Century Gothic" color="#EBF5FB">
<hr align="center" width="50%">
<p align="center">&copy2016&nbsp Bookishelf.com
</font>

        </html>""" )
