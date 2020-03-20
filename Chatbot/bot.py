from chatterbot import ChatBot

botcito = ChatBot(

	"Example",
	trainer = "chatterbot.trainers.ChatterBotCorpusTrainer"
	)

"""botcito.train(
	"chatterbot.corpus.spanish"
	)"""

while 1:
	user = input(">> ")
	answer = botcito.get_response(user)
	print(str(answer))