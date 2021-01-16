# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot(
    "Teste", read_only = True,
    logic_adapters = [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'])
trainer = ListTrainer(bot)

for arq in os.listdir("conversation"):
    chats = open("conversation/" + arq, 'r').readlines()
    trainer.train(chats)


while True:
    question = input("User: ")
    response = bot.get_response(question)
    print("Bot: " + str(response))