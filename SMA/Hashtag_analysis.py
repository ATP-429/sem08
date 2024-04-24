# Exp 4

'''
To determine which hashtags are most popular among different user groups, we can use the following approach:

- Read in the CSV file containing the social media data and filter it to include only the columns we need (e.g. user ID, user group, and hashtags).
- Split the hashtags into individual words and count their frequency for each user group.
- Plot the top N most frequent hashtags for each user group in a bar chart.
'''

import pandas as pd
import matplotlib.pyplot as plt

from gensim import corpora

# Read in the CSV file
df = pd.read_csv('sma/hashtag_analysis.csv')
#df.set_index('user_group')
df_by_group = df.groupby('user_group')

for group in df['user_group'].unique():
    hashtags = df[df["user_group"] == group]['hashtags'].apply(lambda x: x.split(' '))
    dct = corpora.Dictionary(hashtags)
    plt.bar([x[0] for x in dct.most_common()], [x[1] for x in dct.most_common()])
    plt.title(group)
    plt.show()
    