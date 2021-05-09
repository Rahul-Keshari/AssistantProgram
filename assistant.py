import pyttsx3
import webbrowser
import os
import speech_recognition
import wikipedia
import datetime
import time
import random
from datetime import date



owner = "Rahul Keshari"

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning "+owner)
        pyttsx3.speak("Good Morning "+ owner+"!")

    elif hour >= 12 and hour < 18:
        print("Good Afternoon "+ owner+"!")
        pyttsx3.speak("Good Afternoon "+ owner+"!")

    else:
        print("Good Evening "+ owner+"!")
        pyttsx3.speak("Good Evening "+ owner+"!")
 
#pyttsx3.speak("Hello I am jadoo")
wishMe()

while True:

	print("Hello! I'm your assistant. Tell me the requirement? : "  , end="")
	r = speech_recognition.Recognizer()
	r.energy_threshold=4000
	with speech_recognition.Microphone() as man:
		print("start saying...")
		audio = r.listen(man)
		print("ok done...")
	audio.frame_data
	
	try:
		p= r.recognize_google(audio)         # recognize speech using Google Speech Recognition
	except IndexError:                                  # the API key didn't work
		print("No internet connection")
	except KeyError:                                    # the API key didn't work
		print(" ")
	except LookupError :                                 # speech is unintelligible
		print(" ")
	except speech_recognition.UnknownValueError as u:
		p=" "

	#print(p)
	
	#pyttsx3.speak("Okay proceeding")
	#p = input()
	if p== " ":
		pyttsx3.speak("Requirement can't be empty")
	else :
		p=p.lower()
	print("You said:  "+ p)
	if (("not" in p) or ("never" in p) or ("don't" in p) or ("dont" in p) or ("do not" in p) or ("stop" in p) ):
		#pyttsx3.speak("Okay!")
		pyttsx3.speak("Okay! Give me other requirement:")
		
	elif(("run" in p) or  ("execute" in p ) or  ("open" in p ) or ("go to" in p ) or ("start" in p )) and ( ("internet explorer" in p) or ("internet browser" in p) or ("microsoft edge" in p) or ("microsoftedge" in p)):
		 
		os.system("start microsoft-edge:")
		

	elif(("run" in p) or  ("execute" in p ) or  ("open" in p ) or ("go to" in p ) or ("start" in p )) and ( ("file explorer" in p) or ("this pc" in p) or ("my pc" in p)):
		 
		os.system("explorer")

	elif(("open" in p) or ("execute" in p) or ("start" in p) or ("go to" in p)) and (("bluetooth" in p)):
		 
		os.system("fsquirt")

	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or ("open" in p ) or ("start" in p )) and (("notepad" in p) or ("editor" in p) or ("text editor" in p) ) :
		 
		os.system("notepad")

	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or ("open" in p ) or ("start" in p )) and (("calculator" in p) or ("calculators" in p) or ("claculating application" in p) ) :
		 
		os.system("calc")

	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or ("open" in p ) or ("start" in p )) and (("one note" in p) or ("onenote" in p) or ("notebook" in p) ) :
		 
		os.system("onenote.exe")
	
	elif (("run" in p) or ("go to" in p ) or ("open" in p ) or ("start" in p ) or ("execute" in p)) and (("media player" in p) or ("video player" in p) or ("player" in p)):
		 
		os.system("wmplayer")

	elif (("run" in p) or ("execute" in p ) or ("go to" in p ) or ("open" in p ) or ("start" in p )) and (("ms word" in p) or ("word" in p) or ("microsoft word" in p)):
		 
		os.system("winword")

	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or ("go to" in p ) or  ("open" in p ) or  ("start" in p )) and  (("powerpoint" in p) or ("ms powerpoint" in p) or ("microsoft powerpoint" in p) or ("presentation application" in p) ) :
		 
		os.system("powerpnt")

	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or ("go to" in p ) or  ("open" in p ) or  ("start" in p ) or ("ms paint" in p) or ("microsoft paint" in p)) and  (("mspaint" in p) or ("ms paint" in p) or ("microsoft paint" in p) or ("paint" in p) ) :
		 
		os.system("mspaint")

	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or ("go to" in p ) or  ("open" in p ) or  ("start" in p ) or ("ms paint" in p) or ("microsoft paint" in p)) and  (("mspaint" in p) or ("ms paint" in p) or ("microsoft paint" in p) or ("paint" in p) ) :
		 
		os.system("mspaint")

	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or ("go to" in p ) or  ("open" in p ) or  ("start" in p ) or ("cmd" in p) or ("command prompt" in p)) and  (("command prompt" in p) or ("cmd" in p) or ("terminal" in p) ) :
		 
		os.system("cmd")

	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or ("go to" in p ) or  ("open" in p ) or  ("start" in p ) or ("powershell" in p) or ("power shell" in p)) and  (("powershell" in p) ) :
		 
		os.system("powershell")

	elif((("show" in p) or ("run" in p) or ("display" in p) or ("my ip" in p)) and ( ("my ip" in p) or ("ipconfig" in p)) ):
		os.system("ipconfig")

	elif (("date" in p ) or ("current" in p ) or ("today" in p ) or  ("today's" in p ) or  ("todays" in p )) and  ( ("date" in p) ) :
		 
		os.system("date /t")

	elif (("time" in p ) or ("current" in p ) or ("time now" in p )  or  ("live timimg" in p )) and  ( ("time" in p)  ) :
		 
		os.system("time /t")

	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or  ("open" in p ) or  ("start" in p )) and  (("camera" in p) or ("take photo" in p) ) :
		 
		os.system("start microsoft.windows.camera:")

	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or  ("open" in p ) or  ("start" in p )) and  (("recorder" in p) or ("recording" in p) ) :
		
		os.system("soundrecorder")

	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or  ("open" in p ) or  ("start" in p )) and  (("excel" in p) or ("spreadsheet" in p) or ("worksheet" in p) or ("workbook" in p) ) :
		 
		os.system("excel")


	elif (("run" in p) or  ("execute" in p ) or ("open" in p ) or ("go to" in p ) or ("start" in p )) and  (("system info" in p)):
		 
		os.system("msinfo32")
	
	elif (("run" in p) or  ("execute" in p ) or ("open" in p ) or ("start" in p ) or ("go to" in p )) and  (("display settings" in p) ) :
		 
		os.system("utilman")

	elif (("run" in p) or  ("execute" in p ) or ("open" in p ) or ("start" in p ) or ("go to" in p )) and  (("settings" in p) or ("setting" in p) ) :
		 
		os.system("start ms-settings:")
		
	elif(("run" in p) or  ("execute" in p ) or ("open" in p ) or ("start" in p ) or ("go to" in p ) or ("wi fi" in p) or ("wifi" in p)) and (("wireless fidelity" in p) or ("wifi" in p) or ("wifi setting" in p)):
		 
		os.system("start ms-settings:network-wifi")
	elif(("run" in p) or  ("execute" in p ) or ("open" in p ) or ("start" in p ) or ("go to" in p ) or ("vpn" in p)) and (("vpn" in p)):
		 
		os.system("start ms-settings:network-vpn")

	elif(("run" in p) or  ("execute" in p ) or ("open" in p ) or ("go to" in p )) and ("storage" in p):
		 
		os.system("start ms-settings:storagesense")
	
	elif(("run" in p) or  ("execute" in p ) or ("open" in p ) or ("go to" in p )) and (("lockscreen" in p)):
		 
		os.system("start ms-settings:lockscreen")

	elif(("run" in p) or  ("execute" in p ) or ("open" in p ) or ("go to" in p )) and ("taskbar" in p):
		 
		os.system("start ms-settings:taskbar")

	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or  ("open" in p ) or  ("start" in p )) and  (("control panel" in p) ) :
		 
		os.system("Control appwiz.cpl")

	elif(("open" in p) or ("start" in p)) and (( "resolution" in p) or ("oreintation" in p) ):
		os.system("desk.cpl")
	
	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or  ("open" in p ) or  ("start" in p )) and  (("administrative tool" in p) or ("administrative tools" in p) ) :
		 
		os.system("Control admintools")
	
	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or  ("open" in p ) or  ("start" in p )) and  (("color manager" in p) or ("colour management" in p) or ("color management" in p) or ("colour manager")) :
		 
		os.system("colorcpl.exe")

	elif(("run" in p) or  ("execute" in p ) or ("go to" in p ) or  ("open" in p ) or  ("start" in p ) or ("firewall" in p) or ("firewal" in p)) and (("firewall" in p) or ("firewal" in p)):
		 
		os.system("firewall.cpl")

	elif(("ip configuration" in p) or  ("ipconfig" in p ) or ("go to" in p ) or  ("open" in p ) or  ("start" in p )) and (("ip configuration" in p) or  ("ipconfig" in p )):
		 
		os.system("ipconfig")


	elif (("show system info" in p) or ("show systeminfo" in p) or ("system info" in p) or ("system information" in p))  :
		 
		os.system("systeminfo")		

	elif (("open" in p) or  ("show" in p ) or ("show me" in p ) or ("display" in p )) and  ( ("window version" in p) or ("the version of windows" in p) or ("windows version" in p) or ("window version" in p) ) :
		 
		os.system("ver")
	

	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or ("open" in p ) or ("start" in p )) and (("device manager" in p) or ("device management") or ("devicemanager" in p) ) :
		 
		os.system("devmgmt.msc")

	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or ("open" in p ) or ("start" in p )) and (("task manager" in p) or ("task management") or ("task viewer") or ("taskmanager" in p) ) :
		 
		os.system("taskmgr")
		
	elif(("snipping tool" in p) or ("snipping tools") in p ):

		 os.system("snippingtool")
	
	elif(("sound" in p) or ("audio" in p) and ("device" in p)):
		os.system("mmsys.cpl")

	elif (("laptop" in p) or  ("desktop" in p ) or ("PC" in p ) or ("computer" in p )) and  (("shut down" in p) or ("shutdown" in p) or ("turn off the computer" in p) or ("turnoff the computer" in p) ) :
		 
		os.system("shutdown /s")

	elif (("laptop" in p) or  ("desktop" in p ) or ("pc" in p ) or ("computer" in p )) and  (("restart" in p )) :
		 
		os.system("shutdown /r")
	
	elif (("laptop" in p) or  ("desktop" in p ) or ("pc" in p ) or ("computer" in p )) and  (("log off" in p ) or ("logoff" in p )) :
		 
		os.system("shutdown /l")

	elif (("run" in p) or  ("execute" in p ) or ("open" in p ) or ("go to" in p ) or ("start" in p )) and  ( ("gmail" in p) or ("g-mail" in p) or ("email" in p) or ("e-mail" in p) or ("mailer" in p) or ("mailing" in p) ) :
		 
		webbrowser.open("https://mail.google.com/mail/u/0/")

	elif "wikipedia" in p:
		 
		pyttsx3.speak("Searching Wikipedia...") 
		p= p.replace("wikipedia", "") 
		results = wikipedia.summary(p, sentences = 5) 
		pyttsx3.speak("According to Wikipedia") 
		print(results) 
		pyttsx3.speak(results)
		
	elif (("date today" in p) or  ("today's date"in p) or ("today date" in p)  ): 
		today = date.today()
		print("Today's date:", today)

	elif ("location" in p or "maps" in p or "locate" in p ):
		if (("locate me " in p) or ("my location" in p)) :
			webbrowser.open("www.google.com/maps")
		elif "open maps" in p:
			webbrowser.open("www.google.com/maps")
		else:
			location = p.replace("location", "")
			location= p.replace("search","")
			webbrowser.open("https://www.google.co.in/maps/place/" + location)
		
	elif (("run" in p) or  ("execute" in p ) or  ("open" in p ) or ("go to" in p ) or ("start" in p ))  and ( ("chrome" in p) or ("browser" in p) or ("google chrome" in p)):		
		 
		os.system("chrome")
		
	elif (("news" in p) or ("open news" in p) or ("show news" in p)):
		webbrowser.open_new_tab("https://news.google.com/")

	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or  ("open" in p ) or  ("start" in p ) or ("online video" in p) or  ("play" in p ) or  ("play online video" in p )or  ("play video online" in p )) and  (("online video" in p) or ("play online video" in p ) or  ("play video online" in p ) or ("youtube" in p) or ("youtube" in p) or ("online video" in p) or ("video online" in p) ) :
		 
		webbrowser.open("https://www.youtube.com/watch?v=4Z3oHURLkds")

	elif (("run" in p) or  ("execute" in p ) or ("go to" in p ) or  ("open" in p ) or  ("start" in p )) and  (("map" in p ) or  ("google map" in p ) or  ("maps" in p ) or ("navigation" in p )):
		 
		webbrowser.open("https://www.google.com/maps")

	elif (("start" in p) or ("open" in p) or ("display" in p) or ("show" in p)) and (("news" in p) or ("today's news" in p)) :
		 
		webbrowser.open("https://news.google.co.in/")

	elif (("run" in p) or  ("execute" in p ) or ("open" in p ) or ("go to" in p ) or ("start" in p )) and  ( ("youtube" in p) ) :
		 
		webbrowser.open("https://www.youtube.com")

	elif (("run" in p) or  ("execute" in p ) or ("open" in p ) or ("go to" in p ) or ("start" in p )) and  ( ("whatsapp" in p) ) :
		 
		webbrowser.open("https://web.whatsapp.com/")

	elif (("show" in p) or ("open" in p ) or ("display" in p)) and (("weather" in p) or ("weather today" in p)):
		 
		webbrowser.open("https://www.google.com/search?q=weather&rlz=1C1CHBF_enIN915IN915&oq=weather&aqs=chrome..69i57j35i39j46j0l5.2122j1j1&sourceid=chrome&ie=UTF-8")

	elif (("run" in p) or  ("execute" in p ) or ("open" in p ) or ("go to" in p ) or ("start" in p ) or ("translate" in p)) and  ( ("translator" in p) or ("translate" in p) ) :
		 
		webbrowser.open("https://translate.google.com/")

	elif (("open" in p) or ("execute" in p) or ("go to" in p) or ("start" in p)) and (("charmap" in p) or ("character map" in p)):
		 
		os.system("charmap")

	

	elif  ("exit" in p)  or ("quit" in p) or ("terminate" in p) or ("end" in p):
		break

	else:
		print("Oops Sorry! can't process your request.")
		pyttsx3.speak( "We are working on an update to get you this feature.")