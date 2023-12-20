#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace 'twitter_data.csv' with your file path)
twitter_data = pd.read_csv("C:\\Users\\compaq\\Desktop\\twitter_training.csv")
print(twitter_data.columns)
# Assuming the dataset contains a 'Sentiment' column indicating sentiment (positive, negative, neutral)
sentiment_counts = twitter_data['Sentiment'].value_counts()

# Plotting sentiment distribution
plt.figure(figsize=(8, 6))
sentiment_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Sentiment Distribution in Twitter Data')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




