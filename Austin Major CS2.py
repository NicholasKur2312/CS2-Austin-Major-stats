#!/usr/bin/env python
# coding: utf-8

# This is some stats from the recent CS2 Austin Major tournament just because I want to see some stats. <br>
# Data is obtained from [hltv.org](https://www.hltv.org/stats/players?event=7902) and put into a sheet. <br>
# I want to see how much certain players carried their team i.e. how much a player overperforms compared to their team.

# # 1. Import libraries and data

# In[106]:


import pandas as pd
import numpy as np

import seaborn
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 80)


# In[58]:


players = pd.read_excel("CS2 Austin major performance.xlsx")


# # 2. Preliminary check on data

# In[61]:


players
# 16 teams * 5 players = 80 rows - correct


# In[63]:


players.groupby("Teams").count()
# 5 entries for each team means 5 players - correct


# # 3. Getting team averages

# We will simply graph their rating against their team's average rating and see who belongs where in the graph. <br>
# A scatterplot sounds good for this kind of task.

# In[84]:


# getting averages for team
players["Team average rating"] = players.groupby("Teams")["Rating2.1"].transform('mean')


# In[90]:


players


# # 4. Plotting
# 
# 
#    

# In[137]:


statplot = seaborn.scatterplot(data = players, x = "Team average rating", y = "Rating2.1", hue = "Teams")

# label with names
for index, row in players.iterrows():
        statplot.text(row["Team average rating"], row["Rating2.1"], row['Player'], ha='center', va='bottom')


#bigger plot
seaborn.set_theme(rc={'figure.figsize':(10, 10)})
plt.show()


# From the graph, it is very clear how much a player overperforms compared to others because the team members are all within a line. Although some players may be very similar and next to each other. As such, it passes the eye test that donk and ZywOo are leagues ahead, representing the no 1 and 3 players in HLTV's 2024 top 20 players. <br><br>
# 
# Notable players include XANTARES, s1mple, Senzu and dumau who are quite ahead of their colleagues. Especially the latter two whose teams performed quite above expectations when they entered the tournament.

# In[ ]:




