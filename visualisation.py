
import numpy as np
data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')
import matplotlib.pyplot as plt
ave_inflammation=np.mean(
  data,
  axis=0
)
plt.plot(ave_inflammation)
max_inlammation=np.max(
  data,
  axis=0
)
plt.plot(max_inflammation)
