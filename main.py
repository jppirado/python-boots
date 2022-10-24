import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia


#metodo usando para obter a voz em forma de string
def takeCommand():

	#Reconhecimento 
	r = sr.Recognizer()

	#microfone, aqui é feita a entrada de audio
	with sr.Microphone() as source:
		print('Fale agora!')
		
		#tempo de espera para finaliazar uma frase
		r.pause_threshold = 0.7
		audio = r.listen(source)

		#tratando a exessão, se o audio for reconhecido 
		try:
			print("Reconhecendo")
			
			#aqui é possivel trocar o idioma e obter o que voce disse na forma de texto
			Query = r.recognize_google(audio, language='pt-br')
			print("Você disse ", Query)
			
		except Exception as e:
			print(e)
			print("Não foi possível entender o que você disse")
			return "None"
		
		return Query

#usado na fala do robo
def speak(audio):
	
	#inicia o robo

	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	
	#verifica se a voz é feminina ou masculina
	engine.setProperty('voice', voices[0].id)
	
	#output do boot
	engine.say(audio)
	
	#manipula a fila de instruções geradas pelo robo
	engine.runAndWait()


def Hello():
	#fala inicial do robo
	speak("Olá")


def Take_query():

	Hello()
	#fluxo do nosso programa
	#looping infinito até seja dito tchau
	while(True):
		
		
		query = takeCommand().lower()

		if "open geeksforgeeks" in query:
			speak("Opening GeeksforGeeks ")
			webbrowser.open("www.geeksforgeeks.com")
			continue
		
		elif "abrir mapa" in query:
			speak("Opening Google ")
			webbrowser.open("https://www.google.com.br/maps")
			continue
			
		
		elif "preciso saber" in query:
			print("sobre o que voce deseja saber?")
			query2 =  takeCommand().lower() 

			wikipedia.set_lang('pt') 
			speak("Checking the wikipedia ")
			query2 = query2.replace("wikipedia" , '' )
		
			result = wikipedia.summary(query2, sentences=4)
			print ( result)
			speak("According to wikipedia")
			speak(result)
			continue
		
		elif "tell me your name" in query:
			speak("I am Jarvis. Your desktop Assistolaant")

		
		# encerra o fluxo de execução do programa
		elif "bye" in query:
			speak("Bye. Check Out GFG for more exciting things")
			exit()

if __name__ == '__main__':
	Take_query()
