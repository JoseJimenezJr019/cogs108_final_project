# pandas and numpy
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns

# applying plot settings for seaborn
sns.set(font_scale=2, style="white")

# set plotting size parameter
plt.rcParams['figure.figsize'] = (12, 5)

traffic_collisions = pd.read_csv('datasets/traffic_collisions/pd_collisions_datasd_v1.csv')
traffic_collisions_dictionary = pd.read_csv('datasets/traffic_collisions/pd_collisions_dictionary_datasd.csv')
date_time = traffic_collisions['date_time'].str.split(' ', n=1, expand=True)
traffic_collisions = traffic_collisions.drop(['date_time'], axis=1)
traffic_collisions['date'] = date_time[0]
traffic_collisions['time'] = date_time[1]

plt.hist(traffic_collisions['time'])
plt.show()
