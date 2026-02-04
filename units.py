from chatterbot import ChatBot

bot = ChatBot(
    "units_bot",
    logic_adapters=[
        'chatterbot.logic.UnitConversion',
        'chatterbot.logic.BestMatch'
    ]
)

print("-----------------units bot activated------------------")

while True:
    user_text = input("ask a question(unit conversion): ")
    response = bot.get_response(user_text)
    print(response)


