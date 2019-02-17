""""
File: datathon2019.py
Goal: To import data and apply our group's model in order to predict stock closing values.
Author(s): Evan LeClercq
Date: 16/02/2019 (DD/MM/YYYY)
Copr: Copyright © 2019 Evan LeClercq. All Rights Reserved.

Modified By: NAME. Copyright © 2019 NAME. All Rights Reserved.
"""

############################################################
# Libraries
############################################################
import pandas as pd
import numpy as np
import tensorflow as tf
import internetarchive as ia
import newspaper
from newspaper import news_pool, Source
import time
import re
############################################################

start_time = time.timer()

############################################################
# Classes
############################################################
class Data:

    def __init__(self):
        # Download necessary data to be used by Model
        import newspaper
        from newspaper import Source, news_pool
        forbes_papers = newspaper.build('http://forbes.com')
        bloomberg_papers = newspaper.build('http://bloomberg.com')
        papers = [forbes_papers, bloomberg_papers]
        news_pool.set(papers, threads_per_source=3)
        news_pool.join()
        print(papers.size())

        self.df_MMM = pd.read_csv('MMM.csv', r)
        self.df_HON = pd.read_csv('HON.csv', r)
        self.df_SYF = pd.read_csv('SYF.csv', r)
        self.df_BAYZF = pd.read_csv('BAYZF.csv', r)

        pass

class Model(tf.keras.Model):

  def __init__(self):
    super(Model, self).__init__()
    self.layer1 = tf.keras.layers.Dense(4, activation=tf.nn.relu)
    self.layer2 = tf.keras.layers.Dense(50, activation=tf.nn.sigmoid)
    self.layer3 = tf.keras.layers.Dense(50, activation=tf.nn.sigmoid)
    self.layer4 = tf.keras.layers.Dense(50, activation=tf.nn.sigmoid)
    self.layer5 = tf.keras.layers.Dense(1, activation=tf.nn.tanh)

  def call(self, input):
    x = self.layer1(input)
    return self.layer2(x)
############################################################



############################################################
# Running the Model
############################################################

model = Model()

############################################################

end_time = start_time - time.timer()

############################################################
# Output
############################################################

print("Runtime: ", end_time, "[s]")

file('BAYZF.csv', 'w')
file('BAYZF.csv', 'w')
file('BAYZF.csv', 'w')
file('BAYZF.csv', 'w')

############################################################
