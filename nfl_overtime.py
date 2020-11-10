#!/usr/bin/env python3
#####################################
#    LAST UPDATED     14 OCT 2020   #
#####################################
"""
Program that takes information from the NFL Overtime spreadsheet and does some basic
dataframe analysis to calculate the percentage of NFL teams that win the game, given that
they won the overtime coin toss.

Bayes Thereom discussion?

              P(A)*P(B|A)
P(A|B)  =    -------------
                  P(B)

Probability of winning the game given that you have won the coin toss
                  (A)                              (B)

"""
import os
import sys
import pandas as pd

# load the df with all of the overtime information
try:
    df = pd.read_excel('overtimes_clean.xlsx', sheet_name='Sheet')
except FileNotFoundError:
    df = pd.read_excel('/Users/Alex/Documents/Python3/nfl_overtime/overtimes_clean.xlsx', sheet_name='Sheet')

# create dfs for the "won the coin toss" groups
df_won_toss = df[df["Won OT toss"] == True]  # same thing as df[df["Won OT toss"] == True]
df_won_toss_won = df_won_toss[df_won_toss["Result"] == 'W']
df_won_toss_lost = df_won_toss[df_won_toss["Result"] == 'L']
df_won_toss_tied = df_won_toss[df_won_toss["Result"] == 'T']

# create the dfs for the "lost the coin toss" groups
df_lost_toss = df[df["Won OT toss"] == False]
df_lost_toss_won = df_lost_toss[df_lost_toss["Result"] == 'W']
df_lost_toss_lost = df_lost_toss[df_lost_toss["Result"] == 'L']
df_lost_toss_tied = df_lost_toss[df_lost_toss["Result"] == 'T']

# create the dfs for the total win, loss, or tie dfs
df_won = df[df["Result"] == 'W']
df_lost = df[df["Result"] == 'L']
df_tied = df[df["Result"] == 'T']

print('Of the teams who won the coin toss, {:.1f}% won, {:.1f}% lost, and'
      ' {:.1f}% tied'.format((len(df_won_toss_won)/len(df_won_toss))*100,
                             (len(df_won_toss_lost)/len(df_won_toss))*100,
                             (len(df_won_toss_tied)/len(df_won_toss))*100))

print('Of the teams who lost the coin toss, {:.1f}% won, {:.1f}% lost, and'
      ' {:.1f}% tied'.format((len(df_lost_toss_won)/len(df_lost_toss))*100,
                             (len(df_lost_toss_lost)/len(df_lost_toss))*100,
                             (len(df_lost_toss_tied)/len(df_lost_toss))*100))
