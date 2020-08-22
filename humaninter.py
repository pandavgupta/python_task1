import os
import pyttsx3
import smtplib,ssl
import mylogin
import time


pyttsx3.speak("Welcome to human interaction platform")
pyttsx3.speak("Tell me how can i help you sir")

while True:
    
  p= input("Tell me how can i help you : ")
  p=p.lower()

  if ((("open" in p) or ("launch" in p)) and (("chrome" in p) or ("browser" in p))):
    os.system("chrome")
  elif (("mail" in p) or ("email" in p)):
    pyttsx3.speak("Enter your message")
    message=input("Enter your message: ")
    pyttsx3.speak("To whom you want to send mail")
    to= input("To : ")
    context = ssl.create_default_context()
    server=smtplib.SMTP_SSL("smtp.gmail.com",465, context=context)
    server.ehlo()
    server.login(mylogin.user,mylogin.password)
    server.sendmail(mylogin.password,to,message)
    server.close()
    time.sleep(5)
    pyttsx3.speak("Email is sent successfully ")
  elif ( ("search" in p)or ("find" in p)):
    pyttsx3.speak("Tell me what you want to search")
    str=input("Search : ")
    i=0
    while i!=len(str):
        if (str[i] == ' '): 
            str = str.replace(str[i], '+') 
        i=i+1

    os.system(f"chrome https://www.google.com/search?q={str}") 
    time.sleep(2)
    pyttsx3.speak("Here is you search result")
  elif ((("play" in p) or ("open" in p) or ("launch" in p)) and ("music" in p)):
    os.system(r'start /d "%ProgramFiles(x86)%\Windows Media Player" wmplayer.exe')
  elif ((("go" in p) or ("open" in p) or ("launch" in p)) and ("wordpad" in p) or ("msword" in p)):
    time.sleep(1)
    os.system(r'start /d "%ProgramFiles%\Windows NT\Accessories" wordpad.exe ')
  elif ((("go" in p) or ("open" in p) or ("launch" in p)) and ("youtube" in p)):
    pyttsx3.speak("Tell me what you want to search on youtube")
    str=input("Search : ")
    i=0
    while i!=len(str):
        if (str[i] == ' '): 
            str = str.replace(str[i], '+') 
        i=i+1

    os.system(f"chrome https://www.youtube.com/results?search_query={str}") 
    time.sleep(2)
    pyttsx3.speak("Here is you search result")
  elif ((("go" in p) or ("open" in p) or ("launch" in p)) and ("facebook" in p)):
    os.system("chrome facebook.com")
  elif ((("open" in p) or ("launch" in p)) and ("notepad" in p)):
    os.system(r'"%windir%\system32\notepad.exe"')
  elif ((("open" in p) or ("launch" in p)) and ("linkdein" in p)):
    os.system("chrome https://www.linkedin.com/feed/")
  elif (("end" in p) or ("exit")):
    pyttsx3.speak("Have a nice day sir") 
    exit()
  else:
    pyttsx3.speak("This is not supported")
 