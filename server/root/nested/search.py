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
    
    def GET(self, title, Genre):
        
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
</head>

<body background="http://wallpaperus.org/wallpapers/03/122/books-1920x1080-wallpaper-1711426.jpg" text=#D6EAF8>
	
	<a href="http//localhost:8080/api/bookishelf">
	<img src="http://images.clipartpanda.com/embryo-clipart-book17.png" height="50" width="100">
	</a>

	<font size="16" face="Consolas" color="#2E86C1">
	<hr width=50px align="left">
	
	<form action="http://localhost:8080/api/search" method="get">
	<table align="center">

	<tr><td>
	Search for another book:</td><td align="left"><input type="text" name="title" maxlength="32" size="16">
	</td><td>
	<select name="Genre">
	  <option value="Fiction">Fiction</option>
	  <option value="Horror">Horror</option>
	  <option value="Thriller">Thriller</option>
	  <option value="Romance">Romance</option>
	</select>
	</td>

	<td><input type="submit" value="Search"></td></tr>

	</table>

	</form>

<table align="center">
<tr>
<th colspan=5 align="center">Search Results</th>
<tr></tr></tr>
<tr>
<a href="http://127.0.0.1:8080/api/bookPage?bookid=2">
%s
</a></tr>

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

        </html>""" % (returnString))
