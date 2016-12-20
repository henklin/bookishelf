'''
Created on 19 dec. 2016

@author: Abigail
'''

import os, os.path
import string

import cherrypy
import pymysql
import requests

class CreditPage():

    exposed = True
    
    def POST(self, userid):
        return ("""
<!DOCTYPE html>

<head>
<title>Bookishelf</title>


<style>
input[type=text] {
    width: 200px;
    height: 45px;
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
    border-radius:28px;
    border:1px solid #EBF5FB;
    display:inline-block;
    }

	#card
	{
    width: 100px;
    height: 35px;
    }

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

	
input[type=submit] {
    width: 300px;
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
	&nbsp ADD CREDITS
	</font>
	</h1>
	<hr width=50px align="left">

	<font color="#EBF5FB" size="20"><p align="center">Fill in the details for adding credits</font>
	<font face="Consolas" size="8" color="#2E86C1">
	<p align="center">Enter the required details:
	</font>

	<table align="center">
	
	<tr><td align="right">	<font color="#EBF5FB" size="11">
	Card Type:
	</td><td align="left"><select name="cardtype">
	<option value="Master">Master</option>
	<option value="Visa">Visa</option>
	<option value="Maestro">Maestro</option>
	</select>
	</font>
	</td></tr>

	<tr><td align="right">	<font color="#EBF5FB" size="11">
	Card Owner-Name:
	</td><td align="left">
	<input class="normal" type="text" name="cardname">
	</font>
	</td></tr>
	<tr><td align="right"><font color="#EBF5FB" size="11">
	Card-Number:
	</td><td align="left">
    <input id="card" type="text" class="input-block-level" autocomplete="off" maxlength="4" pattern="\d{4}" title="First four digits" required>-
    <input id="card" type="text" class="input-block-level" autocomplete="off" maxlength="4" pattern="\d{4}" title="Second four digits" required>-
    <input id="card" type="text" class="input-block-level" autocomplete="off" maxlength="4" pattern="\d{4}" title="Third four digits" required>-
    <input id="card" type="text" class="input-block-level" autocomplete="off" maxlength="4" pattern="\d{4}" title="Fourth four digits" required>
    </div>
	</font>
	</td></tr>

    <form action="http://localhost:8080/api/addcredit" method="post">
    <tr><td align="right">    <font color="#EBF5FB" size="11">
    Add amount:
    </td><td align="left"><select name="amount">
    <option value="10">10</option>
    <option value="50">50</option>
    <option value="100">100</option>
    <option value="200">200</option>
    <option value="500">500</option>
    </select>
    </font>
    </td></tr>
	<tr>
	<input type="hidden" name="userid" value="%s">
	<td colspan=2 align=center><input type="submit" value="Submit details"></td></tr>
	</form>
    </table>

	<br><br>

</body>
<br><br><br>
<font face="Century Gothic" color="#EBF5FB">
<hr align="center" width="50px">
<p align="center">&copy2016&nbsp Bookishelf.com
</font>

        </html>""" % (userid))
