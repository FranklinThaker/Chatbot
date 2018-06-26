# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 09:24:14 2018

@author: Frank
"""

from chatterbot import ChatBot #importing the chatbot

bot = ChatBot('Jarvis') #Creating Object of ChatBot

while(1):
    request = input("You: ")
    response = bot.get_response(request)
    print("Jarvis: ", response)