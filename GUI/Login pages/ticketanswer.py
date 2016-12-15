'''
Created on 15 dec. 2016

@author: Abigail
'''

import os, os.path
import string

import cherrypy
import pymysql


class TicketAnswerPage:

    exposed = True
    
    def GET(self, user):
	
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()

        cur.execute("SELECT request FROM ticket WHERE username=%s", user)

        ticketrequest=cur.fetchone()

        cur.execute("SELECT answer FROM ticket WHERE username=%s", user)

        ticketanswer=cur.fetchone()

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
	&nbsp TICKET ANSWER
	</font>
	</h1>
	<hr width=50% align="left">

	<font color="#EBF5FB" size="20"><p align="center">You have recieved response from the administrator</font>

	<table align="center" cellpadding=10>

	<tr><td align=center>
	<font face="Consolas" size="8" color="#2E86C1">
	Request sent
	</font>
	</td>
	<td align=center>
	<font face="Consolas" size="8" color="#2E86C1">
	Answer recieved
	</font>
	</td></tr>
	<tr></td><td align="left"><textarea cols="50" rows="10" height="500px" width="500px" name="ticket" maxlength="500" size="16">
	%s</textarea></td>
	<td align="right"><textarea cols="50" rows="10" height="500px" width="500px" name="ticket" maxlength="500" size="16">
	%s</textarea>
	</td>
	</tr>

	</table>

	<br><br>
	<br><br>
	<p align="center"><font face="Century Gothic" color="#FADBD8">
	Send another request?
	</font>
	<a href="http://localhost:8080/api/ticket"><font color="#EBF5FB">Request Ticket</font></a>

	</font>

</body>
<br><br><br>
<font face="Century Gothic" color="#EBF5FB">
<hr align="center" width="50%">
<p align="center">&copy2016&nbsp Bookishelf.com
</font>

        </html>""" % (request, answer))
