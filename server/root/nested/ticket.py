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
    width: 300px;
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

button {
    width: 200px;
	height: 300px;
    padding: 0px 0px;
    margin: 0px;
    box-sizing: border-box;
	border-radius:28px;
	border:0px;
	display:inline-block;

	}

</style>

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
	<font face="Century Gothic" size=20 color="#FCF3CF">
	&nbsp SEND A TICKET
	</font>
	</h1>
	<hr width=1000px align="left">

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

        </html>""" % (userid, userid))
        
        
    def POST(self, userid, info, answer, open):
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("INSERT INTO ticket (userid, info, answer, open) VALUES ('%s', '%s', '%s', '%s')" % (userid, info, answer, open))
        
            ##r = requests.get("http://127.0.0.1:8080/api/ticket")
            ##return (r.text)

        cur.close
        
        
        return ("""
            <html>
            
            <head>
            <title>Bookishelf</title>
            
            <style>
            select {
            border: 0 none;
            color: #4A235A;
            background: #FBEEE6;
            font-size: 24px;
            font-family: Consolas;
            font-weight: bold;
            padding: 2px 10px;
            width: 200px;
            height: 45px;
            border-radius:28px;
            border:1px solid #EBF5FB;
            display:inline-block;
            
            }
            
            .button {
            padding: 0px 0px;
            margin: 0px;
            }
            
            .button1 {
            width: 100px;
            height: 100px;
            background-color: Transparent;
            box-sizing: border-box;
            border-radius:28px;
            border:0px;
            display:inline-block;
            }
            
            .button2 {
            width: 200px;
            height: 300px;
            box-sizing: border-box;
            border-radius:28px;
            border:0px;
            display:inline-block;
            }
            
            
            input[type=submit] {
            width: 200px;
            height: 45px;
            padding: 12px 20px;
            margin: 8px 0;
            box-sizing: border-box;
            font-size: 24px;
            font-family: Consolas;
            border-radius:28px;
            border:1px solid #EBF5FB;
            display:inline-block;
            
            }
            
            </style>
            
            </head>
            
            <body background="http://wallpaperus.org/wallpapers/03/122/books-1920x1080-wallpaper-1711426.jpg" text=#D6EAF8>
            
            
            
            <font size="16" face="Consolas" color="#2E86C1">
            <hr width=1000px align="left">
            
            <table align="center">
            <tr><td>
            <form action="http://127.0.0.1:8080/api/" method="post">
            <input type="hidden" name="userid" value="%s">
            <input type="submit" value="Go Back to Home Page">
            </form>
            </td></tr>
            <tr>
            <td width="1000" align="right">
            <h2><a href="http://localhost:8080/api/logoutpage"><font size=15 face="Consolas" color="#EBF5FB">Logout</font></a></h2>
            </td></tr>
            
            
            <br><br>
            
            <table align=center cellpadding=4>
            <tr><td align=right>
            <font face="Century Gothic" color="#FADBD8">
            Do you have any problem?
            </font>
            </td><td align=left>
            <form method="get" action="http://127.0.0.1:8080/api/ticket">
            <font color="#EBF5FB">
            <input type="hidden" name="userid" value="%s">
            <input type="submit" value="Contact us!"></font>
            </form>
            </td></tr>
            </table>
            
            </font>
            </body>
            <br><br><br>
            <font face="Century Gothic" color="#1A5276">
            <hr align="center" width="50">
            <p align="center">&copy2016&nbsp Bookishelf.com
            </font>
            
            </html>""" % (userid, userid))

