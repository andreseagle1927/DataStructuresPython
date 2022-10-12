
from chatterbot import ChatBot

chat = ChatBot("cctmx")

while True:
    respuesta = input("write something: \n")

    bot = chat.get_response(respuesta)

    print(bot)