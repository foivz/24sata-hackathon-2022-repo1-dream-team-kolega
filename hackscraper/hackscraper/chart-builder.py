import matplotlib.pyplot as plt
import numpy as np

y = np.array([14.0, 20.49, 29.99, 74.99])
mylabels = ["NOVINE", "Zdravi_kutak", "Njega_i_higijena", "Bebe_i_mame"]
myexplode = [0, 0, 0, 0]
mycolors = ["#F5B700", "#00A1E4", "#DC0073", "#272932"]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True, colors=mycolors)
plt.show()