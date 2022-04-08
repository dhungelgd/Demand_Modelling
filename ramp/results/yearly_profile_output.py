import random

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#Create Yearly profile by concatenating the monthly profiles
Profiles= {}
for i in range (1,13):
    Profiles[i]=pd.read_csv('output_file_{}.csv'.format(i),usecols=['0'])/1000
Yearly_Profile = pd.concat(Profiles.values())
Yearly_Profile = Yearly_Profile.apply(lambda x: x + random.uniform(-0.2*x,0.2*x))
Yearly_Profile.columns = ['kW']
Yearly_Profile.to_csv('yearly_profile.csv',index=None)

# Plot the yearly profile
plt.figure(figsize=(10, 5))
plt.plot(np.arange(len(Yearly_Profile)), Yearly_Profile.values, '#4169e1')
plt.xlabel('Hours')
plt.ylabel('Power (kW)')
plt.ylim(ymin=0)
# plt.ylim(ymax=5000)
plt.margins(x=0)
plt.margins(y=0)
# plt.xticks([0,240,480,(60*12),(60*16),(60*20),(60*24)],[0,4,8,12,16,20,24])
plt.savefig('yearly_profiles.png', format='png', dpi=1000)
plt.show()