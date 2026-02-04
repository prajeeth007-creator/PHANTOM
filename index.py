from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request

app = Flask(__name__)

bot = ChatBot(
    "HARSH",
    read_only=False,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I am sorry, I don't have an answer for that.",
            "maximum_similarity_threshold": 0.90
        }
    ]
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('userMessage')
    return str(bot.get_response(userText))




if __name__ == "__main__":
    app.run(debug=True)
 