#!/usr/bin/env python3
#####################################
#    LAST UPDATED     07 DEC 2020   #
#####################################
"""
Program that takes information from the NFL Overtime spreadsheet and does some basic
dataframe analysis to calculate the percentage of NFL teams that win the game, given that
they won the overtime coin toss.

"""
import os
import sys
import pandas as pd

# load the df with all of the overtime information
try:
    df = pd.read_excel('overtimes_clean.xlsx', sheet_name='Sheet')
except FileNotFoundError:
    os.chdir(os.path.dirname(__file__))
    df = pd.read_excel('overtimes_clean.xlsx', sheet_name='Sheet')

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

print('Of the teams who won the coin toss, {:.1%} won, {:.1%} lost, and'
      ' {:.1%} tied'.format(len(df_won_toss_won)/len(df_won_toss),
                            len(df_won_toss_lost)/len(df_won_toss),
                            len(df_won_toss_tied)/len(df_won_toss)))

print('Of the teams who lost the coin toss, {:.1%} won, {:.1%} lost, and'
      ' {:.1%} tied'.format(len(df_lost_toss_won)/len(df_lost_toss),
                            len(df_lost_toss_lost)/len(df_lost_toss),
                            len(df_lost_toss_tied)/len(df_lost_toss)))
