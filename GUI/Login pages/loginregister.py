import os, os.path
import random
import string
import pymysql
import cherrypy


class RegisterPage:

    exposed = True
    
    def GET(self):
        return ("""
<!DOCTYPE html>
<html>

<head>
<title>Bookishelf</title>

<script type="text/javascript">

  function registerCheck(form)
  {
    if(form.firstname.value == "") {
      alert("Error: First name is required!");
      form.firstname.focus();
      return false;
    }

    if(form.address.value == "") {
      alert("Error: Please fill your address!");
      form.address.focus();
      return false;
    }

    if(form.email.value == "") {
      alert("Error: E-mail is required!");
      form.email.focus();
      return false;
    }

    if(form.usern.value == "") {
      alert("Error: Username cannot be blank!");
      form.usern.focus();
      return false;
    }

    re = /^\w+$/;
    if(!re.test(form.usern.value)) {
      alert("Error: Username must contain only letters, numbers and underscores!");
      form.username.focus();
      return false;
    }

    if(form.upassword.value != "" && form.upassword.value == form.repassword.value) {
      if(form.upassword.value.length < 6) {
        alert("Error: Password must contain at least six characters!");
        form.upassword.focus();
        return false;
      }
      if(form.upassword.value == form.usern.value) {
        alert("Error: Password must be different from Username!");
        form.pwd1.focus();
        return false;
      }
      re = /[0-9]/;
      if(!re.test(form.upassword.value)) {
        alert("Error: password must contain at least one number (0-9)!");
        form.upassword.focus();
        return false;
      }
      re = /[a-z]/;
      if(!re.test(form.upassword.value)) {
        alert("Error: password must contain at least one lowercase letter (a-z)!");
        form.upassword.focus();
        return false;
      }
      re = /[A-Z]/;
      if(!re.test(form.upassword.value)) {
        alert("Error: password must contain at least one uppercase letter (A-Z)!");
        form.upassword.focus();
        return false;
      }
    } else {
      alert("Error: Please check that the password you've entered and re-typed is same!");
      form.upassword.focus();
      return false;
    }

    return true;
  }

</script>

</head>

<body background="http://wallpaperus.org/wallpapers/03/122/books-1920x1080-wallpaper-1711426.jpg" text=#D6EAF8 ng-app="reg">

	
	<a href="http://localhost:8080/api/bookihomepage">
	<img src="http://images.clipartpanda.com/embryo-clipart-book17.png" height="50" width="100">
	</a>

	<h1>
	<font face="Century Gothic" color="#FCF3CF">
	&nbsp ENTER THE FUTURE
	</font>
	</h1>
	<font size=5 face="Consolas" color="#FADBD8">
	<hr width=50% align="left">
	<br><br><br>

	<font color="#EBF5FB"><p align="center">Enter your details to Register</font>

	<form action="http://localhost:8080/api/registered" method="post" onsubmit="return registerCheck(this)">
	<table align="center">

	<tr><td>
	First Name:</td><td align="left"><input type="text" name="firstname" maxlength="32" size="16">
	</td></tr>

	<tr><td>
	Last Name:</td><td align="left"><input type="text" name="lastname" maxlength="32" size="16">
	</td></tr>

	<tr><td>
	Address:</td><td align="left"><input type="textbox" name="address" maxlength="555" size="16">
	</td></tr>
	
	<tr><td>
	E-mail ID:</td><td align="left"><input type="text" name="email" maxlength="32" size="16">
	</td></tr>

	<tr><td>
	User-name:</td><td align="left"><input type="text" name="usern" maxlength="32" size="16">
	</td></tr>

	<tr><td>
	Password:</td><td align="left"><input type="password" name="upassword" maxlength="32" size="20">
	</td></tr>

	<tr><td>
	Re-type Password:</td><td align="left"><input type="password" name="repassword" size="20">
	</td></tr>

	<tr><td align="center"><input type="submit" value="Register"></td></tr>

	</table>

	</form>

	<br><br>

	</font>
</body>
<br><br><br>
<font face="Century Gothic" color="#1A5276">
<hr align="center" width="50%">
<p align="center">&copy2016&nbsp Bookishelf.com
</font>
        </html>""" )

