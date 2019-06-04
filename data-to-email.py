import smtplib   
s = smtplib.SMTP('smtp.gmail.com', 587)   
s.starttls() 

#!Remember! You need to enable 'Allow less secure apps' in your google account
# Enter your gmail username and password
s.login("youremail@gmail.com", "yourpassword") 
  
# message to be sent 
message = "Hello how are you doing"
  
# Sender email, recipient email 
s.sendmail("sender-email@gmail.com", "recv@anymail.com", message) 
s.quit() 
