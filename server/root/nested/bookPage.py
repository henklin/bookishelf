'''
Created on 18 nov. 2016

@author: Henrik
'''
import cherrypy
import pymysql



class BookPage:

    exposed = True
    
    
    def POST(self, bookid, userid):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("SELECT image FROM book WHERE id=%s" % bookid)
        
        bookImage = cur.fetchone()
        
        cur.execute("SELECT qty FROM book WHERE id=%s" % bookid)
        
        bookQty = cur.fetchone()
        
        cur.execute("SELECT price FROM book WHERE id=%s" % bookid)
        
        bookPrice = cur.fetchone()
        
        cur.execute("SELECT title FROM book WHERE id=%s" % bookid)
        
        bookTitle = cur.fetchone()
        
        cur.execute("SELECT description FROM book WHERE id=%s" % bookid)
        
        bookDesc = cur.fetchone()
        
        cur.close()
        
        qtyString = ''
        
        if(int(bookQty[0]) > 0):
            qtyString = 'In stock'
        else:
            qtyString = 'Out of stock'    
        
        
        
        
        
        return("""<html>
            
            <head>
            <title>Book page</title>
            
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

.button {
    padding: 0px 0px;
    margin: 0px;
    }

.button1 {
    width: 0px;
    height: 0px;
    background-color: Transparent;
    }

.button2 {
    width: 0px;
    height: 0px;
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
            
            <div align="left">
            <form action="http://127.0.0.1:8080/api/" id="form1" method=post>
            <input type=hidden name="userid" value="%s">
            <button class="button button2" type=submit form="form1">
            <img src="http://images.clipartpanda.com/embryo-clipart-book17.png" height="50" width="100">
            </button>
            </form>
            
            <div align="right">
            <form action="http://127.0.0.1:8080/api/shoppingCart" method="post">
            <button>
            <input type="hidden" name="userid" value="%s">
            Shopping Cart<br><img src="https://www.iconexperience.com/_img/g_collection_png/standard/512x512/shopping_cart.png" alt="Shopping Cart" height="150" width="150">
            </button>
            </form>
            </div>
            
            
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
            
            <h1 align="center"><font face="Century Gothic" color="#EBF5FB">%s</font></h1>
            <font size=5 face="Consolas" color="#EBF5FB">
            <hr width=30>
            
            <table align="center" cellpadding=55>
            <tr>
            <td><img height="500" width="400" src="%s" alt="book1"></td>
            <td>
            <font color="#EBF5FB" size=5 face="Source Sans Pro">Details<br><br>%s<br>
            <font size=3>Author-TBA</font><br>
            Price-%s kr<br>
            %s<br>
            </font><br>
            <form action="http://127.0.0.1:8080/api/addshoppingCart" method=post>
            <input type=hidden name="bookid" value="%s">
            <input type=hidden name="userid" value="%s">
            <input type="submit" value="Add to Cart">
            </form>
            </td>
            </tr>
            <tr><td>
            <form action="http://localhost:8080/api/bookCirclePage" method="post">
            <input type="hidden" value="%s" name="bookid">
            <input type="hidden" value="%s" name="userid">
            <input type="submit" value="Go to Book Circle">
            </form>
            </td></tr>
            </table>
            
            <font face="Century Gothic" color="#1A5276">
            <hr align="center" width="50">
            <p align="center">&copy2016&nbsp Bookishelf.com
            </font>
            </body>
            
            
            </html>
""" % (userid, userid, bookTitle[0], bookImage[0], bookDesc[0], bookPrice[0], qtyString, bookid, userid, bookid, userid))

            
            
          
            
            
        

    
    
    
    def GET(self, bookid):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("SELECT image FROM book WHERE id=%s" % bookid)
        
        bookImage = cur.fetchone()
        
        cur.execute("SELECT price FROM book WHERE id=%s" % bookid)
        
        bookPrice = cur.fetchone()
        
        cur.execute("SELECT qty FROM book WHERE id=%s" % bookid)
        
        bookQty = cur.fetchone()
        
        cur.execute("SELECT title FROM book WHERE id=%s" % bookid)
        
        bookTitle = cur.fetchone()
        
        cur.execute("SELECT description FROM book WHERE id=%s" % bookid)
        
        bookDesc = cur.fetchone()
        
        cur.close()
        
        
        
        if(int(bookQty[0]) > 0):
            qtyString = 'In stock'
        else:
            qtyString = 'Out of stock' 
        
        return("""<html>

<head>
<title>Book page</title>
</head>

    <div align="left">
    <a href="http://127.0.0.1:8080/api/">
    <img src="http://images.clipartpanda.com/embryo-clipart-book17.png" height="50" width="100">
    </a>

    <div align="right">
    <form action="http://127.0.0.1:8080/api/shoppingCart" method="get">
    <button>
    <input type="hidden" name="userid" value="1">
    Shopping Cart<br><img src="https://www.iconexperience.com/_img/g_collection_png/standard/512x512/shopping_cart.png" alt="Shopping Cart" height="150" width="150">
    </button>
    </form>
    </div>
    

<body background="http://wallpaperus.org/wallpapers/03/122/books-1920x1080-wallpaper-1711426.jpg" text=#D6EAF8>

            
            <table>
            <tr><td>
            <a href="http://localhost:8080/api/">
            <img src="http://images.clipartpanda.com/embryo-clipart-book17.png" height="50" width="100">
            </a>
            </td></tr>
            </table>


<h1 align="center"><font face="Century Gothic" color="#EBF5FB">%s</font></h1>
<font size=5 face="Consolas" color="#EBF5FB">
<hr width=30>

<table align="center" cellpadding=55>
<tr>
<td><img height="500" width="400" src="%s" alt="book1"></td>
<td>
<font color="#EBF5FB" size=5 face="Source Sans Pro">Details<br><br>%s<br>
<font size=3>Author-TBA</font><br>
Price-%s kr<br>
%s<br>
</font><br>

</td>
</tr>
<br>
<form action="http://localhost:8080/api/bookCircle" method="GET">
<input type="hidden" value="%s" name="bookid">
<input type="submit" value="Go to Book Circle">
</form>
</td></tr>
</table>

<font face="Century Gothic" color="#1A5276">
<hr align="center" width="50">
<p align="center">&copy2016&nbsp Bookishelf.com
</font>
</body>


        </html>""" % (bookTitle[0], bookImage[0], bookDesc[0], bookPrice[0], qtyString, bookid))

    
  
        
        
       
