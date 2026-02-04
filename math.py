from chatterbot import chatbot

bot = chatbot("math_bot", logic_adaptors=["chatterbot.logic.mathematical_evaluation"])

print ("-----------------math bot activated------------------")
while True:
    user_text = input("you:")
    print("chatbot:"+str(bot.get_response(user_text)))
