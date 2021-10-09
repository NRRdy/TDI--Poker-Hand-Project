# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 02:14:51 2021

@author: nrr50
"""

import pandas as pd
import numpy as np

suitNumbers =   np.concatenate((np.repeat(1, 13), np.repeat(2, 13), np.repeat(3, 13), np.repeat(4, 13)))
suitNames = ["Hearts"] * 13 + ["Spades"] * 13 + ["Diamonds"] * 13 + ["Clubs"] * 13
rankNumbers = np.concatenate((range(1,14), range(1,14), range(1,14), range(1,14)))
rankNames = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"] * 4

DeckOfCards = pd.DataFrame(list(zip(suitNumbers, suitNames, rankNumbers, rankNames))
                           , columns = ["Suit_Numbers", "Suit_Names", "Rank_Numbers", "Rank_Names"])

YourHand = DeckOfCards.sample(5, replace = False)

print("You have been dealt a " + YourHand.iloc[0, 3] + " of " + YourHand.iloc[0, 1] +
      ", a " + YourHand.iloc[1, 3] + " of " + YourHand.iloc[1, 1] + 
      ", a " + YourHand.iloc[2, 3] + " of " + YourHand.iloc[2, 1] + 
      ", a " + YourHand.iloc[3, 3] + " of " + YourHand.iloc[3, 1] + 
      ", and a " + YourHand.iloc[4, 3] + " of " + YourHand.iloc[4, 1])
