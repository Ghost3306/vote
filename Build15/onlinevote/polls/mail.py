import smtplib  
import random   




def mail_send(email,message):
    sender_mail = 'jessicasobinpinto@gmail.com'    
          
    password = "croqzqflhbpgslpr" 
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_mail, password)
    s.sendmail(sender_mail, email, message)
    s.quit()
    print("mail send successful")
    return True




