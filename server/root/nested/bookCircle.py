'''
Created on 19 dec. 2016

@author: Alejandro P. Hernandez
'''

import os, os.path
import string
import cherrypy
import pymysql
import requests
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import Encoders

class BookCircle:

    exposed = True

    def mail(self, to, subject, text):
    
        gmail_user = "bookishelfNoReply@gmail.com"
        gmail_pwd = "bookishelf1"
        
        msg = MIMEMultipart()
    
        msg['From'] = gmail_user
        msg['To'] = to
        msg['Subject'] = subject
    
        msg.attach(MIMEText(text))
    
    
        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmail_user, gmail_pwd)
        mailServer.sendmail(gmail_user, to, msg.as_string())
    
        mailServer.close()


    
    
    def GET(self, bookid):
        
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
            &nbsp Send mail to USER
            </font>
            </h1>
            <hr width=50px align="left">
            
            <font color="#EBF5FB" size="20"><p align="center">Fill in the details of BOOK</font>
            
            <form action="http://localhost:8080/api/bookCircle" method="post">
            <table align="center">
            
            <tr><td align=center>
            <font face="Consolas" size="8" color="#2E86C1">
            Enter your request:
            </font>
            <input type="hidden" name="bookid" value="%s">
            <tr></td><td align="left"><textarea cols="100" rows="10" height="500px" width="5000px" name="circleMessage" maxlength="500" size="16"> </textarea></td></tr>
            
            
            <td align=center><input type="submit" value="Send"></td></tr>
            
            </table>
            
            </form>
            
            
            <br><br>
            
            </body>
            <br><br><br>
            <font face="Century Gothic" color="#EBF5FB">
            <hr align="center" width="50px">
            <p align="center">&copy2016&nbsp Bookishelf.com
            </font>

            
            """ % (bookid))
        
        
    def POST(self, bookid, userid, circleMessage):
        
        conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mydb', autocommit=True)

        cur = conn1.cursor()
        
        cur.execute("SELECT email FROM mydb.user WHERE userid = %s" % (userid))
        
        senderEmail = cur.fetchone()
        tempSt0 = str(senderEmail[0]).replace("(", "")
        tempSt1 = str(tempSt0).replace(")", "")
        tempSt2 = str(tempSt1).replace("'", "")
        tempSt3 = str(tempSt2).replace(",", "")
        
        circleMessage = circleMessage + " \n This is my email, if you want to keep talking about the book please contanct me: " + tempSt3

        cur.execute("SELECT email FROM mydb.user INNER JOIN bookOrder WHERE bookID = %s" % (bookid))
        
        emails = cur.fetchall()
        
        for x in range(0 , len(emails)):
            tempStr0 = str(emails[x]).replace("(", "")
            tempStr1 = str(tempStr0).replace(")", "")
            tempStr2 = str(tempStr1).replace("'", "")
            tempStr3 = str(tempStr2).replace(",", "")
            BookCircle.mail(self, tempStr3 ,"Book Circle", circleMessage)


        

