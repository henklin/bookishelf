import os, os.path
import random
import string

import cherrypy


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>

<head>
<title>Book Review</title>
</head>

	<table>
	<tr><td>
	<a href="Homepage.html">
	<img src="http://images.clipartpanda.com/embryo-clipart-book17.png" height="50" width="100">
	</a>
	</td>
	<td width="1000" align="right">
	<h2><a href="Login.html"><font size=30 face="Consolas" color="#EBF5FB">Login</font></a></h2>
	</td></tr>
	</table>
	

<body background="http://wallpaperus.org/wallpapers/03/122/books-1920x1080-wallpaper-1711426.jpg" text=#D6EAF8>


<h1 align="center"><font face="Century Gothic" color="#EBF5FB">SHOPPING CART</font></h1>
<font size=5 face="Consolas" color="#EBF5FB">
<hr width=30%>

<table align="center" cellpadding=55>
<tr>
<td><img height="500" width="400" src="http://www.images-booknode.com/book_cover/2574/full/le-jour-ou-j-ai-voulu-devenir-populaire-2573812.jpg" alt="book1"></td>
<td>
<font color="#EBF5FB" size=5 face="Source Sans Pro">
Details<br><br>
<%print(Howtobepopular);%>
<br>
<font size=3>Author-<%print(bookauthor);%></font><br>
Original Price-$<%print(bookoriginalprice);%>/-<br>
Price-$<%print(bookprice);%>/-<br>
You save-<%print(discount);%>%<br>
Rating-<%print(bookrating);%>/5<br>
</font><br>
<form action="checkout.html">
<input type="submit" value="Proceed to Buy" name="buy">
</form>
</td>
</tr>
</table>

<font face="Century Gothic" color="#1A5276">
<hr align="center" width="50%">
<p align="center">&copy2016&nbsp Bookishelf.com
</font>
</body>


        </html>"""



if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)