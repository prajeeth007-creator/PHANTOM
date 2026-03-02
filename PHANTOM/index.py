from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize BMO
bot = ChatBot(
    "BMO",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "BMO does not compute!",
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
def get_response():
    # This 'userMessage' must match the JS fetch URL
    user_text = request.args.get("userMessage") 
    if user_text:
        return str(bot.get_response(user_text))
    return "I didn't hear you!"

if __name__ == "__main__":
    app.run(debug=True)