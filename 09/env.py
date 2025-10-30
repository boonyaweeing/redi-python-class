"""
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]

plt.plot(x)
plt.show()
"""

import plotly.express as px

x = [1,2,3,4,5]
y = [2, 4, 6,8, 10]

fig = px.scatter(x,y)
fig.show()