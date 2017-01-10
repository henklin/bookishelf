'''
Created on 6 dec. 2016

@author: Abigail
'''

import os, os.path
import string

import cherrypy
import pymysql
from mako.template import Template


class SearchResult:

    exposed = True
    
    def GET(self, title):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
		
        tempQuery = Template("SELECT image FROM book WHERE title LIKE '%${search}%'")
        tempTitle = title
        cur.execute(tempQuery.render(search=tempTitle))
        

        bookImage = cur.fetchall()
        
        
        tempQuery = Template("SELECT id FROM book WHERE title LIKE '%${search}%'")
        tempTitle = title
        cur.execute(tempQuery.render(search=tempTitle))
        bookIds = cur.fetchall()
        
        
        returnString = ""
        i = 0
        for i in range(0, len(bookImage)):
            tempStr0 = str(bookImage[i]).replace("(", "")
            tempStr1 = str(tempStr0).replace(")", "")
            tempStr2 = str(tempStr1).replace("'", "")
            tempStr3 = str(tempStr2).replace(",", "")
            
            temp0 = str(bookIds[i]).replace("(", "")
            temp1 = str(temp0).replace(")", "")
            temp2 = str(temp1).replace("'", "")
            temp3 = str(temp2).replace(",", "")
            
            tempHTML = Template("""<img src="${image}" alt="harry poter" style="width:100px;height:150px;">
            """)
            
            
            HTMLtemp = Template("""<a href="http://127.0.0.1:8080/api/bookPage?bookid=${id}">
             ${imagelink}</a>""")
            returnString += HTMLtemp.render(id=temp3, imagelink=tempHTML.render(image=tempStr3))
        cur.close()
                   
        
        return ("""<html>

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
<tr>
<th colspan=5 align="center">Search Results</th>
</tr>
</table>
<a href="http://127.0.0.1:8080/api/bookPage?bookid=2">
%s
</a>
</font>
</form>

	<br><br>
	<p align="center"><font face="Century Gothic" color="#FADBD8">
	Not a member yet?
	</font>
	<a href="http//localhost:8080/api/loginregister"><font color="#EBF5FB">Sign Up</font></a>

	</font>
</body>
<br><br><br>
<font face="Century Gothic" color="#1A5276">
<hr align="center" width="50px">
<p align="center">&copy2016&nbsp Bookishelf.com
</font>

        </html>""" % (returnString))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def POST(self, title, userid):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        tempQuery = Template("SELECT image FROM book WHERE title LIKE '%${search}%'")
        tempTitle = title
        cur.execute(tempQuery.render(search=tempTitle))
        

        bookImage = cur.fetchall()
        
        
        tempQuery = Template("SELECT id FROM book WHERE title LIKE '%${search}%'")
        tempTitle = title
        cur.execute(tempQuery.render(search=tempTitle))
        bookIds = cur.fetchall()
        
        
        returnString = ""
        i = 0
        for i in range(0, len(bookImage)):
            tempStr0 = str(bookImage[i]).replace("(", "")
            tempStr1 = str(tempStr0).replace(")", "")
            tempStr2 = str(tempStr1).replace("'", "")
            tempStr3 = str(tempStr2).replace(",", "")
            
            temp0 = str(bookIds[i]).replace("(", "")
            temp1 = str(temp0).replace(")", "")
            temp2 = str(temp1).replace("'", "")
            temp3 = str(temp2).replace(",", "")
            
            tempHTML = Template("""<form method="post" action="http://127.0.0.1:8080/api/bookPage">
            <input type="hidden" name="bookid" value="${bookid1}">
            <input type="hidden" name="userid" value="${userid1}">
            <button>
            <img src="${image}" alt="harry poter" style="width:100px;height:150px;">
            </button>
            </form>
            """)
            
            
            returnString += tempHTML.render(bookid1=temp3, userid1=userid, image=tempStr3)
        cur.close()
                   
        
        return ("""<html>

<head>
<title>Bookishelf</title>
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

    <font size="16" face="Consolas" color="#2E86C1">
    <hr width=50px align="left">
    

<table align="center">
<tr>
<th colspan=5 align="center">Search Results</th>
</tr>

<a href="http://127.0.0.1:8080/api/bookPage?bookid=2">
%s
</a>&nbsp

</table>
</font>
</form>

    <br><br>
    <p align="center"><font face="Century Gothic" color="#FADBD8">
    Not a member yet?
    </font>
    <a href="http//localhost:8080/api/loginregister"><font color="#EBF5FB">Sign Up</font></a>

    </font>
</body>
<br><br><br>
<font face="Century Gothic" color="#1A5276">
<hr align="center" width="50px">
<p align="center">&copy2016&nbsp Bookishelf.com
</font>

        </html>""" % (userid, returnString))

