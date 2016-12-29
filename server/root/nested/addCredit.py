'''
Created on 18 nov. 2016

@author: Henrik
'''
import cherrypy
import pymysqlimport requests
from mako.template import Template

##conn = sqlite3.connect('C:/Users/Henrik/test.db')
##c=conn.cursor()

class AddCredit:
    
    
    exposed = True
    
    
    def POST(self, amount, userid):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("SELECT credit FROM user WHERE userid=%s " % (userid) )        credit = cur.fetchone()                        temp0 = str(credit[0]).replace("(", "")        temp1 = str(temp0).replace(")", "")        temp2 = str(temp1).replace("'", "")        temp3 = str(temp2).replace(",", "")                        newCredit = int(temp3) + int(amount)                        cur.execute("UPDATE user SET credit=%s WHERE userid=%s" % (newCredit, userid))                cur.close()            ##r = requests.post("http://127.0.0.1:8080/api/shoppingCart", data={'userid': theuserid})        return ("""<!DOCTYPE html><head><title>Bookishelf</title><style>    input[type=submit] {    width: 300px;    height: 45px;    padding: 12px 20px;    margin: 8px 0;    box-sizing: border-box;    font-size: 24px;    font-family: Consolas;    border-radius:28px;    border:1px solid #EBF5FB;    display:inline-block;}</style></head><body background="http://wallpaperus.org/wallpapers/03/122/books-1920x1080-wallpaper-1711426.jpg" text=#D6EAF8>        <table>    <tr><td>    <a href="http://localhost:8080/api/">    <img src="http://images.clipartpanda.com/embryo-clipart-book17.png" height="50" width="100">    </a>    </td></tr>    </table>    <h1>    <font face="Century Gothic" size=20 color="#FCF3CF">    &nbsp SUCCESSFUL!    </font>    </h1>    <hr width=50px align="left">    <font color="#EBF5FB" size="20"><p align="center">    Credits Successfully added into your account!    </font>    <br><br>    <h2><form action="http://localhost:8080/api/shoppingCart" method=post>    <input type=hidden name="userid" value="%s">    <font size=15 face="Consolas" color="#EBF5FB">    <p align=center><input type=submit value="Back to shopping cart">    </font>    </form></h2></body><br><br><br><font face="Century Gothic" color="#EBF5FB"><hr align="center" width="50px"><p align="center">&copy2016&nbsp Bookishelf.com</font>        </html>""" % userid)   
                        
        
        