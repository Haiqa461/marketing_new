import pandas as pd
import matplotlib.pyplot as plt
info = pd.read_csv('CC GENERAL.csv')
info_present = info.head(10)
info_present.plot( )
plt.show()