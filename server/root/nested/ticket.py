'''
Created on 15 dec. 2016

@author: Abigail
'''

import os, os.path
import string

import cherrypy
import pymysql
import requests

class TicketPage():

    exposed = True
    
    def GET(self, userid):
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
    width: 100px;
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
	<a href="http://localhost:8080/api/">
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
	<hr width=50px align="left">

	<font color="#EBF5FB" size="20"><p align="center">Fill in the details for sending the ticket request</font>

	<form action="http://localhost:8080/api/ticket" method="post">
	<table align="center">

	<tr><td align=center>
	<font face="Consolas" size="8" color="#2E86C1">
	Enter your request:
	</font>
	<input type="hidden" name="userid" value="%s">
	<tr></td><td align="left"><textarea cols="100" rows="10" height="500px" width="5000px" name="info" maxlength="500" size="16">
	</textarea></td></tr>
	<input type="hidden" name="answer" value="">
	<input type="hidden" name="open" value="1">
	

	<td align=center><input type="submit" value="Send Ticket"></td></tr>

	</table>

	</form>


	<br><br>

</body>
<br><br><br>
<font face="Century Gothic" color="#EBF5FB">
<hr align="center" width="50px">
<p align="center">&copy2016&nbsp Bookishelf.com
</font>

        </html>""" % (userid))
        
        
    def POST(self, userid, info, answer, open):
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("INSERT INTO ticket (userid, info, answer, open) VALUES (%s, '%s', '%s', %s)" % (userid, info, answer, open))
        
            ##r = requests.get("http://127.0.0.1:8080/api/ticket")
            ##return (r.text)

        cur.close
        
        return(""""<!DOCTYPE html>

<html>

<head>

<style>

body{

      background-image:url("https://images.pexels.com/photos/175994/pexels-photo-175994.jpeg?w=940&h=650&auto=compress&cs=tinysrgb");

      background-size: 2700px 2000px;

      background-repeat: no-repeat;

      background-attachment: fixed;

      background-position: center;

}

</style>

</head>

<body>



<h1> <i> <center> <font size="10"> <p style="margin-top: 10cm;"> Thank you for submitting your problem, we will be in touch! </p></font> </center> </i></h1>

<a href="" target="_self"> <center> <font size="10"> Continue Shopping </font> </center> </a>

</body>

</html>""")
