# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

bot = ChatBot(
    "Teste", read_only = True,
    logic_adapters = [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'])
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.portuguese")


while True:
    question = input("User: ")
    response = bot.get_response(question)
    print("Bot: " + str(response))