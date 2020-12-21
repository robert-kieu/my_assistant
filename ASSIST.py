import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import webbrowser as wb
import os
import re

Jace = pyttsx3.init()
voice = Jace.getProperty('voices')
Jace.setProperty('voice', voice[1].id)

def talk(audio):
	print('JACE : ' + audio)
	Jace.say(audio)
	Jace.runAndWait()

def time():
	Time = datetime.datetime.now().strftime('%I: %M: %p')
	talk('this is ' + Time)

def welcome():
	now = datetime.datetime.now()
	talk('to day is day %d of month %d, %d'  %(now.day, now.month, now.year))
	hour = now.hour
	if hour >= 5 and hour <= 12:
		talk('good morning sir, have a nice day!')
	elif(hour > 12 and hour < 18):
		talk('good afternoon sir, what is your plan?')
		boss_ans = Listen().lower()
		if 'no' in boss_ans: talk('oh why not play with me')
		else: talk('good luck to you')
	else:
		talk('good night sir have you eat diner yet?')
		boss_ans = Listen().lower()
		if 'yes' in boss_ans: talk('it is sound good')
		else: talk('''oh let's find something for dinner''')
	talk('How can I help you')

def openwebsite(domain):
	url = ''
	if '.' in domain:
		if 'google' in domain or 'youtube' in domain or 'shopee' in domain:
			talk(f'what should I search boss?')
			search = Listen().lower()
			url = 'https://www.' + domain + '''/search?q=''' + search
		else:
			url = 'https://www.' + domain
			talk(f'the web page you requested has been opened')
	else: talk(f'something wrong please try again')
	return url


def Listen():
	lis = sr.Recognizer()
	with sr.Microphone() as source:
		lis.pause_threshold = 1
		audio = lis.listen(source)
	try:
		query = lis.recognize_google(audio, language = 'en')
		print('Master : ' + query)
	except sr.UnknownValueError:
		print('please repeat or typing command : ')
		query = str(input('Master : '))
	return query

if __name__ == '__main__':
	welcome()
	query = ''
	while True:
		print('I am listening...')
		query = Listen().lower()
		if 'search' in query or 'website' in query:
			talk('which website you want me to open boss')
			domain = Listen().lower()
			url = openwebsite(domain)
			wb.get().open(url)
			talk(f'here is what i found')
		elif 'time' in query: time()
		elif 'brave' in query:
			talk('Welcome to brave BOSS')
			f = r'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'
			os.startfile(f)
		elif 'music' in query:
			talk('Just relax BOSS')
			f = r'C:/Users/84918/Desktop/music/Tu-Bo-Cover-ERIK.mp3'
			os.startfile(f)
		elif 'bye' in query or 'stop' in query:
			talk('Goodbye Sir')
			quit()
		elif 'thank you' in query:
			talk(f'not at all, that is my pleasure')
		else : talk(f'try again please')