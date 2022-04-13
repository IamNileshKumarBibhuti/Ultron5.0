from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

Code_For_ChatBot = Flask(__name__)

english_bot = ChatBot(
    "Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")


@Code_For_ChatBot.route("/")
def home():
    return render_template("User_To_ChatBot.html")


@Code_For_ChatBot.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    Code_For_ChatBot.run()
