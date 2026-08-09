import smtplib
# outlook.office365.com

my_email = "satyamlodhi735562@gmail.com"
password = 'AjayLodhiSonia112211@@@'
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user= my_email, password=password)

connection.sendmail(from_addr=my_email, to_addrs="satyamlodhi122@outlook.com", msg="hello")
connection.close()