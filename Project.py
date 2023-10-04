import pandas as pd
import matplotlib.pyplot as plt
Rumors = pd.read_csv('RedditNews.csv')
Rumors.plot()
plt.show()