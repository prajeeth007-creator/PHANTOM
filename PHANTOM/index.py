from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request

app = Flask(__name__)

# ===== PHANTOM AI =====
bot = ChatBot(
    "PHANTOM",
    read_only=False,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I'm not sure how to respond to that yet.",
            "maximum_similarity_threshold": 0.90
        }
    ]
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# ===== ROUTES =====
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_response():
    user_text = request.args.get("userMessage")
    response = bot.get_response(user_text)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)