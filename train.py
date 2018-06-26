# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 09:11:36 2018

@author: Frank
"""

from chatterbot.trainers import ListTrainer #method to train the chatbot
from chatterbot import ChatBot #importing the chatbot
import os

bot = ChatBot('Jarvis') #Creating Object of ChatBot

bot.set_trainer(ListTrainer) #Set the trainer

for _data in os.listdir('data'):
    chats = open('data/' + _data,'r', encoding="utf8").readlines()
    
    bot.train(chats)
    
    
    
    
    
    
    
    
    
