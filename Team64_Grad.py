""""
File:       datathon2019.py
Goal:       To import data and apply our group's model in order to predict stock closing values.
Author(s):  Evan LeClercq
Date:       16/02/2019 (DD/MM/YYYY)
Copr:       Copyright © 2019 Evan LeClercq. All Rights Reserved.
"""

############################################################
# Libraries
############################################################
import pandas as pd
import numpy as np
import tensorflow as tf
import vaderSentiment as vs
from yahoo_fin.stock_info import *
from bs4 import BeautifulSoup
import urllib
import time
import re
############################################################

start_time = time.time()

############################################################
# Classes
############################################################
class WebScraper:

    def __init__(self):

        ### QUALITATIVE DATA ###

        page_MMM = 'https://www.forbes.com/search/?q=MMM'
        page_HON = 'https://www.forbes.com/search/?q=HON'
        page_SYF = 'https://www.forbes.com/search/?q=SYF'
        page_BAYZF_1 = 'https://www.forbes.com/search/?q=bayer'
        page_BAYZF_2 = 'https://www.forbes.com/search/?q=BAYZF'

        html_unp_MMM = urllib.request.urlopen(page_MMM)
        html_unp_HON = urllib.request.urlopen(page_HON)
        html_unp_SYF = urllib.request.urlopen(page_SYF)
        html_unp_BAYZF_1 = urllib.request.urlopen(page_BAYZF_1)
        html_unp_BAYZF_2 = urllib.request.urlopen(page_BAYZF_2)

        html_p_MMM = BeautifulSoup(html_unp_MMM, 'html.parser')
        html_p_MMM = BeautifulSoup(html_unp_MMM, 'html.parser')
        html_p_MMM = BeautifulSoup(html_unp_MMM, 'html.parser')
        html_p_MMM = BeautifulSoup(html_unp_MMM, 'html.parser')
        html_p_MMM = BeautifulSoup(html_unp_MMM, 'html.parser')

        # formatting:  <div class="stream-item__<name of thing>">
        self.summary_MMM = html_p_MMM.body.find_all('div', attrs={'class':'stream-item__description'})
        self.date_MMM = html_p_MMM.body.find_all('div', attrs={'class':'stream-item__date'})

        self.summary_HON = html_p_HON.body.find_all('div', attrs={'class':'stream-item__description'})
        self.date_HON = html_p_HON.body.find_all('div', attrs={'class':'stream-item__date'})

        self.summary_MMM = html_p_MMM.body.find_all('div', attrs={'class':'stream-item__description'})
        self.date_MMM = html_p_MMM.body.find_all('div', attrs={'class':'stream-item__date'})

        self.summary_MMM = html_p_MMM.body.find_all('div', attrs={'class':'stream-item__description'})
        self.date_MMM = html_p_MMM.body.find_all('div', attrs={'class':'stream-item__date'})

        self.summary_MMM = html_p_MMM.body.find_all('div', attrs={'class':'stream-item__description'})
        self.date_MMM = html_p_MMM.body.find_all('div', attrs={'class':'stream-item__date'})


        ### QUANTITATIVE DATA ###

        #self.pddf_MMM_info = get_analysts_info('MMM')
        #self.pddf_HON_info = get_analysts_info('HON')
        #self.pddf_SYF_info = get_analysts_info('SYF')
        #self.pddf_BAYZF_info = get_analysts_info('BAYZF')

        pass

    def getStatus():
        pass

"""
class Model(tf.keras.Model):

    def __init__(self):
        super(Model, self).__init__()
        self.layer1 = tf.keras.layers.Dense(4, activation=tf.nn.relu)
        self.layer2 = tf.keras.layers.Dense(50, activation=tf.nn.sigmoid)
        pass

    def call(self, input):
        x = self.layer1(input)
        return self.layer2(x)
"""
############################################################



############################################################
# Running the Model
############################################################
WEBSCRAPER = WebScraper()

"""
model = Model()
"""
############################################################

end_time = start_time - time.time()

############################################################
# Output
############################################################

print("Runtime: ", end_time, "[s]")

############################################################
