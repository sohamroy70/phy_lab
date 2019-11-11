  
import smtplib 
s = smtplib.SMTP('smtp.gmail.com', 587)  
s.starttls() 
s.login("sohamroy70@gmail.com", "8409553891") 
message ="""\
Subject: Hi there

This message is sent from Python."""
s.sendmail("sohamroy70@gmail.com", "wizsoham@gmail.com", message) 
print("message sent") 
s.quit() 
