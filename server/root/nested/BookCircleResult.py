'''
Created on 18 nov. 2016

@author: Henrik
'''
import cherrypy
import pymysql
import string

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()

class bookCResult:

    exposed = True
    
    def POST(self, userid):
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
    

    <table>
    <tr><td>
    <form action="http://127.0.0.1:8080/api/" method="post">
    <input type="hidden" name="userid" value="%s">
    <button class="button button1">
    <img src="http://images.clipartpanda.com/embryo-clipart-book17.png" height="100" width="300">
    </button>
    </form>
    </td></tr>
    <tr>
	<td width="1000" align="right">
    <h2><a href="http://localhost:8080/api/logoutpage"><font size=15 face="Consolas" color="#EBF5FB">Logout</font></a></h2>
    </td></tr>
    </table>

    <div align="right">
    <form action="http://127.0.0.1:8080/api/shoppingCart" method="post">
    <button class="button button1">
    <input type="hidden" name="userid" value="%s">
    <br>
    </button>
    </form>
    </div>


    <font size="16" face="Consolas" color="#2E86C1">
    <hr width=1000px align="left">

    <form action="http://localhost:8080/api/search" method="post">
    <table align="center">

    <tr><td>
    <input type="hidden" name="userid" value="%s">
    Search:</td><td align="left"><input type="text" name="title" maxlength="32" size="16">
    <input type="hidden" name="userid" value="%s">
    </td>

    <td><input type="submit" value="Search"></td></tr>

    </table>

    </form>

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
    
  
        
      
