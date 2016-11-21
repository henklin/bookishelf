<%@page language="java" contentType="text/html"%>

<html>

 <head><title>Bookishelf</title></head>

	<body background="C:\Users\Mini\Desktop\apache-tomcat-8.5.8-windows-x86\apache-tomcat-8.5.8\webapps\Bookishelf\Profile.jsp" text=#1A5276>
		
		<font size=4 face="Century Gothic">
		
	<%

		String un=request.getParameter("user");
		String pwd=request.getParameter("pswd");

	%>

	<br><br><h2 align="left">Welcome Back <%out.println(un);%>!</h2>
	<br><hr shade width=50% align="left"><br><br><br>

		<div align="center">

		<table cellpadding=10>
		<th>Successfully Logged in</th>
		<tr><%out.println(pwd);%></tr>
		</table>

<br>
<font face="Century Gothic" color="#FADBD8">
<table align="center">
<tr>
<th colspan=5 align="center">Recommended Books for you</th>
<tr></tr></tr>
<tr>
<td><a href="book1.html">
<img height="300" width="200" src="./book1.jpg" alt="book1">
</a></td>
<td><a href="book2.html">
<img height="300" width="200" src="./book2.jpg" alt="book2">
</a></td>
<td><a href="book3.html">
<img height="300" width="200" src="./book3.jpg" alt="book3">
</a></td>
<td><a href="book4.html">
<img height="300" width="200" src="./book4.jpg" alt="book4">
</a></td>
<td><a href="book5.html">
<img height="300" width="200" src="./book5.jpg" alt="book5">
</a></td>
</tr>
</table>
</font>


		<br><br><br><hr width=10%>

		<sub>&copy2016&nbspbookishelf.com</sub>
	
		<hr width=10%>

	</div>
	</font>
	</body>

</html>