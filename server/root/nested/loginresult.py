'''
Created on 05 dec. 2016

@author: Abigail
'''
import cherrypy
import pymysql
import requests

class LoginResult:
    

    exposed = True
    
    def POST(self, uname, pswd):
        		
	
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()

        cur.execute("SELECT username FROM user WHERE username=%s", uname)

        usname=cur.fetchone()
        
        
        cur.execute("SELECT userid FROM user WHERE username=%s", uname)

        userid=cur.fetchone()

        cur.execute("SELECT password FROM user WHERE username=%s", uname)

        temppassword=cur.fetchone()
        

        cur.close()
        
        if(temppassword == None):
            tryPass = ""
        else:
            tryPass = temppassword[0]
            
		
        if(tryPass==pswd):
            r = requests.post("http://127.0.0.1:8080/api/", data={'userid': userid[0]})
            return (r.text)
        else:
            return("""<html>

<head>
<title>Bookishelf</title>
</head>

<body background="http://wallpaperus.org/wallpapers/03/122/books-1920x1080-wallpaper-1711426.jpg" text=#D6EAF8>
	
            
            <table>
            <tr><td>
            <a href="http://localhost:8080/api/">
            <img src="http://images.clipartpanda.com/embryo-clipart-book17.png" height="50" width="100">
            </a>
            </td></tr>
            </table>

	<h1>
	<font face="Century Gothic" color="#FCF3CF">
	&nbsp The password entered does not match with the username %s
	</font>
	</h1>

	<font size="12" face="Consolas" color="#2E86C1">
	<hr width=500px align="left">

	
	<font color="#EBF5FB"><p align="center">Retry to Login</font>

	<form action="http://localhost:8080/api/loginresult" method="post">
	<table align="center">

	<tr><td>
	User-ID:</td><td align="left"><input type="text" name="uname" maxlength="32" size="16">
	</td></tr>

	<tr><td>
	Password:</td><td align="left"><input type="password" name="pswd" maxlength="32" size="16">
	</td></tr>

	<tr><td align="center"><input type="submit" value="Login"></td></tr>

	</table>

	</form>

	<font color="#EBF5FB" size="12"><p align="center">Search the Book you are looking for</font>

	<form action="http://localhost:8080/api/search" method="get">
	<table align="center">

	<tr>
	<td>
	<font size="12">
	Search:
	</font>
	</td>
	<td align="left"><input type="text" name="user" maxlength="32" size="16">
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

</font>
</form>

	<br><br>
	<p align="center"><font face="Century Gothic" color="#FADBD8">
	Not a member yet?
	</font>
	<a href=http://localhost:8080/api/loginregister><font color="#EBF5FB">Sign Up</font></a>

	</font>
</body>
<br><br><br>
<font face="Century Gothic" color="#1A5276">
<hr align="center" width="500px">
<p align="center">&copy2016&nbsp Bookishelf.com
</font>

        </html>""" )
	   
